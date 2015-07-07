# FIXME:
# This is a template package file for Spack.  We've conveniently
# put "FIXME" labels next to all the things you'll want to change.
#
# Once you've edited all the FIXME's, delete this whole message,
# save this file, and test out your package like this:
#
#     spack install vcftools
#
# You can always get back here to change things with:
#
#     spack edit vcftools
#
# See the spack documentation for more information on building
# packages.
#
from spack import *

class Vcftools(Package):
    """FIXME: put a proper description of your package here."""
    # FIXME: add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "http://downloads.sourceforge.net/project/vcftools/vcftools_0.1.12b.tar.gz"

    version('0.1.12b', '662758d1139c138cf5a0239ed99f12c2')

    # FIXME: Add dependencies if this package requires them.
    # depends_on("foo")

    def install(self, spec, prefix):
        # FIXME: Modify the configure line to suit your build system here.
        #configure("--prefix=%s" % prefix)
        # cmake(".", *std_cmake_args)

        # FIXME: Add logic to build and install here
        
        #cppMake=join_path(self._stage.path,'vcftools','cpp','Makefile')
        #filter_file(r'CC =','CC = cc',cppMake)
        #filter_file(r'CXX =','CC = cxx',cppMake)
        make('CC=cc', 'CPP=c++', 'PREFIX=%s' % prefix)
        make("install")
