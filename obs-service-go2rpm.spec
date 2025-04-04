%global service go2rpm

Name:           obs-service-%{service}
Summary:        An OBS source service: Create spec files for rust crates
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
Version:        1.18
Release:        0%{?autorelease}
Source:         %{service}
Requires:       go2rpm
BuildRequires:  python3
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
install -Dm 0755 %{SOURCE0} %{buildroot}%{_obs_service_dir}/%{service}
SERVICE_OUTFILE=%{buildroot}%{_obs_service_dir}/%{service}.service python3 %{SOURCE0} --noop enable

%files
%defattr(-,root,root)
%{_obs_service_dir}/%{service}
%{_obs_service_dir}/%{service}.service

%changelog
