%define name python-gtksourceview
%define version 2.10.1
%define release  9
%define oname pygtksourceview

Summary: Gtksourceview bindings for Python
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/%oname/%{oname}-%{version}.tar.bz2
License: LGPLv2+
Group: Development/Python
Url: http://www.gnome.org
BuildRequires:  docbook-style-xsl
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(gtksourceview-2.0)
BuildRequires:  pkgconfig(pygtk-2.0)

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


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 2.10.1-4mdv2011.0
+ Revision: 667936
- mass rebuild

* Mon Nov 01 2010 Funda Wang <fwang@mandriva.org> 2.10.1-3mdv2011.0
+ Revision: 591296
- rebuild for py 2.7

* Tue Apr 27 2010 Christophe Fergeau <cfergeau@mandriva.com> 2.10.1-2mdv2010.1
+ Revision: 539616
- rebuild so that shared libraries are properly stripped again

* Sun Apr 18 2010 Götz Waschk <waschk@mandriva.org> 2.10.1-1mdv2010.1
+ Revision: 536394
- update to new version 2.10.1

* Sun Mar 28 2010 Götz Waschk <waschk@mandriva.org> 2.10.0-1mdv2010.1
+ Revision: 528549
- update to new version 2.10.0

* Tue Feb 23 2010 Götz Waschk <waschk@mandriva.org> 2.9.2-1mdv2010.1
+ Revision: 509946
- update to new version 2.9.2

* Mon Jan 11 2010 Götz Waschk <waschk@mandriva.org> 2.9.1-2mdv2010.1
+ Revision: 489561
- new version
- update build deps
- update build deps

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 2.8.0-1mdv2010.0
+ Revision: 446727
- update to new version 2.8.0

* Tue Aug 18 2009 Götz Waschk <waschk@mandriva.org> 2.7.0-1mdv2010.0
+ Revision: 417527
- update to new version 2.7.0

* Sat Mar 21 2009 Götz Waschk <waschk@mandriva.org> 2.6.0-1mdv2009.1
+ Revision: 360084
- update to new version 2.6.0

* Thu Mar 05 2009 Götz Waschk <waschk@mandriva.org> 2.5.0-1mdv2009.1
+ Revision: 348782
- update to new version 2.5.0
- fix source URL

* Mon Jan 26 2009 Funda Wang <fwang@mandriva.org> 2.4.0-3mdv2009.1
+ Revision: 333700
- link against python

* Fri Dec 26 2008 Adam Williamson <awilliamson@mandriva.org> 2.4.0-2mdv2009.1
+ Revision: 319536
- rebuild with python 2.6

* Sat Sep 20 2008 Götz Waschk <waschk@mandriva.org> 2.4.0-1mdv2009.0
+ Revision: 286117
- new version

* Mon Aug 11 2008 Götz Waschk <waschk@mandriva.org> 2.3.0-1mdv2009.0
+ Revision: 270641
- new version
- bump deps
- update license

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.2.0-2mdv2009.0
+ Revision: 225131
- rebuild

* Mon Mar 10 2008 Götz Waschk <waschk@mandriva.org> 2.2.0-1mdv2008.1
+ Revision: 183502
- new version
- bump deps

* Tue Feb 05 2008 Götz Waschk <waschk@mandriva.org> 2.1.1-1mdv2008.1
+ Revision: 162645
- new version
- bump deps

* Tue Jan 22 2008 Götz Waschk <waschk@mandriva.org> 2.1.0-1mdv2008.1
+ Revision: 156138
- disable parallel build
- fix buildrequires
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Sep 17 2007 Götz Waschk <waschk@mandriva.org> 2.0.0-1mdv2008.0
+ Revision: 89091
- new version
- bump dep

* Wed Sep 12 2007 Götz Waschk <waschk@mandriva.org> 1.90.5-1mdv2008.0
+ Revision: 84736
- new version
- bump deps

* Tue Aug 28 2007 Götz Waschk <waschk@mandriva.org> 1.90.4-1mdv2008.0
+ Revision: 72605
- new version
- bump deps

* Wed Aug 01 2007 Götz Waschk <waschk@mandriva.org> 1.90.3-1mdv2008.0
+ Revision: 57429
- new version
- fix module name
- bump deps

* Wed Jul 04 2007 Götz Waschk <waschk@mandriva.org> 1.90.2-1mdv2008.0
+ Revision: 47959
- new version
- bump deps

* Mon Jun 25 2007 Götz Waschk <waschk@mandriva.org> 1.90.1-1mdv2008.0
+ Revision: 44018
- Import python-gtksourceview



* Mon Jun 25 2007 Götz Waschk <waschk@mandriva.org> 1.90.1-1mdv2008.0
- initial package
