# TODO:
# - cleanup

%define		orgname		qtwebkit
Summary:	The Qt5 Webkit
Name:		qt5-%{orgname}
Version:	5.2.0
Release:	0.1
License:	LGPL v2.1 or GPL v3.0
Group:		X11/Libraries
Source0:	http://download.qt-project.org/official_releases/qt/5.2/%{version}/submodules/%{orgname}-opensource-src-%{version}.tar.xz
# Source0-md5:	1378e18aecd8cc223deb729c8f0a735d
URL:		http://qt-project.org/
BuildRequires:	qt5-qtbase-devel = %{version}
BuildRequires:	qt5-qtdeclarative-devel = %{version}
BuildRequires:	qt5-qtsensors-devel = %{version}
BuildRequires:	qt5-qttools-devel = %{version}
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_noautostrip	'.*_debug\\.so*'

%define		specflags	-fno-strict-aliasing
%define		_qtdir		%{_libdir}/qt5

%description
Qt5 Webkit libraries.

%package devel
Summary:	The Qt5 Webkit - development files
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Qt5 Webkit - development files.

%package doc
Summary:	The Qt5 Webkit - docs
Group:		Documentation

%description doc
Qt5 Webkit - documentation.

%package examples
Summary:	Qt5 Webkit examples
Group:		X11/Development/Libraries

%description examples
Qt5 Webkit - examples.

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

# Prepare some files list
ifecho() {
	RESULT=`echo $RPM_BUILD_ROOT$2 2>/dev/null`
	[ "$RESULT" == "" ] && return # XXX this is never true due $RPM_BUILD_ROOT being set
	r=`echo $RESULT | awk '{ print $1 }'`

	if [ -d "$r" ]; then
		echo "%%dir $2" >> $1.files
	elif [ -x "$r" ] ; then
		echo "%%attr(755,root,root) $2" >> $1.files
	elif [ -f "$r" ]; then
		echo "$2" >> $1.files
	else
		echo "Error generation $1 files list!"
		echo "$r: no such file or directory!"
		return 1
	fi
}

echo "%defattr(644,root,root,755)" > examples.files
ifecho examples %{_examplesdir}/qt5
for f in `find $RPM_BUILD_ROOT%{_examplesdir}/qt5 -printf "%%P "`; do
	ifecho examples %{_examplesdir}/qt5/$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%post		-p /sbin/ldconfig
%postun		-p /sbin/ldconfig

%files
%if 0
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQt5Script.so.?
%attr(755,root,root) %{_libdir}/libQt5Script.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5ScriptTools.so.?
%attr(755,root,root) %{_libdir}/libQt5ScriptTools.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Script.so
%attr(755,root,root) %{_libdir}/libQt5ScriptTools.so
%{_libdir}/libQt5Script.la
%{_libdir}/libQt5ScriptTools.la
%{_libdir}/libQt5Script.prl
%{_libdir}/libQt5ScriptTools.prl
%{_libdir}/cmake/Qt5Script
%{_libdir}/cmake/Qt5ScriptTools
%{_includedir}/qt5/QtScript
%{_includedir}/qt5/QtScriptTools
%{_pkgconfigdir}/*.pc
%{_qtdir}/mkspecs
%endif

%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc

%files examples -f examples.files
