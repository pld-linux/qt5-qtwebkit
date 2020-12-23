# NOTE: not splitting WebKit/WebKitWidgets, interdependencies are not clear
# (e.g. WebProcess requires WebKitWidgets)
#
# Conditional build:
%bcond_with	bootstrap	# disable features to able to build without installed qt5
# -- build targets
%bcond_without	doc		# documentation
# -- features
%bcond_with	qtmultimedia	# QtMultimedia support (instead of GStreamer)
%bcond_with	seccomp		# WebProcess seccomp filters (broken as of 5.212.0-alpha4)

%if %{with bootstrap}
%undefine	with_doc
%endif

# it's not possible to build this with debuginfo on 32bit archs due to
# memory constraints during linking
%ifarch %{ix86} x32
%define		_enable_debug_packages		0
%endif

%define		snap	alpha4
%define		rel	1

%define		orgname			qtwebkit
%define		qtbase_ver		5.11
%define		qtdeclarative_ver	5.11
%define		qtlocation_ver		5.11
%define		qtmultimedia_ver	5.11
%define		qtsensors_ver		5.11
%define		qttools_ver		5.11
%define		qtwebchannel_ver	5.11
Summary:	The Qt5 WebKit libraries
Summary(pl.UTF-8):	Biblioteki Qt5 WebKit
Name:		qt5-%{orgname}
Version:	5.212.0
Release:	0.%{snap}.%{rel}
License:	LGPL v2+
Group:		X11/Libraries
#Source0Download: https://github.com/qtwebkit/qtwebkit/releases
Source0:	https://github.com/qtwebkit/qtwebkit/releases/download/qtwebkit-%{version}-%{snap}/qtwebkit-%{version}-%{snap}.tar.xz
# Source0-md5:	5b61a72497f06e51db09d57edc3c35fb
Patch0:		%{name}-css.patch
Patch1:		%{name}-docs.patch
# from FC
Patch102:	qtwebkit-5.212.0_cmake_cmp0071.patch
Patch108:	x32.patch
URL:		https://github.com/annulen/webkit
BuildRequires:	OpenGL-devel
BuildRequires:	Qt5Core-devel >= %{qtbase_ver}
BuildRequires:	Qt5Gui-devel >= %{qtbase_ver}
%{?with_qtmultimedia:BuildRequires:	Qt5MultimediaWidgets-devel >= %{qtmultimedia_ver}}
BuildRequires:	Qt5Network-devel >= %{qtbase_ver}
BuildRequires:	Qt5OpenGL-devel >= %{qtbase_ver}
BuildRequires:	Qt5Positioning-devel >= %{qtlocation_ver}
BuildRequires:	Qt5PrintSupport-devel >= %{qtbase_ver}
BuildRequires:	Qt5Qml-devel >= %{qtdeclarative_ver}
BuildRequires:	Qt5Quick-devel >= %{qtdeclarative_ver}
BuildRequires:	Qt5Sensors-devel >= %{qtsensors_ver}
BuildRequires:	Qt5WebChannel-devel >= %{qtwebchannel_ver}
BuildRequires:	Qt5Widgets-devel >= %{qtbase_ver}
BuildRequires:	bison >= 2.1
BuildRequires:	dwz >= 0.13
BuildRequires:	glib2-devel >= 1:2.36
BuildRequires:	gperf >= 3.0.1
BuildRequires:	gstreamer-devel >= 1.0.3
BuildRequires:	gstreamer-gl-devel >= 1.6.0
BuildRequires:	gstreamer-plugins-bad-devel >= 1.4.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0.3
BuildRequires:	hyphen-devel
BuildRequires:	libicu-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
%{?with_seccomp:BuildRequires:	libseccomp-devel}
BuildRequires:	libwebp-devel
BuildRequires:	libxml2-devel >= 1:2.8.0
BuildRequires:	libxslt-devel >= 1.1.7
BuildRequires:	perl-base >= 1:5.10.0
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.7.0
BuildRequires:	ruby >= 1:1.9
%if %{with doc}
BuildRequires:	qt5-assistant >= %{qttools_ver}
%endif
BuildRequires:	qt5-build >= %{qtbase_ver}
BuildRequires:	qt5-qmake >= %{qtbase_ver}
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	tar >= 1:1.22
BuildRequires:	woff2-devel >= 1.0.1
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing
%define		qt5dir		%{_libdir}/qt5

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains Qt5 WebKit libraries.

