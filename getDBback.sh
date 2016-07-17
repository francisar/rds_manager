#!/bin/bash
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin
if $(dirname $0 &>/dev/null) ; then

     CUR_DIR=$(cd $(dirname $0) && pwd)
else
     CUR_DIR=$(pwd)
fi
export PWD=$CUR_DIR
export LANG=en_US.UTF-8
/usr/bin/python $CUR_DIR/getDBbackupurl.py 
