Summary:	Menu converter and editor for various Window Managers
Summary(pl):	Konwerter menu oraz edytor dla wielu Window MenadøerÛw
Name:		menushki
Version:	1.0
Release:	1
License:	GPL v2
Group:		X11/Window Managers/Tools
Group(cs):	X11/OkennÌ manaæery/N·stroje
Group(de):	X11/Fenstermanager/Tools
Group(es):	X11/Administradores de Ventanas/Herramientas
Group(fr):	X11/Gestionnaires de fenÍtres/Outils
Group(pl):	X11/Zarz±dcy okien/NarzÍdzia
Group(pt):	X11/Gestores de Janelas/Ferramentas
Group(ru):	X11/ÔÀœŒŒŸ≈ Õ≈Œ≈ƒ÷≈“Ÿ/ÈŒ”‘“’Õ≈Œ‘Ÿ
Source0:	http://prdownloads.sourceforge.net/menushki/%{name}-%{version}.tar.gz
Patch0:		%{name}-ncurses.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel
URL:		http://menushki.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Menushki is a console menu converter and editor for various X window
managers. Currently works with KDE, GNOME, IceWM, BlackBox,
Enlightenment and WindowMaker menu.

%description -l pl
Menushki jest konwerterem i edytorem menu dla rÛønych X Window 
MenadøerÛw. Aktualnie pracuje z menu KDE, GNOME, IceWM, BlackBox,
Enlightenment oraz WindowMaker.

%prep 
%setup -q
%patch0 -p1

%build
cd ktools-1.1
	rm -f missing
	aclocal
	autoconf
	automake -a -c
cd ..

rm -f missing
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf README COPYING TODO ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/menushki
