%define _disable_rebuild_configure 1
%define _disable_lto 1

%define url_ver %(echo %{version}|cut -d. -f1,2)
%define oname pygtksourceview

Summary:	Gtksourceview bindings for Python
Name:		python2-gtksourceview
Version:	2.10.1
Release:	18
License:	LGPLv2+
Group:		Development/Python
Url:		http://www.gnome.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pygtksourceview/%{url_ver}/%{oname}-%{version}.tar.bz2
BuildRequires:	docbook-style-xsl
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gtksourceview-2.0)
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(python2)
%rename python-gtksourceview

%description
These are the python bindings for the version 2 of the
GtkSourceView library.

%package devel
Group:		Development/Python
Summary:	Files required to build applications with %{name}
Requires:	%{name} = %{version}-%{release}

%description devel
These are the python bindings for the version 2 of the
GtkSourceView library.

%prep
%setup -qn %oname-%{version}

%build
%define _disable_ld_no_undefined 1
export PYTHON=%{__python2}
%configure
%make PYTHON_LIBS="-lpython%{py2_ver}"

%install
%makeinstall_std

%files
%doc README NEWS AUTHORS
%{py2_platsitedir}/gtksourceview2.so

%files devel
%doc ChangeLog
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gtk-doc/html/pygtksourceview2/
%{_datadir}/pygtk/2.0/defs/gtksourceview2.defs

