%define	modname	Convert-PEM
%define	modver	0.13

Summary:	Read/write encrypted ASN.1 PEM files
Name:		perl-%{modname}
Version:	%{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://github.com/perl-Crypt-OpenPGP/Convert-PEM
Source0:	https://cpan.metacpan.org/authors/id/T/TI/TIMLEGGE/Convert-PEM-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Convert::ASN1) 
BuildRequires:	perl-Class-ErrorHandler
BuildRequires:	perl-Crypt-DES_EDE3
# not found automatically
Requires:	perl(Class::ErrorHandler)
Requires:	perl

%description
Convert::PEM reads and writes PEM files containing ASN.1-encoded
objects. The files can optionally be encrypted using a symmetric cipher
algorithm, such as 3DES.

%prep
%setup -q -n %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

