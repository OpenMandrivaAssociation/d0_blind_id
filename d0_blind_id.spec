%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} %{major} -d

Summary:	Blind-ID library for user identification
Name:		d0_blind_id
Version:	0.6
Release:	6
License:	GPLv2+
Group:		Games/Arcade
Url:		http://git.xonotic.org/?p=xonotic/d0_blind_id.git;a=summary
Source0:	%{name}-%{version}.tar.bz2
Requires:	%{libname} = %{version}-%{release}
BuildRequires:	gmp-devel

%description
Cryptographic library to perform identification 
using Schnorr Identification scheme and Blind RSA Signatures.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n %{libname}
Shared library for %{name}.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel

%description -n %{develname}
Development files needed for compiling against %{name}.


%prep
%setup -q

%build
autoreconf -i

%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

%files
%doc COPYING d0_blind_id.txt
%{_bindir}/blind_id

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Sun Apr 22 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6-2
+ Revision: 792694
- enable rijndael support
- update docs

* Sun Apr 22 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6-1
+ Revision: 792646
- import d0_blind_id

