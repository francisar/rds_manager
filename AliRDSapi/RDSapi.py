# -*- coding: utf-8 -*-
'''
#=============================================================================
#
#     FileName: RDSapi.py
#         Desc: aliyunRDS的API
#
#       Author:francis
#
#      Created: 2014-8-17
#      Version: 1.0.0
#      History:
#               1.0.0 | francis
#
#=============================================================================
'''
import aliyun.api
from  datetime  import  *
import time
import json
from config import *

class RDSapi(object):
	__aliyunapi = None
	#__AccessKeyId = ''
	#__AccessKeySecret = ''
	#__Format = ''
	#__apiurl = ''
	#__apiport = ''
	def __init__(self,AccessKeyId=ACCESSKEYID,AccessKeySecret=ACCESSKEYSECRET,Format=FORMAT,apiurl=APIURL,apiport=APIPORT):
		#self.__AccessKeyId = AccessKeyId
		#self.__AccessKeySecret = AccessKeySecret
		#self.__Format = Format
		#self.__apiurl = apiurl
		#self.__apiport = apiport
		self.__aliyunapi = aliyun.api.Rds20140815DescribeDBInstancesRequest(apiurl,apiport)
		self.__aliyunapi.set_app_info(aliyun.appinfo(AccessKeyId,AccessKeySecret))
		self.__aliyunapi.Format = Format
	def __formatTimeM(self,Time):
		Time = Time
		return Time.strftime( u'%Y-%m-%dT%H:%MZ' )
	def __formatTimeS(self,Time):
		Time = Time
		return Time.strftime( u'%Y-%m-%dT%H:%M:%SZ' )
	def __formatTimeM_UTC(self,Time):
		Time = Time - timedelta(hours=8)
		return Time.strftime( u'%Y-%m-%dT%H:%MZ' )
	def __formatTimeS_UTC(self,Time):
		Time = Time - timedelta(hours=8)
		return Time.strftime( u'%Y-%m-%dT%H:%M:%SZ' )
	def getRDSBackup(self,DBInstanceId,StartTime,EndTime,PageNumber=1,BackupMode='Automated',PageSize=100):
		self.__aliyunapi.Action = 'DescribeBackups'
		self.__aliyunapi.DBInstanceId = DBInstanceId
		#self.__aliyunapi.StartTime = StartTime
		#self.__aliyunapi.EndTime = EndTime
		self.__aliyunapi.BackupMode = BackupMode
		self.__aliyunapi.PageNumber = PageNumber
		self.__aliyunapi.PageSize = PageSize
		self.__aliyunapi.StartTime = self.__formatTimeM_UTC(StartTime)
		self.__aliyunapi.EndTime = self.__formatTimeM_UTC(EndTime)
		print self.__aliyunapi
		rawret = self.__aliyunapi.getResponse()
		print  rawret
		jsonret = json.dumps(rawret)
		dictret = json.loads(jsonret)
		return dictret
		#try:
		#	rawret = self.__aliyunapi.getResponse()
		#	print rawret
		#	jsonret = json.dumps(rawret)
		#	dictret = json.loads(jsonret)
			#print dictret["TotalRecordCount"]
		#	return dictret
		#except Exception,e:
		#	print(e)
	def getRDSBackupAllList(self,DBInstanceId,StartTime,EndTime,PageSize=100):
		#print StartTime
		ret = self.getRDSBackup(DBInstanceId,StartTime,EndTime,PageSize=PageSize)
		#print StartTime
		print ret
		TotalRecordCount = ret["TotalRecordCount"]
		TotalPage = int(TotalRecordCount)/PageSize + 1
		List = []
		for i in range(1,TotalPage+1):
			dictret = self.getRDSBackup(DBInstanceId,StartTime,EndTime,PageNumber=i,PageSize=PageSize)
			#print dictret["Items"]["Backup"]
			List = dictret["Items"]["Backup"]+List
		return List
	def getRDSBackupAllUrl(self,DBInstanceId,StartTime,EndTime):
		BackupList = self.getRDSBackupAllList(DBInstanceId,StartTime,EndTime)
		UrlList = []
		for item in BackupList:
			UrlList.append(item["BackupDownloadURL"])
		return UrlList
	def getRDSBackupOnedayUrl(self,DBInstanceId,Date):
		BackupList = self.getRDSBackupAllList(DBInstanceId,Date-timedelta(days=1),Date)
		UrlList = []
		for item in BackupList:
			UrlList.append(item["BackupDownloadURL"])
		return UrlList
			
	#def getRDSBackupUrlList(self,DBInstanceId,StartTime,EndTime):
		
			

    #SQLItemList= fjson["SQLItems"]["SQLItem"]
    #for SQLItem in SQLItemList:
#	print SQLItem['ExecuteTime'],SQLItem['SQLText'],SQLItem['ReturnRowCounts'],"|",SQLItem[u'ReturnRowCounts'],"|",SQLItem[u'TotalExecutionTimes']

    #print(f)
#except Exception,e:
#    print(e)
#rdsapi=RDSapi()
#print  rdsapi.getRDSBackupURL( u'rds54q393jmuwm6hqw83',datetime.now()-timedelta(days=1),datetime.now())   
