'''
Created by auto_sdk on 2015.06.23
'''
from aliyun.api.base import RestApi
class Rkvstore20150101DeleteInstanceRequest(RestApi):
	def __init__(self,domain='r-kvstore.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.InstanceId = None

	def getapiname(self):
		return 'r-kvstore.aliyuncs.com.DeleteInstance.2015-01-01'
