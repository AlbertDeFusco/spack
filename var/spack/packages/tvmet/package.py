# FIXME:
# This is a template package file for Spack.  We've conveniently
# put "FIXME" labels next to all the things you'll want to change.
#
# Once you've edited all the FIXME's, delete this whole message,
# save this file, and test out your package like this:
#
#     spack install tvmet
#
# You can always get back here to change things with:
#
#     spack edit tvmet
#
# See the spack documentation for more information on building
# packages.
#
from spack import *

class Tvmet(Package):
    """FIXME: put a proper description of your package here."""
    # FIXME: add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "http://downloads.sourceforge.net/project/tvmet/Tar.Gz_Bz2%20Archive/1.7.2/tvmet-1.7.2.tar.bz2"

    version('1.7.2', '8e1b2ec67ebec65f680a8bd3ea38a656')

    # FIXME: Add dependencies if this package requires them.
    # depends_on("foo")

    def install(self, spec, prefix):
        # FIXME: Modify the configure line to suit your build system here.
        configure("--prefix=%s" % prefix)

        # FIXME: Add logic to build and install here
        make()
        make("install")
