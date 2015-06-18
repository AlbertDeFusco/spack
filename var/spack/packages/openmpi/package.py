from spack import *
import os

class Openmpi(Package):
    """Open MPI is a project combining technologies and resources from
       several other projects (FT-MPI, LA-MPI, LAM/MPI, and PACX-MPI)
       in order to build the best MPI library available. A completely
       new MPI-2 compliant implementation, Open MPI offers advantages
       for system and software vendors, application developers and
       computer science researchers.
    """

    homepage = "http://www.open-mpi.org"

    version('1.8.2', 'ab538ed8e328079d566fc797792e016e',
            url='http://www.open-mpi.org/software/ompi/v1.8/downloads/openmpi-1.8.2.tar.gz')
    version('1.8.6', 'f4d747d39ac2b8cdd8be6d847cd9228d',
	url='http://www.open-mpi.org/software/ompi/v1.8/downloads/openmpi-1.8.6.tar.gz')
    version('1.6.5', '03aed2a4aa4d0b27196962a2a65fc475',
            url = "http://www.open-mpi.org/software/ompi/v1.6/downloads/openmpi-1.6.5.tar.bz2")

    patch('ad_lustre_rwcontig_open_source.patch', when="@1.6.5")
    patch('llnl-platforms.patch', when="@1.6.5")

    provides('mpi@:2')

    def install(self, spec, prefix):
        config_args = ["--prefix=%s" % prefix]

        # TODO: use variants for this, e.g. +lanl, +llnl, etc.
        # use this for LANL builds, but for LLNL builds, we need:
        #     "--with-platform=contrib/platform/llnl/optimized"
        if self.version == ver("1.6.5") and '+lanl' in spec:
            config_args.append("--with-platform=contrib/platform/lanl/tlcc2/optimized-nopanasas")

        # TODO: Spack should make it so that you can't actually find
        # these compilers if they're "disabled" for the current
        # compiler configuration.
        if not self.compiler.f77 and not self.compiler.fc:
            config_args.append("--enable-mpi-fortran=no")

	if spec.architecture == "haswell":
	  config_args.extend([ "--with-slurm",
	                       "--enable-mpi-fortran",
			       "--with-openib"
			       ])


        configure(*config_args)
        make()
        make("install")

        self.filter_compilers()

    def filter_compilers(self):
        """Run after install to make the MPI compilers use the
           compilers that Spack built the package with.
           If this isn't done, they'll have CC, CXX, F77, and FC set
           to Spack's generic cc, c++, f77, and f90.  We want them to
           be bound to whatever compiler they were built with.
        """
        bin = self.prefix.bin
        mpicc  = os.path.join(bin, 'mpicc')
        mpicxx = os.path.join(bin, 'mpicxx')
        mpif77 = os.path.join(bin, 'mpif77')
        mpif90 = os.path.join(bin, 'mpif90')

        kwargs = { 'ignore_absent' : True, 'backup' : False, 'string' : True }
        filter_file('CC="cc"',   'CC="%s"'  % self.compiler.cc,  mpicc,  **kwargs)
        filter_file('CXX="c++"', 'CXX="%s"' % self.compiler.cxx, mpicxx, **kwargs)
        filter_file('F77="f77"', 'F77="%s"' % self.compiler.f77, mpif77, **kwargs)
        filter_file('FC="f90"',  'FC="%s"'  % self.compiler.fc,  mpif90, **kwargs)

    def setup_dependent_environment(self, module, spec, dep_spec):
        """For dependencies, make mpicc's use spack wrapper."""
        os.environ['MPICH_CC']  = 'cc'
        os.environ['MPICH_CXX'] = 'c++'
        os.environ['MPICH_F77'] = 'f77'
        os.environ['MPICH_F90'] = 'f90'
