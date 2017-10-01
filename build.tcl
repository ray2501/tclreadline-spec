#!/usr/bin/tclsh

set arch "x86_64"
set base "tclreadline-2.2.0"

set var [list wget https://github.com/flightaware/tclreadline/archive/v2.2.0.tar.gz -O $base.tar.gz]
exec >@stdout 2>@stderr {*}$var

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES
file copy -force tclreadline-2.2.0.patch build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb tclreadline.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove our source code
file delete $base.tar.gz

