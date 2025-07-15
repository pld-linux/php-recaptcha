%define		pkgname	recaptcha
%define		php_min_version 5.0.0
Summary:	reCAPTCHA is a free service to protect your website from spam and abuse
Name:		php-%{pkgname}
Version:	1.1.2
Release:	1
Epoch:		1
# google/recaptcha: BSD
# recaptcha-php: MIT
License:	BSD, MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/google/recaptcha/archive/%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	4528aeab04f7a22df4c1ec208b181b18
Source1:	http://recaptcha.googlecode.com/files/recaptcha-php-1.11.zip
# Source1-md5:	06dbb91aeb1869b3051d1b87dea0b891
Patch0:		autoload.patch
URL:		http://www.google.com/recaptcha/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.520
BuildRequires:	unzip
Requires:	php(core) >= %{php_min_version}
Requires:	php(pcre)
Suggests:	php(mcrypt)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# Exclude optional PHP extension dependencies
%define		_noautoreq	php-mcrypt

%description
reCAPTCHA is a free CAPTCHA service that protect websites from spam
and abuse. This is Google authored code that provides plugins for
third-party integration with reCAPTCHA.

%prep
%setup -q -n recaptcha-%{version} -a1

mv src/{,ReCaptcha/}autoload.php
%patch -P0 -p1

mv recaptcha-php-* recaptcha-php
mv recaptcha-php/LICENSE{,.recaptcha-php}
mv recaptcha-php/README{,.recaptcha-php}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_data_dir},%{_examplesdir}/%{name}-%{version}/recaptcha-php}

cp -a src/* $RPM_BUILD_ROOT%{php_data_dir}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# old package
cd recaptcha-php
cp -a recaptchalib.php $RPM_BUILD_ROOT%{php_data_dir}
cp -a example-*.php $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/recaptcha-php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CONTRIBUTING.md LICENSE composer.json
%{php_data_dir}/ReCaptcha
%{_examplesdir}/%{name}-%{version}

# old package contents
%doc recaptcha-php/{LICENSE,README}.*
%{php_data_dir}/recaptchalib.php
