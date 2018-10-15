#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-XML-XPath
Version  : 1.44
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/M/MA/MANWAR/XML-XPath-1.44.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MA/MANWAR/XML-XPath-1.44.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libx/libxml-xpath-perl/libxml-xpath-perl_1.42-1.debian.tar.xz
Summary  : 'Parse and evaluate XPath statements.'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-2.0 GPL-1.0
Requires: perl-XML-XPath-bin = %{version}-%{release}
Requires: perl-XML-XPath-license = %{version}-%{release}
Requires: perl-XML-XPath-man = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Path::Tiny)
BuildRequires : perl(XML::Parser)

%description
NAME
XML::XPath - a set of modules for parsing and evaluating XPath
statements
DESCRIPTION

%package bin
Summary: bin components for the perl-XML-XPath package.
Group: Binaries
Requires: perl-XML-XPath-license = %{version}-%{release}
Requires: perl-XML-XPath-man = %{version}-%{release}

%description bin
bin components for the perl-XML-XPath package.


%package dev
Summary: dev components for the perl-XML-XPath package.
Group: Development
Requires: perl-XML-XPath-bin = %{version}-%{release}
Provides: perl-XML-XPath-devel = %{version}-%{release}

%description dev
dev components for the perl-XML-XPath package.


%package license
Summary: license components for the perl-XML-XPath package.
Group: Default

%description license
license components for the perl-XML-XPath package.


%package man
Summary: man components for the perl-XML-XPath package.
Group: Default

%description man
man components for the perl-XML-XPath package.


%prep
%setup -q -n XML-XPath-1.44
cd ..
%setup -q -T -D -n XML-XPath-1.44 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/XML-XPath-1.44/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-XML-XPath
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-XML-XPath/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-XML-XPath/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.26.1/XML/XPath.pm
/usr/lib/perl5/vendor_perl/5.26.1/XML/XPath/Boolean.pm
/usr/lib/perl5/vendor_perl/5.26.1/XML/XPath/Builder.pm
/usr/lib/perl5/vendor_perl/5.26.1/XML/XPath/Expr.pm
/usr/lib/perl5/vendor_perl/5.26.1/XML/XPath/Function.pm
/usr/lib/perl5/vendor_perl/5.26.1/XML/XPath/Literal.pm
/usr/lib/perl5/vendor_perl/5.26.1/XML/XPath/LocationPath.pm
/usr/lib/perl5/vendor_perl/5.26.1/XML/XPath/Node.pm
/usr/lib/perl5/vendor_perl/5.26.1/XML/XPath/Node/Attribute.pm
/usr/lib/perl5/vendor_perl/5.26.1/XML/XPath/Node/Comment.pm
/usr/lib/perl5/vendor_perl/5.26.1/XML/XPath/Node/Element.pm
/usr/lib/perl5/vendor_perl/5.26.1/XML/XPath/Node/Namespace.pm
/usr/lib/perl5/vendor_perl/5.26.1/XML/XPath/Node/PI.pm
/usr/lib/perl5/vendor_perl/5.26.1/XML/XPath/Node/Text.pm
/usr/lib/perl5/vendor_perl/5.26.1/XML/XPath/NodeSet.pm
/usr/lib/perl5/vendor_perl/5.26.1/XML/XPath/Number.pm
/usr/lib/perl5/vendor_perl/5.26.1/XML/XPath/Parser.pm
/usr/lib/perl5/vendor_perl/5.26.1/XML/XPath/PerlSAX.pm
/usr/lib/perl5/vendor_perl/5.26.1/XML/XPath/Root.pm
/usr/lib/perl5/vendor_perl/5.26.1/XML/XPath/Step.pm
/usr/lib/perl5/vendor_perl/5.26.1/XML/XPath/Variable.pm
/usr/lib/perl5/vendor_perl/5.26.1/XML/XPath/XMLParser.pm

%files bin
%defattr(-,root,root,-)
/usr/bin/xpath

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/XML::XPath.3
/usr/share/man/man3/XML::XPath::Boolean.3
/usr/share/man/man3/XML::XPath::Builder.3
/usr/share/man/man3/XML::XPath::Literal.3
/usr/share/man/man3/XML::XPath::Node.3
/usr/share/man/man3/XML::XPath::Node::Attribute.3
/usr/share/man/man3/XML::XPath::Node::Comment.3
/usr/share/man/man3/XML::XPath::Node::Element.3
/usr/share/man/man3/XML::XPath::Node::Namespace.3
/usr/share/man/man3/XML::XPath::Node::PI.3
/usr/share/man/man3/XML::XPath::Node::Text.3
/usr/share/man/man3/XML::XPath::NodeSet.3
/usr/share/man/man3/XML::XPath::Number.3
/usr/share/man/man3/XML::XPath::PerlSAX.3
/usr/share/man/man3/XML::XPath::XMLParser.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-XML-XPath/LICENSE
/usr/share/package-licenses/perl-XML-XPath/deblicense_copyright

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xpath.1
