%define upstream_name	 Sys-CPU
Name: 		perl-%{upstream_name}
Version: 	0.52
Release:	3

Summary:	Perl extension for getting CPU information. Currently only number of CPU's supported
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Sys-CPU
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CDDB/%{upstream_name}-%{version}.tar.gz

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

BuildRequires:	make
%description
In responce to a post on perlmonks.org, a module for counting the number
of CPU's on a system. Support has now also been added for type of CPU
and clock speed. While much of the code is from UNIX::Processors, win32
support has been added (but not tested).

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorarch}/auto/Sys/CPU/*
%{perl_vendorarch}/Sys/CPU.pm
%{_mandir}/*/*

