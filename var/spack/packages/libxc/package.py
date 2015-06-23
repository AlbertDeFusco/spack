# FIXME:
# This is a template package file for Spack.  We've conveniently
# put "FIXME" labels next to all the things you'll want to change.
#
# Once you've edited all the FIXME's, delete this whole message,
# save this file, and test out your package like this:
#
#     spack install libxc
#
# You can always get back here to change things with:
#
#     spack edit libxc
#
# See the spack documentation for more information on building
# packages.
#
from spack import *

class Libxc(Package):
    """FIXME: put a proper description of your package here."""
    # FIXME: add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "http://www.tddft.org/programs/octopus/down.php?file=libxc/libxc-2.2.2.tar.gz"

    version('2.2.2', 'd9f90a0d6e36df6c1312b6422280f2ec')

    # FIXME: Add dependencies if this package requires them.
    depends_on("boost")

    def install(self, spec, prefix):
        # FIXME: Modify the configure line to suit your build system here.
        configure("--prefix=%s" % prefix)

        # FIXME: Add logic to build and install here
        make()
        make("install")
