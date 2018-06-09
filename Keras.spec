#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Keras
Version  : 2.2.0
Release  : 32
URL      : http://pypi.debian.net/Keras/Keras-2.2.0.tar.gz
Source0  : http://pypi.debian.net/Keras/Keras-2.2.0.tar.gz
Summary  : Deep Learning for humans
Group    : Development/Tools
License  : MIT
Requires: Keras-python3
Requires: Keras-python
Requires: Keras_Applications
Requires: Keras_Preprocessing
Requires: h5py
Requires: numpy
Requires: pandas
Requires: pydot
Requires: requests
Requires: scipy
Requires: six
BuildRequires : Keras_Applications
BuildRequires : Keras_Preprocessing
BuildRequires : PyYAML
BuildRequires : Theano
BuildRequires : h5py
BuildRequires : numpy
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : scipy
BuildRequires : setuptools
BuildRequires : setuptools-python
BuildRequires : six
BuildRequires : tensorflow

%description
Keras is a high-level neural networks API,
        written in Python and capable of running on top of
        TensorFlow, CNTK, or Theano.

%package python
Summary: python components for the Keras package.
Group: Default
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
%setup -q -n Keras-2.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1528564980
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
