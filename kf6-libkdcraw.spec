%define libname %mklibname KF6Dcraw
%define devname %mklibname KF6Dcraw -d
%define git 20231103

Name: kf6-libkdcraw
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/graphics/libkdcraw/-/archive/master/libkdcraw-master.tar.bz2#/libkdcraw-%{git}.tar.bz2
Summary: Library for handling RAW images
URL: https://invent.kde.org/graphics/libkdcraw
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(PlasmaWaylandProtocols)
BuildRequires: cmake(Qt6WaylandClient)
BuildRequires: pkgconfig(libraw)
BuildRequires: pkgconfig(libraw_r)
Requires: %{libname} = %{EVRD}

%description
Library for handling RAW images

%package -n %{libname}
Summary: Library for handling RAW images
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Library for handling RAW images

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Library for handling RAW images

%prep
%autosetup -p1 -n libkdcraw-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_datadir}/qlogging-categories6/libkdcraw.categories

%files -n %{devname}
%{_includedir}/KF6/KDCRAW
%{_libdir}/cmake/KF6KDcraw

%files -n %{libname}
%{_libdir}/libKF6KDcraw.so*
