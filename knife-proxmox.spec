Summary:	ProxmoxVE Support for Chef's Knife Command
Name:		knife-proxmox
Version:	0.0.19
Release:	1
License:	GPL v2+ or Ruby
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{name}-%{version}.gem
# Source0-md5:	d9dc86e214af6a64c328a540b8297ff5
URL:		https://bitbucket.org/jmoratilla/knife-proxmox
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
Requires:	knife >= 0.10.10
Requires:	ruby-json >= 1.5.4
Requires:	ruby-rest-client >= 1.6.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ProxmoxVE Support for Chef's Knife Command

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGELOG LICENSE TODO
%{ruby_vendorlibdir}/chef/knife/connection.rb
%{ruby_vendorlibdir}/chef/knife/proxmox_*.rb
%{ruby_vendorlibdir}/chef/knife/server.rb
%{ruby_vendorlibdir}/chef/knife/template.rb
%{ruby_vendorlibdir}/knife-proxmox
