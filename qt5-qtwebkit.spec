# TODO:
# - package /usr/lib/qt5/libexec correctly
# - qch
# - cleanup

%define		orgname		qtwebkit
Summary:	The Qt5 WebKit
Name:		qt5-%{orgname}
Version:	5.3.0
Release:	0.2
License:	LGPL v2.1 or GPL v3.0
Group:		X11/Libraries
Source0:	http://download.qt-project.org/official_releases/qt/5.3/%{version}/submodules/%{orgname}-opensource-src-%{version}.tar.xz
# Source0-md5:	cc9197eaef9e7950e907635f9bde1e98
URL:		http://qt-project.org/
BuildRequires:	Qt5Core-devel = %{version}
BuildRequires:	Qt5Quick-devel = %{version}
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRequires:	qt5-build
BuildRequires:	qt5-qmake
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_noautostrip	'.*_debug\\.so*'

%define		specflags	-fno-strict-aliasing
%define		_qtdir		%{_libdir}/qt5

%description
Qt5 Webkit libraries.

%package -n Qt5WebKit
Summary:	The Qt5WebKit library
Group:		X11/Libraries

%description -n Qt5WebKit
Qt5 Webkit libraries.

%package -n Qt5WebKit-devel
Summary:	The Qt5 WebKit - development files
Group:		X11/Development/Libraries
Requires:	Qt5WebKit = %{version}-%{release}

%description -n Qt5WebKit-devel
Qt5 Webkit - development files.

%package doc
Summary:	The Qt5 Webkit - docs
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc
Qt5 Webkit - documentation.

%prep
%setup -q -n %{orgname}-opensource-src-%{version}

%build
qmake-qt5
%{__make}
%{__make} docs

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__make} install_docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -n Qt5WebKit	-p /sbin/ldconfig
%postun -n Qt5WebKit	-p /sbin/ldconfig

%files -n Qt5WebKit
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQt5WebKit.so.5
%attr(755,root,root) %{_libdir}/libQt5WebKit.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5WebKitWidgets.so.5
%attr(755,root,root) %{_libdir}/libQt5WebKitWidgets.so.*.*
%dir %{_libdir}/qt5/qml/QtWebKit
%attr(755,root,root) %{_libdir}/qt5/qml/QtWebKit/libqmlwebkitplugin.so
%{_libdir}/qt5/qml/QtWebKit/qmldir
%dir %{_libdir}/qt5/qml/QtWebKit/experimental
%attr(755,root,root) %{_libdir}/qt5/qml/QtWebKit/experimental/libqmlwebkitexperimentalplugin.so
%{_libdir}/qt5/qml/QtWebKit/experimental/qmldir
%attr(755,root,root) %{_libdir}/qt5/libexec

%files -n Qt5WebKit-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5WebKit.so
%attr(755,root,root) %{_libdir}/libQt5WebKitWidgets.so
%{_libdir}/libQt5WebKit.la
%{_libdir}/libQt5WebKitWidgets.la
%{_libdir}/libQt5WebKit.prl
%{_libdir}/libQt5WebKitWidgets.prl
%{_libdir}/cmake/Qt5WebKit
%{_libdir}/cmake/Qt5WebKitWidgets
%{_includedir}/qt5/QtWebKit
%{_includedir}/qt5/QtWebKitWidgets
%{_pkgconfigdir}/Qt5WebKit.pc
%{_pkgconfigdir}/Qt5WebKitWidgets.pc
%{_qtdir}/mkspecs

%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc
