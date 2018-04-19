# Script generated with Bloom
pkgdesc="ROS - <p> MoveIt plugins for the ABB 2400 (and variants). </p> <p> This package contains plugins for use with MoveIt and ABB 2400 manipulators. Plugins included support the 2400. See the ABB 2400 support package for information on used joint angle and velocity limits. </p> <p> Before using any of the plugins included in this package, be sure to check they are correct for the particular robot model and configuration you intend to use them with. </p>"
url='http://ros.org/wiki/abb_irb2400_moveit_plugins'

pkgname='ros-kinetic-abb-irb2400-moveit-plugins'
pkgver='1.3.0_2'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('lapack'
'ros-kinetic-catkin'
'ros-kinetic-moveit-core'
'ros-kinetic-pluginlib'
'ros-kinetic-roscpp'
'ros-kinetic-tf-conversions'
)

depends=('lapack'
'ros-kinetic-moveit-core'
'ros-kinetic-pluginlib'
'ros-kinetic-roscpp'
'ros-kinetic-tf-conversions'
)

conflicts=()
replaces=()

_dir=abb_irb2400_moveit_plugins
source=()
md5sums=()

prepare() {
    cp -R $startdir/abb_irb2400_moveit_plugins $srcdir/abb_irb2400_moveit_plugins
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

