Summary:	xedit application
Summary(pl.UTF-8):	Aplikacja xedit
Name:		xorg-app-xedit
Version:	1.0.2
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xedit-%{version}.tar.bz2
# Source0-md5:	c56160e93c24ddf17e69891ed50deb72
Source1:	xedit.desktop
Source2:	xedit.png
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXp-devel
BuildRequires:	xorg-lib-libXprintUtil-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-util-util-macros >= 0.99.2
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xedit application.

%description -l pl.UTF-8
Aplikacja xedit.

%prep
%setup -q -n xedit-%{version}

%build
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

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/xedit.desktop
install -D %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/xedit.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/xedit
%{_datadir}/X11/app-defaults/Xedit*
%{_libdir}/X11/xedit
%{_desktopdir}/xedit.desktop
%{_pixmapsdir}/xedit.png
%{_mandir}/man1/xedit.1x*
