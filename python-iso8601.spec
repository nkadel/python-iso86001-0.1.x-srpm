%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global pypi_name iso8601
%global pypi_version 0.1.11

%global sum Simple module to parse ISO 8601 dates
%global pkgdesc \
This module parses the most common forms of ISO 8601 date strings \
(e.g. 2007-01-14T20:34:22+00:00) into datetime objects.

Name:           python-%{pypi_name}
Version:        %{pypi_version}
#Release:        8%%{?dist}
Release:        0.8%{?dist}
Summary:        %{sum}

License:        MIT
URL:            http://pypi.python.org/pypi/%{pypi_name}/
#Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/%{pypi_name}-%{pypi_version}.tar.gz
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python-srpm-macros

%description %{pkgdesc}

%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{pypi_name} %{pkgdesc}

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build
%if 0%{?with_python3_other}
%py3_other_build
%endif

%install
%py3_install
%if 0%{?with_python3_other}
%py3_other_install
%endif

%files -n python%{python3_pkgversion}-%{pypi_name}
%doc LICENSE README.rst
%{python3_sitelib}/*

%changelog
* Fri Mar 08 2019 Troy Dawson <tdawson@redhat.com> - 0.1.11-8
- Rebuilt to change main python from 3.4 to 3.6

* Wed Aug 16 2017 Aurelien Bompard <abompard@fedoraproject.org> - 0.1.11-7
- Build for Python3 on EPEL:
  http://fedoraproject.org/wiki/PackagingDrafts:Python3EPEL
- Modernize the spec a bit (build and install macros, no explicit buildroot)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 12 2016 Stratakis Charalampos <cstratak@redhat.com> - 0.1.11-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 0.1.11-1
- Upstream 0.1.11

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Nov 04 2015 Robert Kuska <rkuska@redhat.com> - 0.1.10-7
- Rebuilt for Python3.5 rebuild

* Mon Sep 07 2015 Chandan Kumar <chkumar246@gmail.com> - 0.1.10-6
- Added python2 along with python3 subpackage

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Apr 23 2014 Pádraig Brady <pbrady@redhat.com> - 0.1.10-2
- Add python3 package

* Thu Mar 27 2014 Pádraig Brady <pbrady@redhat.com> - 0.1.10-1
- Latest upstream

* Tue Nov 12 2013 Pádraig Brady <pbrady@redhat.com> - 0.1.8-1
- Latest upstream

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul  9 2010 Ian Weller <iweller@redhat.com> - 0.1.4-2
- Correct python_sitelib macro

* Mon Jun 28 2010 Ian Weller <iweller@redhat.com> - 0.1.4-1
- Initial package build
