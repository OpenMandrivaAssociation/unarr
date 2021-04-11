%define major	1
%define libname	%mklibname unarr %{major}
%define devname %mklibname -d unarr

Name:		unarr
Version:	1.0.1
Release:	1
Group:		Development/C
Summary:	A decompression library
License:	LGPLv3+

URL:            https://github.com/selmf/unarr/
Source0:	https://github.com/selmf/unarr/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires: 	cmake(ZLIB)
BuildRequires: 	pkgconfig(zlib)
BuildRequires: 	bzip2-devel

%description
A lightweight decompression library with support for rar, tar and zip
archives

%package -n %{libname}
Summary:        A decompression library

%description -n %{libname}
A lightweight decompression library with support for rar, tar and zip
archives

%package -n %{devname}
Summary:	Development files for %{name}
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -qn %{name}-%{version}

%build
%cmake 
%make_build

%install
%make_install -C build LIBDIR=%{_libdir}
find %{buildroot} -name '*.a' -exec rm -f {} ';'

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/libunarr.pc
