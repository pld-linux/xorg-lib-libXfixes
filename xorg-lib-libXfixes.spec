Summary:	X Fixes extension library
Summary(pl):	Biblioteka rozszerzenia X Fixes
Name:		xorg-lib-libXfixes
Version:	4.0.1
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXfixes-%{version}.tar.bz2
# Source0-md5:	c20eba4be3e8379fd774e999b65d3f90
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-proto-fixesproto-devel >= 3.0
BuildRequires:	xorg-util-util-macros >= 0.99.2
Obsoletes:	libXfixes
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Fixes extension library.

%description -l pl
Biblioteka rozszerzenia X Fixes.

%package devel
Summary:	Header files for libXfixes library
Summary(pl):	Pliki nag³ówkowe biblioteki libXfixes
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel
Requires:	xorg-proto-fixesproto-devel >= 3.0
Obsoletes:	libXfixes-devel

%description devel
X Fixes extension library.

This package contains the header files needed to develop programs that
use libXfixes.

%description devel -l pl
Biblioteka rozszerzenia X Fixes.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXfixes.

%package static
Summary:	Static libXfixes library
Summary(pl):	Biblioteka statyczna libXfixes
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXfixes-static

%description static
X Fixes extension library.

This package contains the static libXfixes library.

%description static -l pl
Biblioteka rozszerzenia X Fixes.

Pakiet zawiera statyczn± bibliotekê libXfixes.

%prep
%setup -q -n libXfixes-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libXfixes.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXfixes.so
%{_libdir}/libXfixes.la
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xfixes.pc
%{_mandir}/man3/*.3x*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXfixes.a
