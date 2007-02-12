%define		modname htmlcorrector
Summary:	Drupal HTML corrector
Summary(pl.UTF-8):   Moduł poprawiający HTML dla Drupala
Name:		drupal-mod-%{modname}
Version:	4.6.0
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://drupal.org/files/projects/%{modname}-%{version}.tar.gz
# Source0-md5:	076ec184722bc10ed233d87a3ce284a8
URL:		http://drupal.org/project/htmlcorrector
# for %%banner
#BuildRequires:	rpmbuild(macros) >= 1.194
Requires:	drupal >= 4.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_drupaldir	%{_datadir}/drupal
%define		_moddir		%{_drupaldir}/modules

%description
This is a HTML correcting module. The filter scans the input, builds
up a list of open tags and closes them when needed.

Note that it does not validate the document according to the HTML
specifications, but merely ensures that any tags are properly nested.

%description -l pl.UTF-8
To jest moduł poprawiający HTML. Filtr przeszukuje wejście, tworzy
listę otwartych znaczników i zamyka je tam, gdzie trzeba.

Należy zauważyć, że ten moduł nie sprawdza poprawności dokumentu
względem specyfikacji HTML, a jedynie upewnia się, że wszystkie
znaczniki są poprawnie zagnieżdżone.

%prep
%setup -q -n %{modname}
rm -f LICENSE.txt # GPL v2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_moddir}

install *.module $RPM_BUILD_ROOT%{_moddir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%{_moddir}/*.module
