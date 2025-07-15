#
# TODO:
# - teach php-phc-m4-php.patch to be lib64-aware
# - fix final linking (fails to link boost_regex)
#
Summary:	open source compiler for PHP
Summary(pl.UTF-8):	kompilator dla PHP o otwartych źródłach
Name:		php-phc
Version:	0.3.0.1
Release:	0.1
License:	BSD
Group:		Applications
Source0:	http://phpcompiler.org/src/archive/phc-%{version}.tar.bz2
# Source0-md5:	098e3b45d973c1384535c8e8dee154b3
Patch0:		%{name}-m4-boost_regex.patch
Patch1:		%{name}-m4-php.patch
Patch2:		%{name}-php53.patch
URL:		http://www.phpcompiler.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	boost-regex >= 1.35.0
BuildRequires:	php-devel
BuildRequires:	php-embedded
BuildRequires:	xerces-c-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
phc is an open source compiler for PHP with support for plugins. In
addition, it can be used to pretty-print or obfuscate PHP code, as a
framework for developing applications that process PHP scripts, or to
convert PHP into XML and back, enabling processing of PHP scripts
using XML tools.

%prep
%setup -q -n phc-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%{__aclocal} -I m4 -I libltdl
%{__autoconf}
%{__automake}
%configure \
	--with-php=/usr \
	--disable-gc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
