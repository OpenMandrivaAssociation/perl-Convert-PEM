%define		module Convert-PEM

Name:		perl-%module
Version:	0.07
Release:	%mkrel 3
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Read/write encrypted ASN.1 PEM files
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Convert/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%module/
BuildRequires:	perl-devel
BuildRequires:	perl-Convert-ASN1 
BuildRequires:  perl-Class-ErrorHandler
BuildRequires:  perl-Crypt-DES_EDE3
# not found automatically
Requires:	perl(Class::ErrorHandler)
Requires:	perl
BuildArch:	noarch

%description
Convert::PEM reads and writes PEM files containing ASN.1-encoded
objects. The files can optionally be encrypted using a symmetric cipher
algorithm, such as 3DES.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/*/*

