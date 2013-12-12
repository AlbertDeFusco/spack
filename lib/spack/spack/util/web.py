import re
import subprocess
import urllib2
import urlparse
from multiprocessing import Pool
from HTMLParser import HTMLParser

import spack
import spack.error
import spack.tty as tty
from spack.util.compression import ALLOWED_ARCHIVE_TYPES

# Timeout in seconds for web requests
TIMEOUT = 10


class LinkParser(HTMLParser):
    """This parser just takes an HTML page and strips out the hrefs on the
       links.  Good enough for a really simple spider. """
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr, val in attrs:
                if attr == 'href':
                    self.links.append(val)


def _spider(args):
    """_spider(url, depth, max_depth)

       Fetches URL and any pages it links to up to max_depth.  depth should
       initially be 1, and max_depth includes the root.  This function will
       print out a warning only if the root can't be fetched; it ignores
       errors with pages that the root links to.

       This will return a list of the pages fetched, in no particular order.

       Takes args as a tuple b/c it's intended to be used by a multiprocessing
       pool.  Firing off all the child links at once makes the fetch MUCH
       faster for pages with lots of children.
    """
    url, depth, max_depth = args

    pages = {}
    try:
        # Make a HEAD request first to check the content type.  This lets
        # us ignore tarballs and gigantic files.
        # It would be nice to do this with the HTTP Accept header to avoid
        # one round-trip.  However, most servers seem to ignore the header
        # if you ask for a tarball with Accept: text/html.
        req = urllib2.Request(url)
        req.get_method = lambda: "HEAD"
        resp = urllib2.urlopen(req, timeout=TIMEOUT)

        if not resp.headers["Content-type"].startswith('text/html'):
            print "ignoring page " + url + " with content type " + resp.headers["Content-type"]
            return pages

        # Do the real GET request when we know it's just HTML.
        req.get_method = lambda: "GET"
        response = urllib2.urlopen(req, timeout=TIMEOUT)
        response_url = response.geturl()

        # Read the page and and stick it in the map we'll return
        page = response.read()
        pages[response_url] = page

        # If we're not at max depth, parse out the links in the page
        if depth < max_depth:
            link_parser = LinkParser()

            subcalls = []
            link_parser.feed(page)
            while link_parser.links:
                raw_link = link_parser.links.pop()

                # Skip stuff that looks like an archive
                if any(raw_link.endswith(suf) for suf in ALLOWED_ARCHIVE_TYPES):
                    continue

                # Evaluate the link relative to the page it came from.
                abs_link = urlparse.urljoin(response_url, raw_link)
                subcalls.append((abs_link, depth+1, max_depth))

            if subcalls:
                pool = Pool(processes=len(subcalls))
                dicts = pool.map(_spider, subcalls)
                for d in dicts:
                    pages.update(d)

    except urllib2.URLError, e:
        # Only report it if it's the root page.  We ignore errors when spidering.
        if depth == 1:
            raise spack.error.NoNetworkConnectionError(e.reason, url)

    return pages


def get_pages(root_url, **kwargs):
    """Gets web pages from a root URL.
       If depth is specified (e.g., depth=2), then this will also fetches pages
       linked from the root and its children up to depth.

       This will spawn processes to fetch the children, for much improved
       performance over a sequential fetch.
    """
    max_depth = kwargs.setdefault('depth', 1)
    pages =  _spider((root_url, 1, max_depth))
    return pages