#!/bin/sh
#
# Oracle installer agent
#
# This agent runs the oracle installer.
#

# Parameters:
# <installer>	Path and name to the installer
#

par1=$1

if test "$par1" = "" ; then
 echo "usage: $0 <installer>"
 exit 1
fi

echo -n "locking for the installer ..."

if [ -a $par1 ] ; then
 # the installer exists.
 # we continue with the installation.
 #
 echo "ok"
 echo "Installer is $par1";

 echo "Invoking root shell that is required for the oracle commands"
 xterm -title "Root Command Shell" &

 echo "runnig rcorarun stop"
 rcorarun stop
 echo "running rcorarun start"
 rcorarun start
 echo -n "calling installer ..."
 $par1
 echo "ok"
 exit 0
fi

# the installer does not exists.
# we exit with code 1.
#

echo " failed"
echo "the installer $par1 does not exist"
exit 1
