Name: geoclue-provider-gpsd3
Version: 0.2
Release: 1
Summary: geoclue provider for gpsd daemon
Group: System/Libraries
URL: https://github.com/neochapay/geoclue-provider-gpsd3
License: LGPLv2.1
Source: %{name}-%{version}.tar.gz
BuildRequires: pkgconfig(libgps) >= 3.19
BuildRequires: pkgconfig(geoclue) >= 0.12.99

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build
./autogen.sh
%configure
make %{?_smp_mflags}


%install
%make_install

%files
%defattr(-,root,root,-)
%{_libexecdir}/geoclue-gpsd3
%{_datadir}/dbus-1/services/org.freedesktop.Geoclue.Providers.Gpsd3.service
%{_datadir}/geoclue-providers/geoclue-gpsd3.provider
