# revision 24995
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-solarsystem
# catalog-date 2012-01-01 19:16:20 +0100
# catalog-license lppl
# catalog-version 0.12
Name:		texlive-pst-solarsystem
Version:	0.12
Release:	5
Summary:	Plot the solar system for a specific date
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-solarsystem
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-solarsystem.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-solarsystem.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-solarsystem.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package uses pstricks to produce diagrams of the visible
planets, projected on the plane of the ecliptic. It is not
possible to represent all the planets in their real
proportions, so only Mercury, Venus, Earth and Mars have their
orbits in correct proportions and their relative sizes are
observed. Saturn and Jupiter are in the right direction, but
not in the correct size.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-solarsystem/pst-solarsystem.pro
%{_texmfdistdir}/tex/generic/pst-solarsystem/pst-solarsystem.tex
%{_texmfdistdir}/tex/latex/pst-solarsystem/pst-solarsystem.sty
%doc %{_texmfdistdir}/doc/generic/pst-solarsystem/Changes
%doc %{_texmfdistdir}/doc/generic/pst-solarsystem/README
%doc %{_texmfdistdir}/doc/generic/pst-solarsystem/pst-solarsystem-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-solarsystem/pst-solarsystem-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-solarsystem/pst-solarsystem-doc.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-solarsystem/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.12-1
+ Revision: 759028
- texlive-pst-solarsystem
- texlive-pst-solarsystem

