%global tl_name chs-physics-report
%global tl_revision 54512

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Physics lab reports for Carmel High School
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chs-physics-report
License:	pd cc-by-sa-3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chs-physics-report.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chs-physics-report.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package may optionally be used by students at Carmel High School in
Indiana in the United States to write physics lab reports for FW physics
courses. As many students are beginners at LaTeX, it also attempts to
simplify the report-writing process by offering macros for commonly used
notation and by automatically formatting the documents for students who
will only use TeX for mathematics and not typesetting. The package
depends on amsmath, calc, fancyhdr, geometry, graphicx, letltxmacro,
titlesec, transparent, and xcolor.

