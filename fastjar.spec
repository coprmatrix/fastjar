Name:         fastjar
Summary:      Fast Java Archive (JAR) Tool
URL:          https://savannah.nongnu.org/projects/fastjar
Group:        Archiver
License:      GPL
Version:      0.98
Release:      5.1
Source0:      https://download.savannah.gnu.org/releases/fastjar/fastjar-%{version}.tar.gz

%{?!install_info_prereq:%define install_info_prereq info}
%{?!install_info:%define install_info %{_sbindir}/install-info}
%{?!install_info_delete:%define install_info_delete %{install_info} --quiet –delete}

Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

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
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%files
%doc AUTHORS README NEWS ChangeLog
%{_bindir}/*
%{_infodir}/fastjar.info.*
%{_mandir}/man1/*.1.*

