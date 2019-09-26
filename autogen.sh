#!/bin/sh
libtoolize --force
aclocal
autoheader
automake --force-missing --add-missing
autoconf
autoreconf --install --force
