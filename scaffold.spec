Summary:	GNOME based Development Environment
Summary(pl.UTF-8):	Środowisko programistyczne dla GNOME
Name:		scaffold
Version:	0.1.0
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/GNOME/sources/scaffold/0.1/%{name}-%{version}.tar.bz2
# Source0-md5:	e88c1afa35c42a8baea255ba1387d55b
BuildRequires:	GConf2-devel
BuildRequires:	gdl-devel >= 0.4.0
BuildRequires:	gnome-build-devel >= 0.1.0
BuildRequires:	gnome-vfs2-devel >= 2.3.5
BuildRequires:	libbonoboui-devel >= 2.3.3
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel >= 2.3.3
BuildRequires:	libxml2-devel >= 2.5.8
BuildRequires:	vte-devel >= 0.11.0
Requires(post):	/sbin/ldconfig
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scaffold (formerly known as anjuta2) is a GNOME based Integrated
Development Environment (IDE).

%description -l pl.UTF-8
Scaffold (formalnie znany jako anjuta2) jest zintegrowanym
środowiskiem programistycznym (IDE) dla GNOME.

%package devel
Summary:	Header files for scaffold
Summary(pl.UTF-8):	Pliki nagłówkowe scaffold
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for scaffold.

%description devel -l pl.UTF-8
Pliki nagłówkowe scaffold.

%package static
Summary:	Static scaffold library
Summary(pl.UTF-8):	Statyczna biblioteka scaffold
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static scaffold library.

%description static -l pl.UTF-8
Statyczna biblioteka scaffold.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/*.a

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%gconf_schema_install

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO docs/tool-tutorial.txt
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/plugins/lib*.so*
%{_libdir}/%{name}/plugins/lib*.la
%{_libdir}/%{name}/plugins/*.plugin
%{_datadir}/%{name}
%{_sysconfdir}/gconf/schemas/*
%{_datadir}/application-registry/*
%{_desktopdir}/*.desktop
%{_datadir}/gnome-2.0/ui/*
%{_mandir}/man1/*
%{_datadir}/mime-info/*
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
