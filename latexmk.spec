%define srcversion %(echo %{version} | sed -e 's/\\.//g')

Summary:	Perl script for automating LaTeX document compilation
Name:		latexmk
Version:	4.39
Release:	2
Source0:	http://www.phys.psu.edu/~collins/software/latexmk-jcc/%{name}-%{srcversion}.zip
License:	GPLv2
Group:		Publishing
Url:		http://www.phys.psu.edu/~collins/software/latexmk-jcc/
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

%__install -d %{buildroot}%{_bindir}
%__install -d %{buildroot}%{_mandir}/man1

%__install -m 755 %{name}.pl %{buildroot}%{_bindir}/%{name}
%__install -m 755 %{name}.1 %{buildroot}%{_mandir}/man1/

%clean

%files
%doc CHANGES COPYING README latexmk.pdf latexmk.txt example_rcfiles
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*
