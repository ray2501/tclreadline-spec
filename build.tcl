#!/usr/bin/tclsh

set arch "x86_64"
set base "tclreadline-2.3.8"

set var2 [list git clone https://github.com/flightaware/tclreadline.git $base]
exec >@stdout 2>@stderr {*}$var2

cd $base

set var2 [list git checkout cfd5080c6433fd61bbcf54f1552eb0723f9a8154]
exec >@stdout 2>@stderr {*}$var2

set var2 [list git reset --hard]
exec >@stdout 2>@stderr {*}$var2

file delete -force .git

cd ..

set var2 [list tar czvf ${base}.tar.gz $base]
exec >@stdout 2>@stderr {*}$var2

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES
file copy -force $base.patch build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb tclreadline.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove our source code
file delete -force $base
file delete $base.tar.gz

