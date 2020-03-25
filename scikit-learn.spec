#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : scikit-learn
Version  : 0.22.2
Release  : 93
URL      : https://github.com/scikit-learn/scikit-learn/archive/0.22.2/scikit-learn-0.22.2.tar.gz
Source0  : https://github.com/scikit-learn/scikit-learn/archive/0.22.2/scikit-learn-0.22.2.tar.gz
Summary  : A set of python modules for machine learning and data mining
Group    : Development/Tools
License  : BSD-3-Clause
Requires: scikit-learn-license = %{version}-%{release}
Requires: scikit-learn-python = %{version}-%{release}
Requires: scikit-learn-python3 = %{version}-%{release}
Requires: joblib
Requires: matplotlib
Requires: pandas
Requires: scikit-image
Requires: scikit-learn
BuildRequires : Cython
BuildRequires : buildreq-distutils3
BuildRequires : joblib
BuildRequires : matplotlib
BuildRequires : numpy
BuildRequires : pandas
BuildRequires : pytest
BuildRequires : scikit-image
BuildRequires : scikit-learn
BuildRequires : scipy
Patch1: 0001-avx512-for-libsvm-kernel-dot-function.patch

%description
|Azure|_ |Travis|_ |Codecov|_ |CircleCI|_ |PythonVersion|_ |PyPi|_ |DOI|_
.. |Azure| image:: https://dev.azure.com/scikit-learn/scikit-learn/_apis/build/status/scikit-learn.scikit-learn?branchName=master
.. _Azure: https://dev.azure.com/scikit-learn/scikit-learn/_build/latest?definitionId=1&branchName=master

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
Requires: python3-core
Provides: pypi(scikit_learn)
Requires: pypi(joblib)
Requires: pypi(numpy)
Requires: pypi(scipy)

%description python3
python3 components for the scikit-learn package.


%prep
%setup -q -n scikit-learn-0.22.2
cd %{_builddir}/scikit-learn-0.22.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1585156676
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pytest sklearn || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/scikit-learn
cp %{_builddir}/scikit-learn-0.22.2/COPYING %{buildroot}/usr/share/package-licenses/scikit-learn/bfae5540bd15169fd97fd9ff6e224d2c12ae859e
cp %{_builddir}/scikit-learn-0.22.2/sklearn/svm/src/liblinear/COPYRIGHT %{buildroot}/usr/share/package-licenses/scikit-learn/98a0f7cd8d323be9a1aea7f957868b11361c4f51
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/scikit-learn/98a0f7cd8d323be9a1aea7f957868b11361c4f51
/usr/share/package-licenses/scikit-learn/bfae5540bd15169fd97fd9ff6e224d2c12ae859e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
