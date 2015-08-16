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
import spack

class Cp2k(Package):
    """FIXME: put a proper description of your package here."""
    # FIXME: add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "http://downloads.sourceforge.net/project/cp2k/cp2k-2.6.1.tar.bz2"

    version('2.6.1', 'bbeb19e7d5f1e2d29b3efa966ce00c45')

    version('2.6.x', svn='http://svn.code.sf.net/p/cp2k/code/branches/cp2k-2_6-branch')

    #patch('data_dir.patch')
    #patch('path_length.patch')

    # FIXME: Add dependencies if this package requires them.
    depends_on("mpi")
    depends_on("fftw")
    depends_on("libxc")
    depends_on("libint")

    def install(self, spec, prefix):
      if spec.satisfies("@2.6.x"):
        stageDir=join_path(self._stage.path,'cp2k-2_6-branch','cp2k')
      else:
        stageDir=join_path(self._stage.path,'cp2k-2.6.1')

      #get the site-specific Makefile
      pkg_dir = spack.db.dirname_for_package_name('cp2k')
      if spec.satisfies("=haswell"):
        arch='SaM'
        cp = which('cp')
        for file in ['SaM.popt','SaM.psmp']:
          makeFile=join_path(pkg_dir,file)
          cp(makeFile,join_path(stageDir,'arch'))

      for file in ['SaM.popt','SaM.psmp']:
        archMake=join_path(stageDir,'arch',file)
        dataDir=join_path(prefix,'data')
        filter_file(r'<data-dir>',dataDir,archMake)

      cp_filesF=join_path(stageDir,'src','common','cp_files.F')
      filter_file(r'<data-dir>',dataDir,cp_filesF)


      if spec.satisfies("^libxc@2.2"):
        for file in ['SaM.popt','SaM.psmp']:
          archMake=join_path(stageDir,'arch',file)
          filter_file(r'-lxc','-lxcf90 -lxc',archMake)

      if spec.satisfies("^mvapich2"):
        for file in ['SaM.popt','SaM.psmp']:
          archMake=join_path(stageDir,'arch',file)
          filter_file(r'blacs_openmpi','blacs_intelmpi',archMake)
          #filter_file(r'mpif90','mpif77',archMake)
 


      with working_dir(join_path(stageDir,'makefiles')):
        stage_dir = ancestor('.',n=1)
        for vers in ['popt','psmp']:
          make('cp2k','CP2KHOME=%s' % stage_dir,
            'ARCH=SaM','VERSION=%s' % vers)

      exe_dir=join_path(stageDir,'exe','SaM')
      mkdirp(join_path(prefix.bin))
      for vers in ['popt','psmp']:
        install( join_path(exe_dir,'cp2k.%s' % vers),join_path(prefix.bin))

      rsync=which('rsync')
      rsync('-a',join_path(stageDir,'data'),join_path(prefix))
