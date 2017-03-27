Name:           ros-indigo-abb-irb2400-moveit-plugins
Version:        1.2.1
Release:        0%{?dist}
Summary:        ROS abb_irb2400_moveit_plugins package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/abb_irb2400_moveit_plugins
Source0:        %{name}-%{version}.tar.gz

Requires:       lapack-devel
Requires:       ros-indigo-moveit-core
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-tf-conversions
BuildRequires:  lapack-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-moveit-core
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-tf-conversions

%description
MoveIt plugins for the ABB 2400 (and variants). This package contains plugins
for use with MoveIt and ABB 2400 manipulators. Plugins included support the
2400. See the ABB 2400 support package for information on used joint angle and
velocity limits. Before using any of the plugins included in this package, be
sure to check they are correct for the particular robot model and configuration
you intend to use them with.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Mar 27 2017 Shaun Edwards (Southwest Research Institute) <sedwards@swri.org> - 1.2.1-0
- Autogenerated by Bloom

* Sat Jun 06 2015 Shaun Edwards (Southwest Research Institute) <sedwards@swri.org> - 1.2.0-0
- Autogenerated by Bloom

* Tue Apr 07 2015 Shaun Edwards (Southwest Research Institute) <sedwards@swri.org> - 1.1.9-0
- Autogenerated by Bloom

