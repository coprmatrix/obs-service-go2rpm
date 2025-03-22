%global service rust2rpm

Name:           obs-service-rust2rpm
Summary:        An OBS source service: Create spec files for rust crates
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
Version:        1.17
Release:        0%{?autorelease}
Source:         rust2rpm
Source1:        rust2rpm.service
Requires:       rust2rpm
Requires:       rust2rpm-helper
BuildArch:      noarch
BuildRequires:  rpm_macro(_obs_service_dir)

%description
This is a source service for openSUSE Build Service.

It's a wrapper around cpanspec script

%prep
%setup -q -D -T 0 -c
sed -i 's~/usr/bin~%{_bindir}~' %{SOURCE0}

%build

%install
install -Dm 0755 %{SOURCE0} %{buildroot}%{_obs_service_dir}/rust2rpm
install -Dm 0644 %{SOURCE1} %{buildroot}%{_obs_service_dir}/rust2rpm.service

%files
%defattr(-,root,root)
%{_obs_service_dir}/rust2rpm
%{_obs_service_dir}/rust2rpm.service

%changelog
