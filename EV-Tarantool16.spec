# don`t strip
%define __autobuild__ 0
%define __install_path usr
%define _unpackaged_files_terminate_build 0

%if %{__autobuild__}
%define version PKG_VERSION
%define branch GIT_TAG
%else
%define version 1.29.%(/bin/date +"%Y%m%d.%H%M")
%define branch master
%endif

Name: perl-EV-Tarantool16
Version: %{version}
Release: 1

Summary: EV client for Tarantool 1.6
License: GPL
Group: Development/Libraries
URL: https://github.com/derElektrobesen/EV-Tarantool16

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%if %{__autobuild__}
Packager: BUILD_USER
Source0: EV-Tarantool16-GIT_TAG.tar.bz2
%else
Packager: Pavel Berezhnoy <p.berezhnoy@corp.mail.ru>
%endif

BuildRequires: c-ares-devel
BuildRequires: msgpuck-devel

%description
EV::Tarantool16 - EV client for Tarantool 1.6

%if %{__autobuild__}
From tag: GIT_TAG
Git hash: GITHASH
Build by: BUILD_USER
%endif

%{lua:
if rpm.expand("%{__autobuild__}") == '1'
then
print("From tag: GIT_TAG\n")
print("Git hash: GITHASH\n")
print("Build by: BUILD_USER\n")
end}

%prep
%if %{__autobuild__}
%setup -q -n EV-Tarantool16
%else
rm -rf %{name}-%{version}
git clone --recursive https://github.com/derElektrobesen/EV-Tarantool16 %{name}-%{version}
%setup -T -D -n %{name}-%{version}
%endif

%build
mkdir -p %{buildroot}/%{__install_path}
pwd
perl Makefile.PL PREFIX=%{buildroot}/%{__install_path}
make

%install
make install

%files
/%{__install_path}/lib64/perl5/auto/EV/Tarantool16/Tarantool16.so
/%{__install_path}/lib64/perl5/EV/Tarantool16.pm
/%{__install_path}/lib64/perl5/EV/README.pod
/%{__install_path}/lib64/perl5/EV/Tarantool16/Multi.pm
/%{__install_path}/share/man/man3/EV::README.3pm.gz
/%{__install_path}/share/man/man3/EV::Tarantool16.3pm.gz

%post
ldconfig

%changelog
%if %{__autobuild__}
GIT_LOG
%endif

