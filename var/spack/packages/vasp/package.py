# FIXME:
# This is a template package file for Spack.  We've conveniently
# put "FIXME" labels next to all the things you'll want to change.
#
# Once you've edited all the FIXME's, delete this whole message,
# save this file, and test out your package like this:
#
#     spack install vasp
#
# You can always get back here to change things with:
#
#     spack edit vasp
#
# See the spack documentation for more information on building
# packages.
#
from spack import *

class Vasp(Package):
    """FIXME: put a proper description of your package here."""
    # FIXME: add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "file:///opt/sam/src/vasp/vasp.5.4.1.tar.gz"

    version('5.4.1', '57c2b07d0f70987000033984e913f1a6')

    #patch('patch.5.4.1.08072015')
    #patch('fftw3-makefile')

    # FIXME: Add dependencies if this package requires them.
    depends_on("mpi")
    #provided by mkl
    #depends_on("fftw")

    def install(self, spec, prefix):
      cp = which('cp')
      stage_dir = join_path(ancestor('.',n=1),'vasp.%s' % spec.version)

      if spec.satisfies('%intel'):
        cp( join_path(stage_dir,'arch','makefile.include.linux_intel'),
            join_path(stage_dir,'makefile.include') )

        if spec.satisfies("^mvapich2"):
          filter_file(r'blacs_openmpi','blacs_intelmpi',
            join_path(stage_dir,'makefile.include') )

        filter_file(r'OFLAG      = -O2','OFLAG      = -O2 -xHOST',
          join_path(stage_dir,'makefile.include') )



      make(parallel=False)
      rsync=which('rsync')
      rsync('-a',join_path(stage_dir,'bin'),join_path(prefix))
