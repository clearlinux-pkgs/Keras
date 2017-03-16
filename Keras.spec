#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Keras
Version  : 2.0.0
Release  : 2
URL      : http://pypi.debian.net/Keras/Keras-2.0.0.tar.gz
Source0  : http://pypi.debian.net/Keras/Keras-2.0.0.tar.gz
Summary  : Deep Learning for Python
Group    : Development/Tools
License  : MIT
Requires: Keras-python
Requires: h5py
Requires: pytest
Requires: pytest-xdist
Requires: six
Requires: tensorflow
BuildRequires : PyYAML
BuildRequires : Theano
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : tensorflow

%description
No detailed description available

%package python
Summary: python components for the Keras package.
Group: Default
Provides: keras-python

%description python
python components for the Keras package.


%prep
%setup -q -n Keras-2.0.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489675580
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1489675580
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
