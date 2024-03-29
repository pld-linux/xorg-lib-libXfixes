Summary:	X Fixes extension library
Summary(pl.UTF-8):	Biblioteka rozszerzenia X Fixes
Name:		xorg-lib-libXfixes
Version:	6.0.1
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libXfixes-%{version}.tar.xz
# Source0-md5:	65b9ba1e9ff3d16c4fa72915d4bb585a
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel >= 1.6
BuildRequires:	xorg-proto-fixesproto-devel >= 6.0
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.22
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Requires:	xorg-lib-libX11 >= 1.6
Obsoletes:	libXfixes < 3.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Fixes extension library.

%description -l pl.UTF-8
Biblioteka rozszerzenia X Fixes.

%package devel
Summary:	Header files for libXfixes library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXfixes
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel >= 1.6
Requires:	xorg-proto-fixesproto-devel >= 6.0
Requires:	xorg-proto-xproto-devel >= 7.0.22
Obsoletes:	libXfixes-devel < 3.0.0

%description devel
X Fixes extension library.

This package contains the header files needed to develop programs that
use libXfixes.

%description devel -l pl.UTF-8
Biblioteka rozszerzenia X Fixes.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXfixes.

%package static
Summary:	Static libXfixes library
Summary(pl.UTF-8):	Biblioteka statyczna libXfixes
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXfixes-static < 3.0.0

%description static
X Fixes extension library.

This package contains the static libXfixes library.

%description static -l pl.UTF-8
Biblioteka rozszerzenia X Fixes.

Pakiet zawiera statyczną bibliotekę libXfixes.

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
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README.md
%attr(755,root,root) %{_libdir}/libXfixes.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXfixes.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXfixes.so
%{_libdir}/libXfixes.la
%{_includedir}/X11/extensions/Xfixes.h
%{_pkgconfigdir}/xfixes.pc
%{_mandir}/man3/Xfixes.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXfixes.a
