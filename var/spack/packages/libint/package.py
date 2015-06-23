# FIXME:
# This is a template package file for Spack.  We've conveniently
# put "FIXME" labels next to all the things you'll want to change.
#
# Once you've edited all the FIXME's, delete this whole message,
# save this file, and test out your package like this:
#
#     spack install libint
#
# You can always get back here to change things with:
#
#     spack edit libint
#
# See the spack documentation for more information on building
# packages.
#
from spack import *

class Libint(Package):
    """FIXME: put a proper description of your package here."""
    # FIXME: add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "http://downloads.sourceforge.net/project/libint/v1-releases/libint-1.1.4.tar.gz"

    version('1.1.4', '6bc36ba047e23e16b5bc9c0cc8f4a9f7')

    # FIXME: Add dependencies if this package requires them.
    # depends_on("foo")

    def install(self, spec, prefix):
        # FIXME: Modify the configure line to suit your build system here.
        configure("--prefix=%s" % prefix)

        # FIXME: Add logic to build and install here
        make()
        make("install")
