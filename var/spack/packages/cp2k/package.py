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

    #patch('makefile.patch')

    # FIXME: Add dependencies if this package requires them.
    depends_on("mpi")
    depends_on("fftw")
    depends_on("libxc")
    depends_on("libint")

    def install(self, spec, prefix):
      #get the site-specific Makefile
      pkg_dir = spack.db.dirname_for_package_name('cp2k')
      if spec.satisfies("=haswell"):
        arch='SaM'
        makeFile=join_path(pkg_dir,'SaM.popt')
        cp = which('cp')
        cp(makeFile,join_path(self._stage.path,'cp2k-2.6.1','arch'))


      with working_dir('makefiles'):
        stage_dir = ancestor('.',n=1)
        make('CP2KHOME=%s' % stage_dir,
          'ARCH=SaM','VERSION=popt')
