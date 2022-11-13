Name:		texlive-pst-solarsystem
Version:	45097
Release:	1
Summary:	Plot the solar system for a specific date
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-solarsystem
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-solarsystem.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-solarsystem.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/dvips/pst-solarsystem
%{_texmfdistdir}/tex/generic/pst-solarsystem
%{_texmfdistdir}/tex/latex/pst-solarsystem
%doc %{_texmfdistdir}/doc/generic/pst-solarsystem

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
