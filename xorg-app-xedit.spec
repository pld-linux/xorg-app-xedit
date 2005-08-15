# $Rev: 3381 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	xedit application
Summary(pl):	Aplikacja xedit
Name:		xorg-app-xedit
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/xedit-%{version}.tar.bz2
# Source0-md5:	c673117da2e3ccb2809c59701a4e7c46
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXprintUtil-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/xedit-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
xedit application.

%description -l pl
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


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%{_sysconfdir}/X11/app-defaults/*
%attr(755,root,wheel) %{_bindir}/*
