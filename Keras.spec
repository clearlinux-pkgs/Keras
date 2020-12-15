#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Keras
Version  : 2.4.3
Release  : 58
URL      : https://files.pythonhosted.org/packages/df/1d/46fbcf446b5fa42aff723124fb10bc900e542389e7d7574b0c5466e1ffbc/Keras-2.4.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/df/1d/46fbcf446b5fa42aff723124fb10bc900e542389e7d7574b0c5466e1ffbc/Keras-2.4.3.tar.gz
Summary  : Deep Learning for humans
Group    : Development/Tools
License  : MIT
Requires: Keras-license = %{version}-%{release}
Requires: Keras-python = %{version}-%{release}
Requires: Keras-python3 = %{version}-%{release}
Requires: Keras_Applications
Requires: Keras_Preprocessing
Requires: Markdown
Requires: PyYAML
Requires: h5py
Requires: numpy
Requires: pandas
Requires: pydot
Requires: requests
Requires: scipy
BuildRequires : Keras_Applications
BuildRequires : Keras_Preprocessing
BuildRequires : Markdown
BuildRequires : PyYAML
BuildRequires : Theano
BuildRequires : buildreq-distutils3
BuildRequires : h5py
BuildRequires : numpy
BuildRequires : pandas
BuildRequires : pydot
BuildRequires : requests
BuildRequires : scipy
BuildRequires : setuptools-python
BuildRequires : tensorflow

%description
Keras is a high-level neural networks API for Python.

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
Provides: pypi(keras)
Requires: pypi(h5py)
Requires: pypi(numpy)
Requires: pypi(pyyaml)
Requires: pypi(scipy)

%description python3
python3 components for the Keras package.


%prep
%setup -q -n Keras-2.4.3
cd %{_builddir}/Keras-2.4.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603134590
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Keras
cp %{_builddir}/Keras-2.4.3/LICENSE %{buildroot}/usr/share/package-licenses/Keras/fe976930ac2b09766b74534d980d6c04bc566321
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Keras/fe976930ac2b09766b74534d980d6c04bc566321

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
