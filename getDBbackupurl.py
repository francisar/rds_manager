# -*- coding: utf-8 -*-
import AliRDSapi.RDSapi
from  datetime  import  *
from common.function import *
rdsapi=AliRDSapi.RDSapi.RDSapi()
DBInstanceID=''
BackUpPath='/data/rdsbackup/'+DBInstanceID+'/'
#print DBInstanceID,BackUpPath,datetime.now()
a=rdsapi.getRDSBackupOnedayUrl( DBInstanceID,datetime.now())
for item in a:
	#print item	
	download(item,BackUpPath)
