# TODO:
# - package /usr/lib/qt5/libexec correctly
# - cleanup
#
# Conditional build:
%bcond_without	qch	# documentation in QCH format

%define		orgname		qtwebkit
%define		qtbase_ver	%{version}
%define		qtquick_ver	%{version}
%define		qttools_ver	%{version}
Summary:	The Qt5 WebKit libraries
Summary(pl.UTF-8):	Biblioteki Qt5 WebKit
Name:		qt5-%{orgname}
Version:	5.3.0
Release:	0.2
License:	LGPL v2.1 or GPL v3.0
Group:		X11/Libraries
Source0:	http://download.qt-project.org/official_releases/qt/5.3/%{version}/submodules/%{orgname}-opensource-src-%{version}.tar.xz
# Source0-md5:	cc9197eaef9e7950e907635f9bde1e98
URL:		http://qt-project.org/
BuildRequires:	Qt5Core-devel = %{qtbase_ver}
BuildRequires:	Qt5Quick-devel = %{qtquick_ver}
BuildRequires:	rpmbuild(macros) >= 1.654
%if %{with qch}
BuildRequires:	qt5-assistant >= %{qttools_ver}
%endif
BuildRequires:	qt5-build >= %{qtbase_ver}
BuildRequires:	qt5-qmake >= %{qtbase_ver}
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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

%description -n Qt5WebKit
Qt5 WebKit libraries ... TODO.

%description -n Qt5WebKit -l pl.UTF-8
Biblioteki Qt5 WebKit ... TODO

%package -n Qt5WebKit-devel
Summary:	Qt5 WebKit libraries - development files
Summary(pl.UTF-8):	Biblioteki Qt5 WebKit - pliki programistyczne
Group:		X11/Development/Libraries
Requires:	Qt5WebKit = %{version}-%{release}

%description -n Qt5WebKit-devel
Qt5 WebKit libraries - development files.

%description -n Qt5WebKit-devel -l pl.UTF-8
Biblioteki Qt5 WebKit - pliki programistyczne.

%package doc
Summary:	Qt5 WebKit documentation in HTML format
Summary(pl.UTF-8):	Dokumentacja do bibliotek Qt5 WebKit w formacie HTML
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc
Qt5 WebKit documentation in HTML format.

%description doc -l pl.UTF-8
Dokumentacja do bibliotek Qt5 WebKit w formacie HTML.

%package doc-qch
Summary:	Qt5 WebKit documentation in QCH format
Summary(pl.UTF-8):	Dokumentacja do bibliotek Qt5 WebKit w formacie QCH
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-qch
Qt5 WebKit documentation in QCH format.

%description doc-qch -l pl.UTF-8
Dokumentacja do bibliotek Qt5 WebKit w formacie QCH.

%prep
%setup -q -n %{orgname}-opensource-src-%{version}

%build
qmake-qt5
%{__make}
%{__make} %{!?with_qch:html_}docs

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__make} install_%{!?with_qch:html_}docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT

# useless symlinks
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.so.5.?
# actually drop *.la, follow policy of not packaging them when *.pc exist
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.la

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
%{_libdir}/qt5/qml/QtWebKit/qmldir
%dir %{_libdir}/qt5/qml/QtWebKit/experimental
%attr(755,root,root) %{_libdir}/qt5/qml/QtWebKit/experimental/libqmlwebkitexperimentalplugin.so
%{_libdir}/qt5/qml/QtWebKit/experimental/qmldir
%attr(755,root,root) %{_libdir}/qt5/libexec

%files -n Qt5WebKit-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5WebKit.so
%attr(755,root,root) %{_libdir}/libQt5WebKitWidgets.so
%{_libdir}/libQt5WebKit.prl
%{_libdir}/libQt5WebKitWidgets.prl
%{_includedir}/qt5/QtWebKit
%{_includedir}/qt5/QtWebKitWidgets
%{_pkgconfigdir}/Qt5WebKit.pc
%{_pkgconfigdir}/Qt5WebKitWidgets.pc
%{_libdir}/cmake/Qt5WebKit
%{_libdir}/cmake/Qt5WebKitWidgets
%{qt5dir}/mkspecs/modules/*.pri

%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qt*[!h]

%if %{with qch}
%files doc-qch
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/*.qch
%endif
