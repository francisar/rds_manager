'''
Created by auto_sdk on 2015.06.23
'''
from aliyun.api.base import RestApi
class Rds20140815CheckAccountNameAvailableRequest(RestApi):
	def __init__(self,domain='rds.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.AccountName = None
		self.DBInstanceId = None
		self.resourceOwnerAccount = None

	def getapiname(self):
		return 'rds.aliyuncs.com.CheckAccountNameAvailable.2014-08-15'
