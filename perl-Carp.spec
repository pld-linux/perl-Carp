#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Carp
Summary:	Carp - alternative warn and die for modules
Summary(pl.UTF-8):	Carp - alternatywne warn i die dla modułów
Name:		perl-Carp
Version:	1.50
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Carp/%{pdir}-%{version}.tar.gz
# Source0-md5:	95ad382253475fa9f7a4c04c8946136e
URL:		https://metacpan.org/dist/Carp
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(IPC::Open3) >= 1.01_03
BuildRequires:	perl-Test-Simple >= 0.47
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Carp routines are useful in your own modules because they act like
die() or warn(), but with a message which is more likely to be useful
to a user of your module. In the case of cluck, confess, and longmess
that context is a summary of every call in the call-stack. For a
shorter message you can use carp or croak which report the error as
being from where your module was called. There is no guarantee that
that is where the error was, but it is a good educated guess.

%description -l pl.UTF-8
Funkcje Carp są przydatne we własnych modułach, ponieważ zachowują się
jak die() lub warn(), ale z komunikatami bardziej przydatnymi
użytkownikowi modułu. W przypadku cluck, confess, longmess kontekstem
jest podsumowanie wszystkich wywołań ze stosu. Krótsze komunikaty
można uzyskać funkcjami carp lub croak, zgłaszającymi błąd tak, jakby
wystąpił w miejscu wywołania modułu. Nie ma gwarancji, że było to
miejsce wystąpienia błędu, ale jest to dosyć dobre przypuszczenie.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Carp.pm
%{perl_vendorlib}/Carp
%{_mandir}/man3/Carp.3pm*
