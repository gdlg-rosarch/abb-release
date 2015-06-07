Name:           ros-indigo-abb-irb2400-moveit-config
Version:        1.2.0
Release:        0%{?dist}
Summary:        ROS abb_irb2400_moveit_config package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/abb_irb2400_moveit_config
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-abb-irb2400-moveit-plugins
Requires:       ros-indigo-abb-irb2400-support
Requires:       ros-indigo-industrial-robot-simulator
Requires:       ros-indigo-joint-state-publisher
Requires:       ros-indigo-moveit-planners-ompl
Requires:       ros-indigo-moveit-ros-move-group
Requires:       ros-indigo-moveit-ros-visualization
Requires:       ros-indigo-moveit-simple-controller-manager
Requires:       ros-indigo-robot-state-publisher
Requires:       ros-indigo-xacro
BuildRequires:  ros-indigo-catkin

%description
MoveIt package for the ABB IRB 2400. An automatically generated package with
all the configuration and launch files for using the ABB IRB 2400 with the
MoveIt Motion Planning Framework.

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
* Sat Jun 06 2015 Shaun Edwards (Southwest Research Institute) <sedwards@swri.org> - 1.2.0-0
- Autogenerated by Bloom

* Tue Apr 07 2015 Shaun Edwards (Southwest Research Institute) <sedwards@swri.org> - 1.1.9-0
- Autogenerated by Bloom

