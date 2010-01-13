%define		php_min_version 4.0.2
%include	/usr/lib/rpm/macros.php
Summary:	reCAPTCHA Library for PHP
Name:		php-recaptcha
Version:	1.10
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://recaptcha.googlecode.com/files/recaptcha-php-%{version}.zip
# Source0-md5:	978b6069fa6397b8e92254110d1657ff
URL:		http://recaptcha.net/plugins/php/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.520
Requires:	php-common >= 3:%{php_min_version}
Requires:	php-pcre
Suggests:	php-mcrypt
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# Exclude optional PHP extension dependencies
%define		_noautoreq	php(mcrypt)

%description
Provides a CAPTCHA for PHP using the reCAPTCHA service.

To use reCAPTCHA Mailhide, you need to have the mcrypt php module
installed.

%prep
%setup -q -n recaptcha-php-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -a recaptchalib.php $RPM_BUILD_ROOT%{php_data_dir}

# examples
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a example-*.php $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README
%{php_data_dir}/recaptchalib.php
%{_examplesdir}/%{name}-%{version}
