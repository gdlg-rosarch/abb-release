# Script generated with Bloom
pkgdesc="ROS - ROS-Industrial support for ABB manipulators (metapackage)."
url='http://ros.org/wiki/abb'

pkgname='ros-kinetic-abb'
pkgver='1.3.0_2'
pkgrel=1
arch=('any')
license=('BSD'
'Apache 2.0'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-abb-driver'
'ros-kinetic-abb-irb2400-moveit-config'
'ros-kinetic-abb-irb2400-moveit-plugins'
'ros-kinetic-abb-irb2400-support'
'ros-kinetic-abb-irb4400-support'
'ros-kinetic-abb-irb5400-support'
'ros-kinetic-abb-irb6600-support'
'ros-kinetic-abb-irb6640-moveit-config'
'ros-kinetic-abb-irb6640-support'
'ros-kinetic-abb-resources'
)

conflicts=()
replaces=()

_dir=abb
source=()
md5sums=()

prepare() {
    cp -R $startdir/abb $srcdir/abb
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

