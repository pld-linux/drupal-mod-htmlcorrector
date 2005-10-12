%define		modname htmlcorrector
Summary:	Drupal HTML corrector
Summary(pl):	Modu³ poprawiaj±cy HTML dla Drupala
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

%description -l pl
To jest modu³ poprawiaj±cy HTML. Filtr przeszukuje wej¶cie, tworzy
listê otwartych znaczników i zamyka je tam, gdzie trzeba.

Nale¿y zauwa¿yæ, ¿e ten modu³ nie sprawdza poprawno¶ci dokumentu
wzglêdem specyfikacji HTML, a jedynie upewnia siê, ¿e wszystkie
znaczniki s± poprawnie zagnie¿d¿one.

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
