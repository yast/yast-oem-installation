#
# spec file for package yast2-db2setup (Version 1.0)
#
# Copyright (c) 2004 SUSE LINUX AG, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://www.suse.de/feedback/
#

# norootforbuild
# neededforbuild  perl-Digest-SHA1 perl-gettext yast2-devel-packages yast2-perl-bindings yast2-users

BuildRequires: aaa_base acl attr bash bind-utils bison bzip2 coreutils cpio cpp cracklib cvs cyrus-sasl db devs diffutils e2fsprogs file filesystem fillup findutils flex gawk gdbm-devel glibc glibc-devel glibc-locale gpm grep groff gzip info insserv kbd less libacl libattr libgcc libselinux libstdc++ libxcrypt m4 make man mktemp module-init-tools ncurses ncurses-devel net-tools netcfg openldap2-client openssl pam pam-modules patch permissions popt procinfo procps psmisc pwdutils rcs readline sed strace syslogd sysvinit tar tcpd texinfo timezone unzip util-linux vim zlib zlib-devel autoconf automake binutils curl dejagnu doxygen expect gcc gdbm gettext libtool liby2util liby2util-devel openslp openslp-devel perl perl-Digest-SHA1 perl-XML-Writer perl-gettext popt-devel rpm tcl update-desktop-files yast2 yast2-core yast2-core-devel yast2-devtools yast2-packagemanager yast2-packagemanager-devel yast2-perl-bindings 

Name:         yast2-db2setup
Version:      1.0
Release:      1
License:      GPL
Group:        System/YaST
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Source0:      yast2-db2setup-1.0.tar.bz2
prefix:		/usr
Requires:     yast2 yast2-installation 
Summary:      YaST2 - DB2 UDB Setup

%description
Installation of DB2.



Authors:
--------
    Frank Balzer <frank.balzer@suse.com>


%prep
%setup

%build
make -f Makefile.sles9


%install
rm -rf $RPM_BUILD_ROOT;
install -d -m 755 ${RPM_BUILD_ROOT}{/usr/share/YaST2/theme/SuSELinux/icons/48x48/apps,/usr/share/YaST2/theme/SuSELinux/icons/32x32/apps,/usr/share/YaST2/theme/SuSELinux/icons/22x22/apps,/usr/share/YaST2/clients,/usr/share/YaST2/modules,/usr/share/YaST2/bin,/usr/share/applications/YaST2,/var/adm/fillup-templates}
install -m 644 stinger48.png ${RPM_BUILD_ROOT}/usr/share/YaST2/theme/SuSELinux/icons/48x48/apps/stinger.png
install -m 644 stinger32.png ${RPM_BUILD_ROOT}/usr/share/YaST2/theme/SuSELinux/icons/32x32/apps/stinger.png
install -m 644 stinger22.png ${RPM_BUILD_ROOT}/usr/share/YaST2/theme/SuSELinux/icons/22x22/apps/stinger.png
install -m 644 db2.desktop   ${RPM_BUILD_ROOT}/usr/share/applications/YaST2/db2.desktop
install -m 755 yast2_db2setup ${RPM_BUILD_ROOT}/usr/share/YaST2/bin/yast2_db2setup
install -m 644 db2_install.ycp ${RPM_BUILD_ROOT}/usr/share/YaST2/clients/db2_install.ycp
install -m 644 DB2DATA.ycp   ${RPM_BUILD_ROOT}/usr/share/YaST2/modules/DB2DATA.ycp
install -m 644 DB2DATA.ybc   ${RPM_BUILD_ROOT}/usr/share/YaST2/modules/DB2DATA.ybc
install -m 644 DB2GUI.ycp   ${RPM_BUILD_ROOT}/usr/share/YaST2/modules/DB2GUI.ycp
install -m 644 DB2GUI.ybc   ${RPM_BUILD_ROOT}/usr/share/YaST2/modules/DB2GUI.ybc
install -m 644 DB2INSTALL.ycp  ${RPM_BUILD_ROOT}/usr/share/YaST2/modules/DB2INSTALL.ycp
install -m 644 DB2INSTALL.ybc  ${RPM_BUILD_ROOT}/usr/share/YaST2/modules/DB2INSTALL.ybc
install -m 644 yast_db2_ese_template.rsp ${RPM_BUILD_ROOT}/var/adm/fillup-templates/yast_db2_ese_template.rsp
%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
/usr/share/YaST2/clients/db2_install.ycp
/usr/share/YaST2/bin/yast2_db2setup
/usr/share/YaST2/theme/SuSELinux/icons/48x48/apps/stinger.png
/usr/share/YaST2/theme/SuSELinux/icons/32x32/apps/stinger.png
/usr/share/YaST2/theme/SuSELinux/icons/22x22/apps/stinger.png
/usr/share/YaST2/modules/DB2*.*
/var/adm/fillup-templates/yast_db2_ese_template.rsp
%{prefix}/share/applications/YaST2/db2.desktop

%changelog -n yast2-db2setup
* Thu Jul 30 2004 - frank.balzer@suse.com
- initial version
