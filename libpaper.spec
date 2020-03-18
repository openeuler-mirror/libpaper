Name:           libpaper
Version:        1.1.24
Release:        25
Summary:        Library for handling paper characteristics
License:        GPLv2
URL:            http://packages.qa.debian.org/libp/libpaper.html
Source0:        http://ftp.debian.org/debian/pool/main/libp/libpaper/%{name}_%{version}+nmu4.tar.gz
patch0: libpaper-useglibcfallback.patch
patch1: libpaper-file-leak.patch
 
BuildRequires:  gcc, libtool, gettext, gawk

%description
The libpaper paper-handling library automates recognition of many different 
paper types and sizes for programs that need to deal with printed output.

%package        devel
Summary:        Development files for using libpaper
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the development files.

%package        help
Summary:        Documents for libpaper
Buildarch:      noarch
Requires:       man

%description    help
Man pages and other related documents for libpaper.

%prep
%autosetup -n %{name}-%{version}+nmu4 -p1
libtoolize

%build
touch AUTHORS NEWS
aclocal
autoconf
automake -a
%configure --disable-static
%disable_rpath
%make_build

%install
%make_install
rm $RPM_BUILD_ROOT%{_libdir}/*.la
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
echo '# Simply write the paper name. See papersize(5) for possible values' > $RPM_BUILD_ROOT%{_sysconfdir}/papersize
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/libpaper.d
for i in cs da de es fr gl hu it ja nl pt_BR sv tr uk vi; do
	mkdir -p $RPM_BUILD_ROOT%{_datadir}/locale/$i/LC_MESSAGES/;
	msgfmt debian/po/$i.po -o $RPM_BUILD_ROOT%{_datadir}/locale/$i/LC_MESSAGES/%{name}.mo;
done
%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%doc ChangeLog README
%license COPYING
%config(noreplace) %{_sysconfdir}/papersize
%dir %{_sysconfdir}/libpaper.d
%{_bindir}/paperconf
%{_libdir}/libpaper.so.1.1.2
%{_libdir}/libpaper.so.1
%{_sbindir}/paperconfig

%files devel
%{_includedir}/paper.h
%{_libdir}/libpaper.so

%files help
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_mandir}/man3/*

%changelog
* Wed Mar 18 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.1.24-25
- fix memory leark and bugfix
* Thu Jan 05 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.1.24-24
- remove useless patch

* Thu Sep 05 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.1.24-23
- Package init
