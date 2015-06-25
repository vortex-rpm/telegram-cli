%global		_github_commit	be1ac1f45691cabfd0456cbcb322eb46bd3ccd3c

Name:           telegram-cli
Version:        0
Release:        1.%{_github_commit}.vortex%{?dist}
Summary:        Telegram messenger CLI

Group:          Applications/Internet
License:        GPLv2
URL:            https://github.com/vysheng/tg
Vendor:		    Vortex RPM
Source0:        %{name}-%{_github_commit}.tar.gz
Patch0:         key-path.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:      lua-devel, openssl-devel, libconfig-devel, readline-devel
BuildRequires:	    libevent-devel, libjansson-devel, python-devel


%description
Command-line interface for Telegram. Uses readline interface.

%prep
%setup -q
%patch0 -p0


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datarootdir}/%{name}
install -D -m 0755 bin/%{name} $RPM_BUILD_ROOT/%{_bindir}/%{name}
install -D -m 0644 tg-server.pub $RPM_BUILD_ROOT/%{_datarootdir}/%{name}/tg-server.pub


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datarootdir}/%{name}
%doc README.md README.es README-PY.md README-LUA CHANGELOG


%changelog
* Thu Jun 25 2015 Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - 0-1.be1ac1f45691cabfd0456cbcb322eb46bd3ccd3c.vortex
- Initial packaging.
