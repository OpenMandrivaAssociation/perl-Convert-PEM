%define	upstream_name    Convert-PEM
%define	upstream_version 0.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 6

Summary:	Read/write encrypted ASN.1 PEM files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Convert/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-Convert-ASN1 
BuildRequires:  perl-Class-ErrorHandler
BuildRequires:  perl-Crypt-DES_EDE3
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/*/*
