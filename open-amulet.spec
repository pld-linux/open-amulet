Summary:	Open Amulet
Summary(pl):	Open Amulet
Name:		open-amulet
Version:	4.3
Release:	1
Copyright:	GPL
Group:		Libraries	
Group(pl):	Biblioteki
Source:		http://www.openip.org/oa/%name-%version.tar.gz
#Patch:
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr/X11R6

%description

%description -l pl

# optional package =====================
%package devel
Summary:	OA devel
Summary(pl):	OA devel
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki

%description devel
%description -l pl devel

# end of optional package ==============

%prep
%setup -q

%build
./autogen.sh
./configure --prefix=%{_prefix} \
	--with-x
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc
%attr(755,root,root) %{_libdir}/libamulet*

# optional package

%files devel
%defattr(644, root, root, 755)
%doc
%attr(644,root,root) %{_includedir}/am_*
%attr(644,root,root) %{_includedir}/amulet.h
%attr(644,root,root) %{_includedir}/oa_dl_import.h
%attr(644,root,root) %{_includedir}/amulet/*.h*
%attr(644,root,root) %{_includedir}/amulet/impl/*
%attr(755,root,root) %{_libdir}/libamulet*.la
%attr(644,root,root) %{_datadir}/aclocal/acamulet.m4
%dir	%{_datadir}/open-amulet

#end of optional package

%changelog
* Wed Oct 17 1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
- build RPM.
