'''
Created by auto_sdk on 2015.06.23
'''
from aliyun.api.base import RestApi
class Rds20130528ModifySecurityIpsRequest(RestApi):
	def __init__(self,domain='rds.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.DBInstanceId = None
		self.SecurityIps = None

	def getapiname(self):
		return 'rds.aliyuncs.com.ModifySecurityIps.2013-05-28'
