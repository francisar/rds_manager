'''
Created by auto_sdk on 2015.06.23
'''
from aliyun.api.base import RestApi
class Rds20140815CreateDatabaseForInnerRequest(RestApi):
	def __init__(self,domain='rds.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.AccountName = None
		self.AccountPassword = None
		self.AccountPrivilege = None
		self.CharacterSetName = None
		self.DBDescription = None
		self.DBInstanceId = None
		self.DBName = None
		self.ownerId = None
		self.resourceOwnerAccount = None
		self.resourceOwnerId = None

	def getapiname(self):
		return 'rds.aliyuncs.com.CreateDatabaseForInner.2014-08-15'
