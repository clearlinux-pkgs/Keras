#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Keras
Version  : 2.2.4
Release  : 50
URL      : https://files.pythonhosted.org/packages/13/5c/11b1d1e709cfb680cf5cc592f8e37d3db19871ee5c5cc0d9ddbae4e911c7/Keras-2.2.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/13/5c/11b1d1e709cfb680cf5cc592f8e37d3db19871ee5c5cc0d9ddbae4e911c7/Keras-2.2.4.tar.gz
Summary  : Deep Learning for humans
Group    : Development/Tools
License  : MIT
Requires: Keras-license = %{version}-%{release}
Requires: Keras-python = %{version}-%{release}
Requires: Keras-python3 = %{version}-%{release}
Requires: Keras_Applications
Requires: Keras_Preprocessing
Requires: PyYAML
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
BuildRequires : buildreq-distutils3
BuildRequires : h5py
BuildRequires : numpy
BuildRequires : scipy
BuildRequires : setuptools-python
BuildRequires : six
BuildRequires : tensorflow
Patch1: 9416f3647ac4c9ec0c57575a66d66aeac077d56c.patch

%description
Keras is a high-level neural networks API,
        written in Python and capable of running on top of
        TensorFlow, CNTK, or Theano.

%package license
Summary: license components for the Keras package.
Group: Default

%description license
license components for the Keras package.


%package python
Summary: python components for the Keras package.
Group: Default
Requires: Keras-python3 = %{version}-%{release}
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
%setup -q -n Keras-2.2.4
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556653028
export LDFLAGS="${LDFLAGS} -fno-lto"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Keras
cp LICENSE %{buildroot}/usr/share/package-licenses/Keras/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Keras/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
