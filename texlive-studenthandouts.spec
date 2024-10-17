Name:		texlive-studenthandouts
Version:	43516
Release:	2
Summary:	Management and styling of student handout projects
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/studenthandouts
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/studenthandouts.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/studenthandouts.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package can be used to generate a single master document
that contains a set of individual student handouts. The package
has two main functions. First, it provides a simple framework
for organizing handout source code, and supplies a set of
import management tools for selectively importing a subset of
the handouts into the master document. Selective import is
convenient when compilation of all of the handouts is
unnecessary, for example when working on a new handout. As a
secondary feature, the package defines a basic visual style for
handouts. This style can be easily changed.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/studenthandouts
%doc %{_texmfdistdir}/doc/latex/studenthandouts

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
