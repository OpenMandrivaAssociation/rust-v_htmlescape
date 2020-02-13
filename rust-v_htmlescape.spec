# Generated by rust2rpm 11
%bcond_without check
%global debug_package %{nil}

%global crate v_htmlescape

Name:           rust-%{crate}
Version:        0.4.5
Release:        2%{?dist}
Summary:        Simd optimized HTML escaping code

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/v_htmlescape
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Simd optimized HTML escaping code.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 20:52:11 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.5-1
- Update to 0.4.5

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 20:00:09 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.3-2
- Regenerate

* Thu May 30 18:16:54 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.3-1
- Initial package
