Summary:	A portable OpenGL GUI library for highly interactive applications
Name:		open-amulet
Version:	4.3
Release:	1
License:	GPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(pl):	X11/Biblioteki
Source0:	http://www.openip.org/oa/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
A portable GUI library for highly interactive applications, with
OpenGL support etc.

%package devel
Summary:	OA devel
Summary(pl):	OA devel
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
OA devel.

%prep
%setup -q

%build
%configure \
	--with-x
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	macrosdir=%{_aclocaldir}

gzip -9nf readme.txt

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libamulet*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%{_includedir}/*
%attr(755,root,root) %{_libdir}/libamulet*.so
%attr(755,root,root) %{_libdir}/libamulet*.la
%{_aclocaldir}/acamulet.m4
%dir %{_datadir}/open-amulet
