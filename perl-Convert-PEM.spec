%define	upstream_name    Convert-PEM
%define	upstream_version 0.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	8

Summary:	Read/write encrypted ASN.1 PEM files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Convert/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-Convert-ASN1 
BuildRequires:	perl-Class-ErrorHandler
BuildRequires:	perl-Crypt-DES_EDE3
BuildRequires:	perl-devel
BuildArch:	noarch

# not found automatically
Requires:	perl(Class::ErrorHandler)
Requires:	perl

%description
Convert::PEM reads and writes PEM files containing ASN.1-encoded
objects. The files can optionally be encrypted using a symmetric cipher
algorithm, such as 3DES.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.80.0-6mdv2012.0
+ Revision: 765112
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.80.0-5
+ Revision: 763569
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 0.80.0-4
+ Revision: 676622
- rebuild

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 0.80.0-3
+ Revision: 676517
- rebuild

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.80.0-2
+ Revision: 656895
- rebuild for updated spec-helper

* Wed Dec 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.80.0-1mdv2011.0
+ Revision: 616207
- update to new version 0.08

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.70.0-1mdv2011.0
+ Revision: 406920
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.07-5mdv2009.0
+ Revision: 256136
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.07-3mdv2008.1
+ Revision: 136694
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-3mdv2008.0
+ Revision: 86230
- rebuild


* Fri Jul 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.07-2mdk
- Fix BuildRequires

* Tue Jun 07 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.07-1mdk
- 0.07
- cleanup spec, add Changes file

* Mon Jun 06 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.06-3mdk
- Rebuild for new perl

* Wed Feb 09 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.06-2mdk
- rebuild for new perl

* Thu Nov 06 2003 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 0.06-1mdk
- New package

