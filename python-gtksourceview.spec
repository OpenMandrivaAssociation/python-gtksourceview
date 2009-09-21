%define name python-gtksourceview
%define version 2.8.0
%define release %mkrel 1
%define oname pygtksourceview

Summary: Gtksourceview bindings for Python
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/%oname/%{oname}-%{version}.tar.bz2
License: LGPLv2+
Group: Development/Python
Url: http://www.gnome.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtksourceview-devel >= 2.3.0
BuildRequires: pygtk2.0-devel
BuildRequires: libxslt-proc docbook-style-xsl

%description
These are the python bindings for the version 2 of the
GtkSourceView library.

%package devel
Group: Development/Python
Summary: Files required to build applications with %name
Requires: %name = %version

%description devel
These are the python bindings for the version 2 of the
GtkSourceView library.


%prep
%setup -q -n %oname-%version

%build
%configure2_5x
%make PYTHON_LIBS="-lpython%{py_ver}"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot%py_platsitedir/gtksourceview2.la
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README NEWS AUTHORS
%py_platsitedir/gtksourceview2.so

%files devel
%defattr(-,root,root)
%doc ChangeLog
%_libdir/pkgconfig/*.pc
%_datadir/gtk-doc/html/pygtksourceview2/
%_datadir/pygtk/2.0/defs/gtksourceview2.defs
