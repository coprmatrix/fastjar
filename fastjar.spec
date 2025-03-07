Name:         fastjar
Summary:      Fast Java Archive (JAR) Tool
URL:          https://savannah.nongnu.org/projects/fastjar
Group:        Archiver
License:      GPL
Version:      0.98
Release:      7%{?autorelease}
Source0:      https://download.savannah.gnu.org/releases/fastjar/fastjar-%{version}.tar.gz
Patch0:       fastjar-CVE-2010-2322.patch
Patch1:       fix-update-mode.diff

%{?!ext_info:%define ext_info .gz}

Requires(post):  info
Requires(preun): info

BuildRequires:  zlib-devel
BuildRequires:  autoconf
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  automake

%description
FastJar is an attempt at creating a feature-for-feature copy of
Sun's JDK's jar(1) command. Sun's jar(1) is written entirely in Java
which makes it very slow. Since FastJar is written in C, it can
create the same .jar file as Sun's tool in a fraction of the time.

%prep
%setup -q
%autopatch -p1

%build
autoreconf -ifv

./configure \
    --prefix=%{_prefix} \
    --mandir=%{_mandir} \
    --infodir=%{_infodir}
%{__make} %{_smp_mflags -O}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"
#rm -f $RPM_BUILD_ROOT%{_prefix}/lib/charset.alias
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%post
install-info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun
install-info --info-dir=%{_infodir} --delete %{_infodir}/%{name}.info%{ext_info}

%files
%doc AUTHORS README NEWS ChangeLog
%{_bindir}/*
%{_infodir}/fastjar.info%{ext_info}
%{_mandir}/man1/*.1%{ext_info}

