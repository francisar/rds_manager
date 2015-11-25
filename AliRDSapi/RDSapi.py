# -*- coding: utf-8 -*-


import aliyun.api
from  datetime  import  *
import time
import json
from config import *

class RDSapi(object):
	__aliyunapi = None
	def __init__(self,AccessKeyId=ACCESSKEYID,AccessKeySecret=ACCESSKEYSECRET,Format=FORMAT,apiurl=APIURL,apiport=APIPORT):
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
	def getRDSBackupAllList(self,DBInstanceId,StartTime,EndTime,PageSize=100):
		ret = self.getRDSBackup(DBInstanceId,StartTime,EndTime,PageSize=PageSize)
		TotalRecordCount = ret["TotalRecordCount"]
		TotalPage = int(TotalRecordCount)/PageSize + 1
		List = []
		for i in range(1,TotalPage+1):
			dictret = self.getRDSBackup(DBInstanceId,StartTime,EndTime,PageNumber=i,PageSize=PageSize)
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