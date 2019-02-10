%{!?directory:%define directory /usr}

Summary:	Readline Tcl extension
Name:		tclreadline
Version:	2.3.2
Release:	1
License:	BSD
Group:		Development/Languages/Tcl
Source0:	https://github.com/flightaware/tclreadline/releases/%{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}.patch
URL:		https://github.com/flightaware/tclreadline
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	readline-devel
BuildRequires:	tcl-devel >= 8.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The tclreadline package makes the GNU readline library available for
interactive Tcl shells. This includes history expansion and
file/command completion. Command completion for all Tcl/Tk commands is
provided and commmand completers for user defined commands can be
easily added. tclreadline can also be used for Tcl scripts which want
to use a shell like input interface. In this case the
::tclreadline::readline read command has to be called explicitly.

The advantage of tclreadline is that it uses the callback handler
mechanism of the GNU readline while it processes Tcl events. This way
X events from a wish GUI will processed as well as events from the
tclreadline line interface.

%package devel
Summary:        Readline Tcl extension developement files
Group:          Development/Languages/Tcl
Requires:       %{name} = %{version}-%{release}

%description devel
Readline Tcl extension developement files.

%prep
%setup -q
%patch0

%build
rm -f config/missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake} --add-missing
%configure --with-tcl=/usr/lib64 --prefix=%{directory} \
	   --exec-prefix=%{directory} \
           --libdir=%{directory}/%{_lib}/tcl

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        pkglibdir=%{directory}/%{_lib}/tcl/%{name}%{version} \
	DESTDIR="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%{directory}/%{_lib}/tcl/libtclreadline-%{version}.so
%{directory}/%{_lib}/tcl/libtclreadline.so
%{directory}/%{_lib}/tcl/%{name}%{version}
%{_mandir}/mann/*.n*

%files devel
%defattr(644,root,root,755)
%{directory}/%{_lib}/tcl/*.la
%{_includedir}/*.h
