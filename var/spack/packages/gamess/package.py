# FIXME:
# This is a template package file for Spack.  We've conveniently
# put "FIXME" labels next to all the things you'll want to change.
#
# Once you've edited all the FIXME's, delete this whole message,
# save this file, and test out your package like this:
#
#     spack install gamess
#
# You can always get back here to change things with:
#
#     spack edit gamess
#
# See the spack documentation for more information on building
# packages.
#
from spack import *

class Gamess(Package):
    """FIXME: put a proper description of your package here."""
    # FIXME: add a proper url for your package's homepage here.
    homepage = "http://www.example.com"

    version('2014-12-05-R1', git='/opt/sam/src/gamess',
      brach='cmake' )

    depends_on('mpi')


    def install(self, spec, prefix):
        # FIXME: Modify the configure line to suit your build system here.
      with working_dir("build",create=True):
        cmake_args = [ "..", "-DCMAKE_C_FLAGS=-xHOST", "-DCMAKE_Fortran_FLAGS=-xHOST", 
           '-DQMNUC=ON', '-DTinker=ON' ]

        if spec.satisfies("%intel"):
          cmake_args.append("-DBLAS_LIBRARIES=/opt/sam/intel/composer_xe_2015.3.187/mkl/lib/intel64/libmkl_intel_ilp64.so;libmkl_core.so;libmkl_sequential.so")
        if spec.satisfies("=haswell"):
          cmake_args.append("-DMPIEXEC=/usr/bin/srun")

        cmake_args.extend(std_cmake_args)
        cmake( *cmake_args )

        # FIXME: Add logic to build and install here
        make()
        make("install")
