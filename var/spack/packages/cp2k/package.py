# FIXME:
# This is a template package file for Spack.  We've conveniently
# put "FIXME" labels next to all the things you'll want to change.
#
# Once you've edited all the FIXME's, delete this whole message,
# save this file, and test out your package like this:
#
#     spack install cp2k
#
# You can always get back here to change things with:
#
#     spack edit cp2k
#
# See the spack documentation for more information on building
# packages.
#
from spack import *

class Cp2k(Package):
    """FIXME: put a proper description of your package here."""
    # FIXME: add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "http://downloads.sourceforge.net/project/cp2k/cp2k-2.6.1.tar.bz2"

    version('2.6.1', 'bbeb19e7d5f1e2d29b3efa966ce00c45')

    # FIXME: Add dependencies if this package requires them.
    # depends_on("foo")

    def install(self, spec, prefix):
        # FIXME: Modify the configure line to suit your build system here.
        configure("--prefix=%s" % prefix)
        # cmake(".", *std_cmake_args)

        # FIXME: Add logic to build and install here
        make()
        make("install")
