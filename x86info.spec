Summary:        x86 processor information tool.
Name:           x86info
Version:        1.30
Release:        5%{?dist}
Epoch:          1
Group:          System Environment/Base
License:        GPLv2
Source0:        http://www.codemonkey.org.uk/projects/x86info/x86info-%{version}.tgz
ExclusiveArch:  %{ix86} x86_64
Url:            http://www.codemonkey.org.uk/projects/x86info
BuildRequires:  python2-devel pciutils-devel

%description
x86info displays diagnostic information about x86 processors, such
as cache configuration and supported features.

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_mandir}/man{1,8}

install -p -m 0755 x86info %{buildroot}%{_sbindir}/x86info
install -p -m 0644 x86info.1 %{buildroot}%{_mandir}/man1/
install -p -m 0755 lsmsr %{buildroot}%{_sbindir}/lsmsr
install -p -m 0644 lsmsr.8 %{buildroot}%{_mandir}/man8/


%files
%defattr(-,root,root,-)
%{_sbindir}/x86info
%{_sbindir}/lsmsr
%{_mandir}/man1/*
%{_mandir}/man8/*

%changelog
* Thu May 23 2013 Prarit Bhargava <prarit@redhat.com> - 1:1.30-5
- Add man page for lsmsr

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 09 2011 Dave Jones <davej@redhat.com>
- Update to new upstream 1.30

* Tue Apr 05 2011 Dave Jones <davej@redhat.com>
- Update to new upstream 1.29 (fixes lsmsr)

* Mon Mar 14 2011 Dave Jones <davej@redhat.com>
- Update to new upstream 1.28

* Tue Feb 08 2011 Dave Jones <davej@redhat.com>
- Correct license tag in spec. (It's explicitly GPLv2).

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Oct 02 2010 Parag Nemade <paragn AT fedoraproject.org> - 1.27-2
- Merge-review cleanup (#226547)

* Wed Sep 08 2010 Dave Jones <davej@redhat.com>
- Update to new upstream 1.27 (fixes build problem in 1.26)

* Wed Sep 08 2010 Dave Jones <davej@redhat.com>
- Update to new upstream 1.26

* Fri Oct 30 2009 Dave Jones <davej@redhat.com>
- Update to new upstream 1.25

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.24-1.42.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Adam Jackson <ajax@redhat.com>
- Fix parallel build.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.24-1.40.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb  6 2009 Dave Jones <davej@redhat.com>
- Update to new upstream 1.24

* Tue Dec 16 2008 Dave Jones <davej@redhat.com>
- Update to new upstream 1.23

* Tue Dec 16 2008 Dave Jones <davej@redhat.com>
- Update to new upstream 1.22

* Mon Mar 17 2008 Dave Jones <davej@redhat.com>
- More specfile cleanups.

* Thu Mar 13 2008 Dave Jones <davej@redhat.com>
- Fix rpmlint warnings.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1:1.21-1.29
- Autorebuild for GCC 4.3

* Mon Nov 26 2007 Dave Jones <davej@redhat.com>
- Update to new upstream 1.21

* Thu Aug 16 2007 Dave Jones <davej@redhat.com>
- Clarify license.

* Sat Jun 09 2007 Dave Jones <davej@redhat.com>
- Add URL: tag

* Wed Sep 27 2006 Dave Jones <davej@redhat.com>
- New upstream (1.20)
  Fixes 'silent' output, and recognises Intel Core Extreme.

* Sat Sep 23 2006 Dave Jones <davej@redhat.com>
- New upstream (1.19)
  Improved identification of numerous new Intel CPUs.

* Wed Jul 12 2006 Dave Jones <davej@redhat.com>
- New upstream (1.18)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1:1.17-1.22.1
- rebuild

* Thu Feb 09 2006 Dave Jones <davej@redhat.com>
- rebuild.

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcj

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Nov  4 2005 Dave Jones <davej@redhat.com>
- Update to upstream 1.17

* Sat Sep 24 2005 Dave Jones <davej@redhat.com>
- Update to upstream 1.16
  (Various 64bit fixes).

* Fri Sep  2 2005 Dave Jones <davej@redhat.com>
- Update to upstream 1.15

* Sun Aug  7 2005 Dave Jones <davej@redhat.com>
- Update to upstream 1.14 (now builds on x86-64)

* Fri Apr 15 2005 Florian La Roche <laroche@redhat.com>
- remove empty scripts

* Tue Mar  1 2005 Dave Jones <davej@redhat.com>
- Rebuild for gcc4

* Tue Feb  8 2005 Dave Jones <davej@redhat.com>
- Update to upstream 1.13

* Sat Dec 18 2004 Dave Jones <davej@redhat.com>
- Initial packaging, based upon kernel-utils.

