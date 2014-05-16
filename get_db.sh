#!/bin/bash
set +ue
set -x
wget http://www.openwlanmap.org/db.tar.bz2
bunzip2 -c db.tar.bz2 > db.tar
tar xvf db.tar
#delemter chr(09) - tab
