Summary:	Menu converter and editor for various Window Managers
Summary(pl.UTF-8):   Konwerter menu oraz edytor dla wielu zarządców okien
Name:		menushki
Version:	1.0
Release:	1
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://dl.sourceforge.net/menushki/%{name}-%{version}.tar.gz
# Source0-md5:	fceed87938e5adfad7bc67a5374d6d8b
Patch0:		%{name}-ncurses.patch
URL:		http://menushki.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Menushki is a console menu converter and editor for various X window
managers. Currently works with KDE, GNOME, IceWM, BlackBox,
Enlightenment and WindowMaker menu.

%description -l pl.UTF-8
Menushki jest konwerterem i edytorem menu dla różnych zarządców okien
dla X. Aktualnie współpracuje z menu KDE, GNOME, IceWMa, BlackBoksa,
Enlightenmenta oraz WindowMakera.

%prep
%setup -q
%patch0 -p1

%build
cd ktools-1.1
	rm -f missing
	%{__aclocal}
	%{__autoconf}
	automake -a -c
cd ..

rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO ChangeLog
%attr(755,root,root) %{_bindir}/menushki
