%global tl_name studenthandouts
%global tl_revision 43516

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Management and styling of student handout projects
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/studenthandouts
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/studenthandouts.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/studenthandouts.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package can be used to generate a single master document that
contains a set of individual student handouts. The package has two main
functions. First, it provides a simple framework for organizing handout
source code, and supplies a set of import management tools for
selectively importing a subset of the handouts into the master document.
Selective import is convenient when compilation of all of the handouts
is unnecessary, for example when working on a new handout. As a
secondary feature, the package defines a basic visual style for
handouts. This style can be easily changed.

