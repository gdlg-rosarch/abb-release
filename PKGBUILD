# Script generated with Bloom
pkgdesc="ROS - <p> MoveIt package for the ABB IRB 2400. </p> <p> An automatically generated package with all the configuration and launch files for using the ABB IRB 2400 with the MoveIt Motion Planning Framework. </p>"
url='http://ros.org/wiki/abb_irb2400_moveit_config'

pkgname='ros-kinetic-abb-irb2400-moveit-config'
pkgver='1.3.0_2'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-abb-irb2400-moveit-plugins'
'ros-kinetic-abb-irb2400-support'
'ros-kinetic-industrial-robot-simulator'
'ros-kinetic-joint-state-publisher'
'ros-kinetic-moveit-planners-ompl'
'ros-kinetic-moveit-ros-move-group'
'ros-kinetic-moveit-ros-visualization'
'ros-kinetic-moveit-simple-controller-manager'
'ros-kinetic-robot-state-publisher'
'ros-kinetic-xacro'
)

conflicts=()
replaces=()

_dir=abb_irb2400_moveit_config
source=()
md5sums=()

prepare() {
    cp -R $startdir/abb_irb2400_moveit_config $srcdir/abb_irb2400_moveit_config
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

