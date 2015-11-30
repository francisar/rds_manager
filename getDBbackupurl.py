# -*- coding: utf-8 -*-
import AliRDSapi.RDSapi
from  datetime  import  *
from common.function import *
import os
import sys
rdsapi=AliRDSapi.RDSapi.RDSapi()
DBInstanceID=''
BackUpPath='/data/rdsbackup/'+DBInstanceID+'/'
if os.path.exists(BackUpPath):
	if os.path.isdir(BackUpPath) is not True:
		print "error:"BackUpPath+" is a file"
		sys.exit(1)
else:
	os.makedirs(BackUpPath)
#print DBInstanceID,BackUpPath,datetime.now()
a=rdsapi.getRDSBackupOnedayUrl( DBInstanceID,datetime.now())
for item in a:
	#print item	
	download(item,BackUpPath)
