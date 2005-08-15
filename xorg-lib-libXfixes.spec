
#
Summary:	X Fixes extension library
Summary(pl):	Biblioteka rozszerzenia X Fixes
Name:		xorg-lib-libXfixes
Version:	3.0.0
Release:	0.02
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXfixes-%{version}.tar.bz2
# Source0-md5:	3134ce2f2c922324e1f8ae23900b2c22
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-proto-fixesproto-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/libXfixes-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
X Fixes extension library.

%description -l pl
Biblioteka rozszerzenia X Fixes.


%package devel
Summary:	Header files libXfixes development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXfixes
Group:		X11/Development/Libraries
Requires:	xorg-lib-libXfixes = %{version}-%{release}
Requires:	xorg-proto-fixesproto-devel
Requires:	xorg-lib-libX11-devel

%description devel
X Fixes extension library.

This package contains the header files needed to develop programs that
use these libXfixes.

%description devel -l pl
Biblioteka rozszerzenia X Fixes.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXfixes.


%package static
Summary:	Static libXfixes libraries
Summary(pl):	Biblioteki statyczne libXfixes
Group:		Development/Libraries
Requires:	xorg-lib-libXfixes-devel = %{version}-%{release}

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
%doc AUTHORS ChangeLog README
%attr(755,root,wheel) %{_libdir}/libXfixes.so.*


%files devel
%defattr(644,root,root,755)
%{_includedir}/X11/extensions/*.h
%{_libdir}/libXfixes.la
%attr(755,root,wheel) %{_libdir}/libXfixes.so
%{_pkgconfigdir}/xfixes.pc
%{_mandir}/man3/*.3*


%files static
%defattr(644,root,root,755)
%{_libdir}/libXfixes.a
