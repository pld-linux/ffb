Summary:	f*ckf*ckb**b - a f*ckf*ck interpreter written in C++
Summary(pl.UTF-8):	f*ckf*ckb**b - interpreter języka f*ckf*ck napisany w C++
Name:		ffb
Version:	0.2
Release:	1
License:	?
Group:		Development/Languages
Source0:	http://www.stacken.kth.se/~foo/feckfeck/files/%{name}-%{version}.tar.gz
# Source0-md5:	b58e2796867561bf88e99383ea352d74
URL:		http://www.stacken.kth.se/~foo/feckfeck/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
f*ckf*ckb**b is a f*ckf*ck interpreter written in C++.

f*ckf*ck language is described at
http://www.chilliwilli.co.uk/ff/index.html .


%description -l pl.UTF-8
f*ckf*ckb**b to interpreter języka f*ckf*ck napisany w C++.

Język f*ckf*ck jest opisany pod
http://www.chilliwilli.co.uk/ff/index.html .

%prep
%setup -q

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install ffb $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/*
