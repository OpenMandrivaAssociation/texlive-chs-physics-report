Name:		texlive-chs-physics-report
Version:	54512
Release:	2
Summary:	Physics lab reports for Carmel High School
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chs-physics-report
License:	pd cc-by-sa-3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chs-physics-report.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chs-physics-report.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package may optionally be used by students at Carmel High
School in Indiana in the United States to write physics lab
reports for FW physics courses. As many students are beginners
at LaTeX, it also attempts to simplify the report-writing
process by offering macros for commonly used notation and by
automatically formatting the documents for students who will
only use TeX for mathematics and not typesetting. The package
depends on amsmath, calc, fancyhdr, geometry, graphicx,
letltxmacro, titlesec, transparent, and xcolor.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/chs-physics-report
%doc %{_texmfdistdir}/doc/latex/chs-physics-report

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
