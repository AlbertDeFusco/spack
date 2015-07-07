from spack import *

class Hdf5(Package):
    """HDF5 is a data model, library, and file format for storing and managing
       data. It supports an unlimited variety of datatypes, and is designed for
       flexible and efficient I/O and for high volume and complex data.
    """

    homepage = "http://www.hdfgroup.org/HDF5/"
    url      = "http://www.hdfgroup.org/ftp/HDF5/releases/hdf5-1.8.13/src/hdf5-1.8.13.tar.gz"
    list_url = "http://www.hdfgroup.org/ftp/HDF5/releases"
    list_depth = 3

    version('1.8.13', 'c03426e9e77d7766944654280b467289')
    version('1.8.15', '03cccb5b33dbe975fdcd8ae9dc021f24')
    version('1.8.15-patch1', '4467c25ed9c0b126b194a4d9d66c29ac')

    depends_on("mpi")
    depends_on("zlib")

    # TODO: currently hard-coded to use OpenMPI
    def install(self, spec, prefix):

        conf_args= [
            "--prefix=%s" % prefix,
            "--with-zlib=%s" % spec['zlib'].prefix,
            "--enable-parallel",
            "--enable-shared",
            "CC=mpicc", "CXX=mpicxx"]
            #"CC=%s" % spec['mpich'].prefix.bin + "/mpicc",
            #"CXX=%s" % spec['mpich'].prefix.bin + "/mpic++")

        if spec.satisfies('%intel'):
          conf_args.extend( [ "CFLAGS=-xHOST",
                              "CXXFLAGS=-xHOST",
                              "FCFLAGS=-xHOST" ] )

        configure(*conf_args)
        make()
        make("install")

    def url_for_version(self, version):
        v = str(version)

        if version == Version("1.2.2"):
            return "http://www.hdfgroup.org/ftp/HDF5/releases/hdf5-" + v + ".tar.gz"
        elif version < Version("1.7"):
            return "http://www.hdfgroup.org/ftp/HDF5/releases/hdf5-" + version.up_to(2) + "/hdf5-" + v + ".tar.gz"
        else:
            return "http://www.hdfgroup.org/ftp/HDF5/releases/hdf5-" + v + "/src/hdf5-" + v + ".tar.gz"
