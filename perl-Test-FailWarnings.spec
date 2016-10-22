%{?scl:%scl_package perl-Test-FailWarnings}

Name:           %{?scl_prefix}perl-Test-FailWarnings
Version:        0.008
Release:        9%{?dist}
Summary:        Add test failures if warnings are caught
License:        ASL 2.0 

URL:            http://search.cpan.org/dist/Test-FailWarnings/
Source0:        http://www.cpan.org/authors/id/D/DA/DAGOLDEN/Test-FailWarnings-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.17
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.86
# Tests:
BuildRequires:  %{?scl_prefix}perl(Capture::Tiny) >= 0.12
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(File::Spec::Functions)
BuildRequires:  %{?scl_prefix}perl(File::Temp)
BuildRequires:  %{?scl_prefix}perl(IO::Handle)
BuildRequires:  %{?scl_prefix}perl(IPC::Open3)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(List::Util)
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))

%{?perl_default_filter}

%description
This module hooks $SIG{__WARN__} and converts warnings to Test::More's
fail() calls. It is designed to be used with done_testing, when you don't
need to know the test count in advance.

%prep
%setup -q -n Test-FailWarnings-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc Changes CONTRIBUTING LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jul 20 2016 Petr Pisar <ppisar@redhat.com> - 0.008-9
- SCL

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-8
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.008-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-5
- Perl 5.22 rebuild

* Fri Jan 09 2015 Petr Pisar <ppisar@redhat.com> - 0.008-4
- Specify all dependencies

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.008-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 29 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.008-1
- Update to 0.008

* Sun Sep 01 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.007-1
- Update to 0.007

* Sun Aug 25 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.006-1
- Update to 0.006

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.005-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Petr Pisar <ppisar@redhat.com> - 0.005-2
- Perl 5.18 rebuild

* Wed May 08 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.005-1
- Update to 0.005

* Fri May 03 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.003-2
- Take into account review comments (#957466)

* Sun Apr 28 2013 Emmanuel Seyman <emmanuel@seyman.fr> 0.003-1
- Specfile autogenerated by cpanspec 1.78.
