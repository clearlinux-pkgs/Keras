#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Keras
Version  : 2.1.2
Release  : 20
URL      : http://pypi.debian.net/Keras/Keras-2.1.2.tar.gz
Source0  : http://pypi.debian.net/Keras/Keras-2.1.2.tar.gz
Summary  : Deep Learning for Python
Group    : Development/Tools
License  : MIT
Requires: Keras-legacypython
Requires: Keras-python3
Requires: Keras-python
Requires: h5py
Requires: numpy
Requires: pandas
Requires: pydot
Requires: pytest
Requires: pytest-cov
Requires: pytest-xdist
Requires: scipy
Requires: six
BuildRequires : PyYAML
BuildRequires : Theano
BuildRequires : numpy
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : scipy
BuildRequires : setuptools
BuildRequires : six
BuildRequires : tensorflow

%description
ï»¿# Keras: Deep Learning for Python
![Keras logo](https://s3.amazonaws.com/keras.io/img/keras-logo-2018-large-1200.png)

%package legacypython
Summary: legacypython components for the Keras package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the Keras package.


%package python
Summary: python components for the Keras package.
Group: Default
Requires: Keras-legacypython
Requires: Keras-python3
Provides: keras-python

%description python
python components for the Keras package.


%package python3
Summary: python3 components for the Keras package.
Group: Default
Requires: python3-core

%description python3
python3 components for the Keras package.


%prep
%setup -q -n Keras-2.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1512433135
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1512433135
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
