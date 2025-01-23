#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Alien-Libxml2
Version  : 0.19
Release  : 31
URL      : https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Alien-Libxml2-0.19.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Alien-Libxml2-0.19.tar.gz
Summary  : 'Install the C libxml2 library on your system'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Alien-Libxml2-license = %{version}-%{release}
Requires: perl-Alien-Libxml2-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : libxml2-dev
BuildRequires : perl(Alien::Build::MM)
BuildRequires : perl(Alien::Build::Plugin::Download::GitLab)
BuildRequires : perl(Capture::Tiny)
BuildRequires : perl(File::Which)
BuildRequires : perl(File::chdir)
BuildRequires : perl(Importer)
BuildRequires : perl(Path::Tiny)
BuildRequires : perl(Sub::Info)
BuildRequires : perl(Term::Table)
BuildRequires : perl(Test2::V0)
BuildRequires : perl(URI)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Alien::Libxml2 - Install the C libxml2 library on your system
VERSION
version 0.19

%package dev
Summary: dev components for the perl-Alien-Libxml2 package.
Group: Development
Provides: perl-Alien-Libxml2-devel = %{version}-%{release}
Requires: perl-Alien-Libxml2 = %{version}-%{release}

%description dev
dev components for the perl-Alien-Libxml2 package.


%package license
Summary: license components for the perl-Alien-Libxml2 package.
Group: Default

%description license
license components for the perl-Alien-Libxml2 package.


%package perl
Summary: perl components for the perl-Alien-Libxml2 package.
Group: Default
Requires: perl-Alien-Libxml2 = %{version}-%{release}

%description perl
perl components for the perl-Alien-Libxml2 package.


%prep
%setup -q -n Alien-Libxml2-0.19
cd %{_builddir}/Alien-Libxml2-0.19
pushd ..
cp -a Alien-Libxml2-0.19 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Alien-Libxml2
cp %{_builddir}/Alien-Libxml2-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Alien-Libxml2/22cfe221b1b815687cc108dbdccf845cbb96bca7 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Alien::Libxml2.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Alien-Libxml2/22cfe221b1b815687cc108dbdccf845cbb96bca7

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
