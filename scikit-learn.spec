#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : scikit-learn
Version  : 1.1.1
Release  : 129
URL      : https://github.com/scikit-learn/scikit-learn/archive/1.1.1/scikit-learn-1.1.1.tar.gz
Source0  : https://github.com/scikit-learn/scikit-learn/archive/1.1.1/scikit-learn-1.1.1.tar.gz
Summary  : A set of python modules for machine learning and data mining
Group    : Development/Tools
License  : BSD-3-Clause
Requires: scikit-learn-filemap = %{version}-%{release}
Requires: scikit-learn-lib = %{version}-%{release}
Requires: scikit-learn-license = %{version}-%{release}
Requires: scikit-learn-python = %{version}-%{release}
Requires: scikit-learn-python3 = %{version}-%{release}
Requires: pypi-joblib
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cython)
BuildRequires : pypi(matplotlib)
BuildRequires : pypi(numpy)
BuildRequires : pypi(pandas)
BuildRequires : pypi(scikit_image)
BuildRequires : pypi(scikit_learn)
BuildRequires : pypi(scipy)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(sphinx_gallery)
BuildRequires : pypi(wheel)
BuildRequires : pypi-cython
BuildRequires : pypi-pytest

%description
This directory contains bundled external dependencies that are updated
every once in a while.

%package filemap
Summary: filemap components for the scikit-learn package.
Group: Default

%description filemap
filemap components for the scikit-learn package.


%package lib
Summary: lib components for the scikit-learn package.
Group: Libraries
Requires: scikit-learn-license = %{version}-%{release}
Requires: scikit-learn-filemap = %{version}-%{release}

%description lib
lib components for the scikit-learn package.


%package license
Summary: license components for the scikit-learn package.
Group: Default

%description license
license components for the scikit-learn package.


%package python
Summary: python components for the scikit-learn package.
Group: Default
Requires: scikit-learn-python3 = %{version}-%{release}

%description python
python components for the scikit-learn package.


%package python3
Summary: python3 components for the scikit-learn package.
Group: Default
Requires: scikit-learn-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(scikit_learn)
Requires: pypi(joblib)
Requires: pypi(matplotlib)
Requires: pypi(numpy)
Requires: pypi(pandas)
Requires: pypi(scikit_image)
Requires: pypi(scipy)
Requires: pypi(sphinx_gallery)
Requires: pypi(threadpoolctl)

%description python3
python3 components for the scikit-learn package.


%prep
%setup -q -n scikit-learn-1.1.1
cd %{_builddir}/scikit-learn-1.1.1
pushd ..
cp -a scikit-learn-1.1.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656425773
unset LD_AS_NEEDED
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pytest sklearn || :
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/scikit-learn
cp %{_builddir}/scikit-learn-1.1.1/COPYING %{buildroot}/usr/share/package-licenses/scikit-learn/2a3ba0cd0df7c92d6322141b1f9a0b153b30e391
cp %{_builddir}/scikit-learn-1.1.1/sklearn/svm/src/liblinear/COPYRIGHT %{buildroot}/usr/share/package-licenses/scikit-learn/98a0f7cd8d323be9a1aea7f957868b11361c4f51
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-scikit-learn

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/scikit-learn/2a3ba0cd0df7c92d6322141b1f9a0b153b30e391
/usr/share/package-licenses/scikit-learn/98a0f7cd8d323be9a1aea7f957868b11361c4f51

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
