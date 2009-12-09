%define name	latexmk
%define version 4.11
%define release %mkrel 1

Summary:	Perl script for automating LaTeX document compilation
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-411.zip
License:	GPLv2
Group:		Publishing
Url:		http://www.phys.psu.edu/~collins/software/latexmk-jcc/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	perl
Requires:	tetex-latex

%description
Latexmk completely automates the process of compiling a LaTeX
document.  Essentially, it is like a specialized relative of
the general make utility, but one which determines dependencies
automatically and has some other very useful features.  In its
basic mode of operation latexmk is given the name of the
primary source file for a document, and it issues the
appropriate sequence of commands to generate a .dvi, .ps, .pdf
and/or hardcopy version of the document.

%prep
%setup -q -c %{name}-%{version}

%install
%__rm -rf %{buildroot}

%__install -d %{buildroot}%{_bindir}
%__install -d %{buildroot}%{_mandir}/man1

%__install -m 755 %{name}.pl %{buildroot}%{_bindir}/%{name}
%__install -m 755 %{name}.1 %{buildroot}%{_mandir}/man1/

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES COPYING README latexmk.pdf latexmk.txt example_rcfiles
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*
