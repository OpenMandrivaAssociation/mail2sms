Summary:	Mail to SMS converter
Name:		mail2sms
Version:	1.3.5
Release:	10
License:	GPL
Group:		Networking/Other
URL:		http://daniel.haxx.se/projects/mail2sms/
Source:		http://daniel.haxx.se/projects/mail2sms/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
mail2sms reads a (MIME) mail and converts it to a short message. It offers
search and replace, conditional rules, conditional search and replace etc to
create a custom output. It can optionally pipe its output into a specified
program.

%prep

%setup -q

%build

%configure

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d  %{buildroot}%{_sysconfdir}/mail/mail/sms
install -d  %{buildroot}%{_bindir}
install -d  %{buildroot}%{_mandir}/man1
install -d  %{buildroot}%{_mandir}/man4

install -m0755 %{name} %{buildroot}%{_bindir}/%{name}
install -m0644 example.conf %{buildroot}%{_sysconfdir}/mail/mail/sms/mail2sms.conf
install -m0644 %{name}.1  %{buildroot}%{_mandir}/man1/
install -m0644 %{name}.4  %{buildroot}%{_mandir}/man4/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc CHANGES FILES INSTALL LEGAL README REGEX TODO forward.README forward.example
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/mail/mail/sms/mail2sms.conf
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0644,root,root) %{_mandir}/man1/*
%attr(0644,root,root) %{_mandir}/man4/*



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.5-9mdv2011.0
+ Revision: 620288
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.3.5-8mdv2010.0
+ Revision: 429907
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 1.3.5-7mdv2009.0
+ Revision: 251705
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.3.5-5mdv2008.1
+ Revision: 170976
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 1.3.5-4mdv2008.1
+ Revision: 140935
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import mail2sms


* Tue Sep 19 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3.5-4mdv2007.0
- rebuild
- new url's
- added the config
- added the man pages

* Wed Jul 06 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.3.5-3mdk
- rebuild

* Wed Jun 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.3.5-2mdk
- rebuild

* Fri Apr 04 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.3.5-1mdk
- 1.3.5

* Tue Jan 28 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.3.3-2mdk
- rebuild

* Fri Nov 16 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.3.3-1mdk
- 1.3.3

* Tue Aug 21 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.3.2-1mdk
- updated to 1.3.2

* Mon Jan 22 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.2.1-1mdk
- updated to 1.2.1

* Mon Sep 11 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.33-3mdk
- BM
- macros

* Tue May 02 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.33-2mdk
- fix group
- fix files section

* Tue Nov 30 1999 Lenny Cartier <lenny@mandrakesoft.com>
- new in contribs
