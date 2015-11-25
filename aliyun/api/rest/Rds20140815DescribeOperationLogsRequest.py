'''
Created by auto_sdk on 2015.06.23
'''
from aliyun.api.base import RestApi
class Rds20140815DescribeOperationLogsRequest(RestApi):
	def __init__(self,domain='rds.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.DBInstanceId = None
		self.DBInstanceUseType = None
		self.EndTime = None
		self.PageNumber = None
		self.PageSize = None
		self.SearchKey = None
		self.StartTime = None

	def getapiname(self):
		return 'rds.aliyuncs.com.DescribeOperationLogs.2014-08-15'
