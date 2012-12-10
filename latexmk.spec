%define name	latexmk
%define version 4.30a
%define srcversion %(echo %{version} | sed -e 's/\\.//g')
%define release %mkrel 1

Summary:	Perl script for automating LaTeX document compilation
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.phys.psu.edu/~collins/software/latexmk-jcc/%{name}-%{srcversion}.zip
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


%changelog
* Fri Dec 23 2011 Lev Givon <lev@mandriva.org> 4.30a-1mdv2011.0
+ Revision: 744849
- Update to 4.30a.

* Wed Aug 17 2011 Lev Givon <lev@mandriva.org> 4.26-1
+ Revision: 695041
- Update to 4.26.

* Thu Jul 14 2011 Lev Givon <lev@mandriva.org> 4.25-1
+ Revision: 690028
- Update to 4.25.

* Fri May 13 2011 Lev Givon <lev@mandriva.org> 4.24-1
+ Revision: 673994
- Update to 4.24.
- Update to 4.22e

* Wed Jan 05 2011 Lev Givon <lev@mandriva.org> 4.22-1mdv2011.0
+ Revision: 628839
- Update to 4.22.

* Mon Jan 03 2011 Lev Givon <lev@mandriva.org> 4.21-1mdv2011.0
+ Revision: 628247
- Update to 4.21.

* Thu Aug 05 2010 Lev Givon <lev@mandriva.org> 4.18-1mdv2011.0
+ Revision: 566473
- Update to 4.18.
- Update to 4.16a.

* Tue Jan 19 2010 Lev Givon <lev@mandriva.org> 4.13a-1mdv2010.1
+ Revision: 493631
- Update to 4.13a.

* Sat Jan 02 2010 Frederik Himpe <fhimpe@mandriva.org> 4.12-2mdv2010.1
+ Revision: 485195
- Really update to version 4.12

* Sat Jan 02 2010 Frederik Himpe <fhimpe@mandriva.org> 4.12-1mdv2010.1
+ Revision: 485191
- update to new version 4.12

* Wed Dec 09 2009 Lev Givon <lev@mandriva.org> 4.11-1mdv2010.1
+ Revision: 475638
- Update to 4.11.

* Thu Sep 24 2009 Lev Givon <lev@mandriva.org> 4.10-1mdv2010.0
+ Revision: 448471
- import latexmk


