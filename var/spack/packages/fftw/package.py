# FIXME:
# This is a template package file for Spack.  We've conveniently
# put "FIXME" labels next to all the things you'll want to change.
#
# Once you've edited all the FIXME's, delete this whole message,
# save this file, and test out your package like this:
#
#     spack install fftw
#
# You can always get back here to change things with:
#
#     spack edit fftw
#
# See the spack documentation for more information on building
# packages.
#
from spack import *

class Fftw(Package):
    """FIXME: put a proper description of your package here."""
    # FIXME: add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "http://www.fftw.org/fftw-3.3.4.tar.gz"

    version('3.3.4', '2edab8c06b24feeb3b82bbb3ebf3e7b3')

    # FIXME: Add dependencies if this package requires them.
    # depends_on("foo")

    depends_on('mpi')

    def install(self, spec, prefix):
        # FIXME: Modify the configure line to suit your build system here.
        config_args = ["--prefix=%s" % prefix] #, "CC=mpicc", "CXX=mpicxx", "FC=mpif90"]

	if spec.satisfies("=haswell"):
	  config_args.extend( ["--enable-avx",
	                       "--enable-fma",
			       "--enable-openmp",
			       "--enable-mpi"] )


        configure(*config_args) 
        make()
        make("install")
