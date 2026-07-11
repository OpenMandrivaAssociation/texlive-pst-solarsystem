%global tl_name pst-solarsystem
%global tl_revision 69675

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.15
Release:	%{tl_revision}.1
Summary:	Plot the solar system for a specific date
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-solarsystem
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-solarsystem.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-solarsystem.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package uses pstricks to produce diagrams of the visible planets,
projected on the plane of the ecliptic. It is not possible to represent
all the planets in their real proportions, so only Mercury, Venus, Earth
and Mars have their orbits in correct proportions and their relative
sizes are observed. Saturn and Jupiter are in the right direction, but
not in the correct size.

