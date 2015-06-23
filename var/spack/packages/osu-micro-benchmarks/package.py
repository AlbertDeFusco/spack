# FIXME:
# This is a template package file for Spack.  We've conveniently
# put "FIXME" labels next to all the things you'll want to change.
#
# Once you've edited all the FIXME's, delete this whole message,
# save this file, and test out your package like this:
#
#     spack install osu-micro-benchmarks
#
# You can always get back here to change things with:
#
#     spack edit osu-micro-benchmarks
#
# See the spack documentation for more information on building
# packages.
#
from spack import *

class OsuMicroBenchmarks(Package):
    """FIXME: put a proper description of your package here."""
    # FIXME: add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "http://mvapich.cse.ohio-state.edu/download/mvapich/osu-micro-benchmarks-4.4.1.tar.gz"

    version('4.4.1', '67bfdb2e923fe01afe5f4f8bf06f8b2a')

    # FIXME: Add dependencies if this package requires them.
    depends_on("mpi")

    def install(self, spec, prefix):
        # FIXME: Modify the configure line to suit your build system here.
        config_args=["--prefix=%s" % prefix ,
                     "--exec-prefix=%s" % prefix,
                     "CC=mpicc"]

        configure(*config_args)

        # FIXME: Add logic to build and install here
        make()
        make("install")