%description -l pl.UTF-8
Qt to wieloplatformowy szkielet aplikacji i interfejsów użytkownika.
Przy użyciu Qt można pisać aplikacje powiązane z WWW i wdrażać je w
systemach biurkowych, przenośnych i wbudowanych bez przepisywania kodu
źródłowego.

Ten pakiet zawiera biblioteki Qt5 WebKit.

%package -n Qt5WebKit
Summary:	The Qt5 WebKit libraries
Summary(pl.UTF-8):	Biblioteki Qt5 WebKit
Group:		X11/Libraries
Requires:	Qt5Core >= %{qtbase_ver}
Requires:	Qt5Gui >= %{qtbase_ver}
%{?with_qtmultimedia:Requires:	Qt5MultimediaWidgets >= %{qtmultimedia_ver}}
Requires:	Qt5Network >= %{qtbase_ver}
Requires:	Qt5OpenGL >= %{qtbase_ver}
Requires:	Qt5Positioning >= %{qtlocation_ver}
Requires:	Qt5PrintSupport >= %{qtbase_ver}
Requires:	Qt5Qml >= %{qtdeclarative_ver}
Requires:	Qt5Quick >= %{qtdeclarative_ver}
Requires:	Qt5Sensors >= %{qtsensors_ver}
Requires:	Qt5Sql >= %{qtbase_ver}
Requires:	Qt5Widgets >= %{qtbase_ver}

%description -n Qt5WebKit
Qt5 WebKit libraries provide a web browser engine as well as C++
classes to render and interact with web content.

%description -n Qt5WebKit -l pl.UTF-8
Biblioteki Qt5 WebKit dostarczają silnik przeglądarki WWW, a także
klasy C++ do renderowania i interakcji z treścią WWW.

%package -n Qt5WebKit-devel
Summary:	Qt5 WebKit libraries - development files
Summary(pl.UTF-8):	Biblioteki Qt5 WebKit - pliki programistyczne
Group:		X11/Development/Libraries
Requires:	Qt5Core-devel >= %{qtbase_ver}
Requires:	Qt5Gui-devel >= %{qtbase_ver}
%{?with_qtmultimedia:Requires:	Qt5MultimediaWidgets-devel >= %{qtmultimedia_ver}}
Requires:	Qt5Network-devel >= %{qtbase_ver}
Requires:	Qt5OpenGL-devel >= %{qtbase_ver}
Requires:	Qt5Positioning-devel >= %{qtlocation_ver}
Requires:	Qt5PrintSupport-devel >= %{qtbase_ver}
Requires:	Qt5Quick-devel >= %{qtbase_ver}
Requires:	Qt5Sensors-devel >= %{qtsensors_ver}
Requires:	Qt5WebKit = %{version}-%{release}
Requires:	Qt5Widgets-devel >= %{qtbase_ver}

%description -n Qt5WebKit-devel
Qt5 WebKit libraries - development files.

%description -n Qt5WebKit-devel -l pl.UTF-8
Biblioteki Qt5 WebKit - pliki programistyczne.

%package doc
Summary:	Qt5 WebKit documentation in HTML format
Summary(pl.UTF-8):	Dokumentacja do bibliotek Qt5 WebKit w formacie HTML
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
%{?noarchpackage}

%description doc
Qt5 WebKit documentation in HTML format.

%description doc -l pl.UTF-8
Dokumentacja do bibliotek Qt5 WebKit w formacie HTML.

%package doc-qch
Summary:	Qt5 WebKit documentation in QCH format
Summary(pl.UTF-8):	Dokumentacja do bibliotek Qt5 WebKit w formacie QCH
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
%{?noarchpackage}

%description doc-qch
Qt5 WebKit documentation in QCH format.

