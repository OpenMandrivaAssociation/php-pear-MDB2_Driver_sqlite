%define        _class           MDB2_Driver_sqlite
%define        _pearname        %{_class}
%define        _status          stable

Summary:        %{_pearname} - sqlite MDB2 driver
Name:           php-pear-%{_pearname}
Version:        1.4.1
Release:        %mkrel 1
Epoch:          0
License:        PHP License
Group:          Development/PHP
Source0:        http://download.pear.php.net/package/MDB2_Driver_sqlite-%{version}.tgz
URL:            http://pear.php.net/package/MDB2_Driver_sqlite/
Requires(post): php-pear
Requires(preun): php-pear
Requires:       php-pear
Requires:       php-pear-MDB2
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot

%description
MDB2 sqlite driver.

In PEAR status of this package is: %{_status}.

%prep
%setup -q -c
find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then %{__rm} -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | %{__grep} -v ".gif" | %{__grep} -v ".png" | %{__grep} -v ".jpg" | xargs %{__perl} -pi -e 's|\r$||g'

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_datadir}/pear/MDB2/Driver/{Datatype,Function,Manager,Native,Reverse}

%{__cp} -a %{_pearname}-%{version}/MDB2/Driver/*.php %{buildroot}%{_datadir}/pear/MDB2/Driver/
%{__cp} -a %{_pearname}-%{version}/MDB2/Driver/Datatype/*.php %{buildroot}%{_datadir}/pear/MDB2/Driver/Datatype/
%{__cp} -a %{_pearname}-%{version}/MDB2/Driver/Function/*.php %{buildroot}%{_datadir}/pear/MDB2/Driver/Function/
%{__cp} -a %{_pearname}-%{version}/MDB2/Driver/Manager/*.php %{buildroot}%{_datadir}/pear/MDB2/Driver/Manager/
%{__cp} -a %{_pearname}-%{version}/MDB2/Driver/Native/*.php %{buildroot}%{_datadir}/pear/MDB2/Driver/Native/
%{__cp} -a %{_pearname}-%{version}/MDB2/Driver/Reverse/*.php %{buildroot}%{_datadir}/pear/MDB2/Driver/Reverse/

%{__mkdir_p} %{buildroot}%{_datadir}/pear/packages
%{__cp} -a package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
        if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
                %{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
        fi
fi
if [ "$1" = "2" ]; then
        if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
               %{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
        fi
fi

%preun
if [ "$1" = 0 ]; then
        if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
                %{_bindir}/pear uninstall --nodeps -r %{_pearname}
        fi
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc
%{_datadir}/pear/MDB2/Driver/Datatype/sqlite.php
%{_datadir}/pear/MDB2/Driver/Function/sqlite.php
%{_datadir}/pear/MDB2/Driver/Manager/sqlite.php
%{_datadir}/pear/MDB2/Driver/Native/sqlite.php
%{_datadir}/pear/MDB2/Driver/Reverse/sqlite.php
%{_datadir}/pear/MDB2/Driver/sqlite.php
%{_datadir}/pear/packages/%{_pearname}.xml


