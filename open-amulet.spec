Summary:	A portable OpenGL GUI library for highly interactive applications
Summary(pl):	Przeno¶na biblioteka GUI OpenGL do interaktywnych aplikacji
Name:		open-amulet
Version:	4.3
Release:	2
License:	GPL
Group:		X11/Libraries
Source0:	http://www.openip.org/oa/%{name}-%{version}.tar.gz
# Source0-md5:	ecf887082f92085488add2b2d10cdb37
Patch0:		%{name}-DESTDIR_fix.patch
URL:		http://www.openip.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
A portable GUI library for highly interactive applications, with
OpenGL support etc.

%description -l pl
Przeno¶na biblioteka GUI do wysoko interaktywnych aplikacji, z obs³ug±
OpenGL itp.

%package devel
Summary:	Open Amulet development package
Summary(pl):	Pakiet dla programistów u¿ywaj±cych Open Amulet
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Open Amulet development package.

%description devel -l pl
Pakiet dla programistów u¿ywaj±cych Open Amulet.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--with-x
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	macrosdir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libamulet*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc readme.txt
%{_includedir}/*
%attr(755,root,root) %{_libdir}/libamulet*.so
%{_libdir}/libamulet*.la
%{_aclocaldir}/acamulet.m4
%dir %{_datadir}/open-amulet
