#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Alien-Libxml2
Version  : 0.16
Release  : 8
URL      : https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Alien-Libxml2-0.16.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Alien-Libxml2-0.16.tar.gz
Summary  : Install the C libxml2 library on your system
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Alien-Libxml2-license = %{version}-%{release}
Requires: perl-Alien-Libxml2-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : libxml2-dev
BuildRequires : perl(Alien::Build::MM)
BuildRequires : perl(Capture::Tiny)
BuildRequires : perl(File::Which)
BuildRequires : perl(File::chdir)
BuildRequires : perl(Importer)
BuildRequires : perl(Mojo::DOM58)
BuildRequires : perl(Path::Tiny)
BuildRequires : perl(Sort::Versions)
BuildRequires : perl(Sub::Info)
BuildRequires : perl(Test2::V0)
BuildRequires : perl(URI)
BuildRequires : perl(URI::Escape)

%description
NAME
Alien::Libxml2 - Install the C libxml2 library on your system
VERSION
version 0.16

%package dev
Summary: dev components for the perl-Alien-Libxml2 package.
Group: Development
Provides: perl-Alien-Libxml2-devel = %{version}-%{release}
Requires: perl-Alien-Libxml2 = %{version}-%{release}
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
%setup -q -n Alien-Libxml2-0.16
cd %{_builddir}/Alien-Libxml2-0.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
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
cp %{_builddir}/Alien-Libxml2-0.16/LICENSE %{buildroot}/usr/share/package-licenses/perl-Alien-Libxml2/5ebb55d13e4bb56ef0d1fa6aec3401f0055a505e
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Alien::Libxml2.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Alien-Libxml2/5ebb55d13e4bb56ef0d1fa6aec3401f0055a505e

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.2/x86_64-linux-thread-multi/Alien/Libxml2.pm
/usr/lib/perl5/vendor_perl/5.30.2/x86_64-linux-thread-multi/Alien/Libxml2/Install/Files.pm
/usr/lib/perl5/vendor_perl/5.30.2/x86_64-linux-thread-multi/auto/Alien/Libxml2/Libxml2.txt
/usr/lib/perl5/vendor_perl/5.30.2/x86_64-linux-thread-multi/auto/share/dist/Alien-Libxml2/_alien/alien.json
/usr/lib/perl5/vendor_perl/5.30.2/x86_64-linux-thread-multi/auto/share/dist/Alien-Libxml2/_alien/alienfile
