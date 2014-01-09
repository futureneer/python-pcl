from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(name='python-pcl',
      description='pcl wrapper',
      url='http://github.com/strawlab/python-pcl',
      version='0.1',
      author='John Stowers',
      author_email='john.stowers@gmail.com',
      license='BSD',
      ext_modules=[Extension(
                   "pcl",
                   ["pcl.pyx", "minipcl.cpp"],
                    include_dirs=["/usr/local/include/pcl-1.7", "/usr/include/eigen3/"],
                    libraries=["pcl_segmentation", "pcl_io", "OpenNI",
                               "usb-1.0", "pcl_filters", "pcl_sample_consensus",
                               "pcl_features", "pcl_surface", "pcl_search", "pcl_kdtree", "pcl_octree",
                               "flann_cpp", "pcl_common"],
                    define_macros=[("EIGEN_YES_I_KNOW_SPARSE_MODULE_IS_NOT_STABLE_YET", "1")],
                    language="c++")],
      cmdclass={'build_ext': build_ext}
)


