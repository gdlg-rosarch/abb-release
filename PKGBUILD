# Script generated with Bloom
pkgdesc="ROS - <p> ROS-Industrial support for the ABB IRB 6640 (and variants). </p> <p> This package contains configuration data, 3D models and launch files for ABB IRB 6640 manipulators. This currently includes the IRB 6640-185/2.8m (6640-185) only. </p> <p> Joint limits and max joint velocities are based on the information in the <a href="http://www.abbrobots.co.uk/en/3HAC028284-en.pdf">ABB IRB 6640 technical data sheet</a> (Version: 3HAC 028284-001 Rev. N). All urdfs / xacros are based on the default motion and joint velocity limits, unless noted otherwise (ie: no support for high speed joints, extended / limited motion ranges or other options). </p> <p> Before using any of the configuration files and / or meshes included in this package, be sure to check they are correct for the particular robot model and configuration you intend to use them with. </p>"
url='http://wiki.ros.org/abb_irb6640_support'

pkgname='ros-kinetic-abb-irb6640-support'
pkgver='1.3.0_2'
pkgrel=1
arch=('any')
license=('Apache2'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-roslaunch>=1.9.55'
)

depends=('ros-kinetic-abb-driver'
'ros-kinetic-joint-state-publisher'
'ros-kinetic-robot-state-publisher'
'ros-kinetic-rviz'
'ros-kinetic-xacro'
)

conflicts=()
replaces=()

_dir=abb_irb6640_support
source=()
md5sums=()

prepare() {
    cp -R $startdir/abb_irb6640_support $srcdir/abb_irb6640_support
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