%description doc-qch -l pl.UTF-8
Dokumentacja do bibliotek Qt5 WebKit w formacie QCH.

%prep
%setup -q -n qtwebkit-%{version}-%{snap}
%patch0 -p1
%patch1 -p1
%patch102 -p1
%patch108 -p1

%build
mkdir -p build
cd build
CFLAGS="%{rpmcflags}"; export CFLAGS
CXXFLAGS="%{rpmcxxflags} -fpermissive"; export CXXFLAGS
# We cannot use default cmake macro here as it overwrites some settings queried
# by qtwebkit cmake from qmake
cmake \
	-DPORT=Qt \
	-DCMAKE_BUILD_TYPE=Release \
	-DENABLE_NETSCAPE_PLUGIN_API=ON \
	%{?with_seccomp:-DENABLE_SECCOMP_FILTERS=ON} \
	-DENABLE_TOOLS=OFF \
	-DENABLE_X11_TARGET=ON \
	-DCMAKE_C_FLAGS_RELEASE:STRING="-DNDEBUG" \
	-DCMAKE_CXX_FLAGS_RELEASE:STRING="-DNDEBUG" \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
	%{?with_qtmultimedia:-DUSE_GSTREAMER:BOOL=OFF -DUSE_QT_MULTIMEDIA:BOOL=ON} \
	%{?with_doc:-DGENERATE_DOCUMENTATION=ON} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
%if "%{_lib}" == "libx32"
	-DLIB_SUFFIX=x32 \
%endif
%ifarch x32
	-DENABLE_JIT=OFF \
%endif
       ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# normalize paths
%{__sed} -i -e '/^Libs:/ s,-L/[^ ]*,-L%{_libdir},' \
	-e '/^Cflags:/ s,-I[^ ]*/include/qt5,-I%{_includedir}/qt5,' \
	$RPM_BUILD_ROOT%{_pkgconfigdir}/*.pc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n Qt5WebKit -p /sbin/ldconfig
%postun	-n Qt5WebKit -p /sbin/ldconfig

%files -n Qt5WebKit
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5WebKit.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5WebKit.so.5
%attr(755,root,root) %{_libdir}/libQt5WebKitWidgets.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5WebKitWidgets.so.5
%dir %{_libdir}/qt5/qml/QtWebKit
%attr(755,root,root) %{_libdir}/qt5/qml/QtWebKit/libqmlwebkitplugin.so
%{_libdir}/qt5/qml/QtWebKit/plugins.qmltypes
%{_libdir}/qt5/qml/QtWebKit/qmldir
%dir %{_libdir}/qt5/qml/QtWebKit/experimental
%attr(755,root,root) %{_libdir}/qt5/qml/QtWebKit/experimental/libqmlwebkitexperimentalplugin.so
%{_libdir}/qt5/qml/QtWebKit/experimental/qmldir
%attr(755,root,root) %{_libdir}/qt5/libexec/QtWebProcess
%attr(755,root,root) %{_libdir}/qt5/libexec/QtWebNetworkProcess
%attr(755,root,root) %{_libdir}/qt5/libexec/QtWebPluginProcess
%attr(755,root,root) %{_libdir}/qt5/libexec/QtWebStorageProcess

%files -n Qt5WebKit-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5WebKit.so
%attr(755,root,root) %{_libdir}/libQt5WebKitWidgets.so
%{_includedir}/qt5/QtWebKit
%{_includedir}/qt5/QtWebKitWidgets
%{_pkgconfigdir}/Qt5WebKit.pc
%{_pkgconfigdir}/Qt5WebKitWidgets.pc
%{_libdir}/cmake/Qt5WebKit
%{_libdir}/cmake/Qt5WebKitWidgets
%{qt5dir}/mkspecs/modules/qt_lib_webkit.pri
%{qt5dir}/mkspecs/modules/qt_lib_webkit_private.pri
%{qt5dir}/mkspecs/modules/qt_lib_webkitwidgets.pri
%{qt5dir}/mkspecs/modules/qt_lib_webkitwidgets_private.pri

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtwebkit

%files doc-qch
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtwebkit.qch
%endif
