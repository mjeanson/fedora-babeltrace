Name:           babeltrace
Version:        1.0.3
Release:        1%{?dist}
License:        MIT and GPLv2
URL:            http://www.efficios.com/babeltrace
Source0:        http://www.efficios.com/files/%{name}/%{name}-%{version}.tar.bz2
Group:          Development/Tools
Summary:        Trace Viewer and Converter, mainly for the Common Trace Format
BuildRequires:  pkgconfig bison flex glib2-devel popt-devel libuuid-devel libtool
Requires:       lib%{name}%{?_isa} = %{version}-%{release}

%description
This project provides trace read and write libraries, as well as a trace
converter. A plugin can be created for any trace format to allow its conversion
to/from another trace format.

The main format expected to be converted to/from is the Common Trace
Format (CTF). See http://www.efficios.com/ctf.


%package -n lib%{name}
Summary:        Common Trace Format Babel Tower
Group:          Development/Libraries

%description -n lib%{name}
This project provides trace read and write libraries, as well as a trace
converter. A plugin can be created for any trace format to allow its conversion
to/from another trace format.



%package -n lib%{name}-devel
Summary:        Common Trace Format Babel Tower
Group:          Development/Libraries
Requires:       lib%{name}%{?_isa} = %{version}-%{release} glib2-devel

%description -n lib%{name}-devel
This project provides trace read and write libraries, as well as a trace
converter. A plugin can be created for any trace format to allow its conversion
to/from another trace format.


%prep
%setup -q -n %{name}-%{version}

%build
#Re-run libtoolize and autoreconf to remove rpath
libtoolize --force --copy
autoreconf -v --install --force
%configure --docdir=%{_docdir}/%{name}-%{version} --disable-static

make %{?_smp_mflags} V=1

%check
make check

%install
make DESTDIR=%{buildroot} install
rm -vf %{buildroot}%{_libdir}/*.la

%post  -n lib%{name} -p /sbin/ldconfig
%postun -n lib%{name} -p /sbin/ldconfig

%files
%{_bindir}/%{name}*
%doc ChangeLog LICENSE gpl-2.0.txt mit-license.txt 

%{_mandir}/man1/*.1*

%files -n lib%{name}
%{_libdir}/*.so.*
%doc ChangeLog LICENSE gpl-2.0.txt mit-license.txt 

%files -n lib%{name}-devel
%{_prefix}/include/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/babeltrace.pc

%changelog
* Tue Feb 26 2013 Yannick Brosseau <yannick.brosseau@gmail.com> - 1.0.3-1
- New upstream release
- Add pkg-config file to devel package (#913895)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Yannick Brosseau <yannick.brosseau@gmail.com> - 1.0.2-1
- New upstream release

* Tue Jan 15 2013 Yannick Brosseau <yannick.brosseau@gmail.com> - 1.0.0-3
- Change documentation directory to proper versionned one. 

* Mon Jan 14 2013 Yannick Brosseau <yannick.brosseau@gmail.com> - 1.0.0-2
- Use autoreconf rpath fix because the sed one was breaking the make check
- Use correct tar file version
- Package documentations in the right packages

* Mon Oct 29 2012 Yannick Brosseau <yannick.brosseau@gmail.com> - 1.0.0-1
- New upstream release

* Tue Oct 02 2012 Yannick Brosseau <yannick.brosseau@gmail.com> - 1.0.0-0.1.rc5
- New upstream release candidate
* Thu Jul 05 2012 Yannick Brosseau <yannick.brosseau@gmail.com> - 1.0.0-0.1.rc4
- New package, inspired by the one from OpenSuse 

