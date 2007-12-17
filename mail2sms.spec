Summary:	Mail2sms is a mail to sms converter
Name:		mail2sms
Version:	1.3.5
Release:	%mkrel 4
License:	GPL
Group:		Networking/Other
URL:		http://daniel.haxx.se/projects/mail2sms/
Source:		http://daniel.haxx.se/projects/mail2sms/%{name}-%{version}.tar.bz2

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

