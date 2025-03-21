#
# spec file for package obs-service-cpanspec
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#
%global service py2pack_generate

Name:           obs-service-py2pack_generate
Summary:        An OBS source service: Create spec files for cpan sources
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
Version:        0.7
Release:        0%{?autorelease}
Source:         py2pack_generate
Source1:        py2pack_generate.service
Requires:       python3-py2pack
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
install -Dm 0755 %{SOURCE0} %{buildroot}%{_obs_service_dir}/py2pack_generate
install -Dm 0644 %{SOURCE1} %{buildroot}%{_obs_service_dir}/py2pack_generate.service

%files
%defattr(-,root,root)
%{_obs_service_dir}/py2pack_generate
%{_obs_service_dir}/py2pack_generate.service

%changelog
