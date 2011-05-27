%define        _class           MDB2
%define        _subclass        Driver_sqlite
%define        upstream_name    %{_class}_%{_subclass}

Name:           php-pear-%{upstream_name}
Version:        1.5.0
Release:        %mkrel 0.0.b3.1
Summary:        Sqlite MDB2 driver
Epoch:          1
License:        PHP License
Group:          Development/PHP
URL:            http://pear.php.net/package/MDB2_Driver_sqlite/
Source0:        http://download.pear.php.net/package/MDB2_Driver_sqlite-%{version}b3.tgz
Requires:	php-sqlite
Requires(post): php-pear
Requires(preun): php-pear
Requires:       php-pear
BuildRequires:  php-pear
BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
MDB2 sqlite driver.

%prep
%setup -q -c -n %{name}-%{version}b3
mv package.xml %{upstream_name}-%{version}b3/%{upstream_name}.xml

%install
%{__rm} -rf %{buildroot}

cd %{upstream_name}-%{version}b3
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml
