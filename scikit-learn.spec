#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : scikit-learn
Version  : 0.19.1
Release  : 60
URL      : https://github.com/scikit-learn/scikit-learn/archive/0.19.1.tar.gz
Source0  : https://github.com/scikit-learn/scikit-learn/archive/0.19.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause BSD-3-Clause-Clear
Requires: scikit-learn-python3
Requires: scikit-learn-license
Requires: scikit-learn-python
Requires: nose
Requires: numpy
Requires: scipy
Requires: wheel
BuildRequires : Cython
BuildRequires : numpy
BuildRequires : numpy-legacypython
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : scipy
BuildRequires : setuptools
Patch1: build.patch

%description
This directory contains bundled external dependencies that are updated
every once in a while.

%package license
Summary: license components for the scikit-learn package.
Group: Default

%description license
license components for the scikit-learn package.


%package python
Summary: python components for the scikit-learn package.
Group: Default
Requires: scikit-learn-python3

%description python
python components for the scikit-learn package.


%package python3
Summary: python3 components for the scikit-learn package.
Group: Default
Requires: python3-core

%description python3
python3 components for the scikit-learn package.


%prep
%setup -q -n scikit-learn-0.19.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1529161079
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/scikit-learn
cp COPYING %{buildroot}/usr/share/doc/scikit-learn/COPYING
cp sklearn/svm/src/liblinear/COPYRIGHT %{buildroot}/usr/share/doc/scikit-learn/sklearn_svm_src_liblinear_COPYRIGHT
cp doc/sphinxext/LICENSE.txt %{buildroot}/usr/share/doc/scikit-learn/doc_sphinxext_LICENSE.txt
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/scikit-learn/COPYING
/usr/share/doc/scikit-learn/doc_sphinxext_LICENSE.txt
/usr/share/doc/scikit-learn/sklearn_svm_src_liblinear_COPYRIGHT

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
