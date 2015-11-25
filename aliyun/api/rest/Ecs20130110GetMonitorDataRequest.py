'''
Created by auto_sdk on 2015.06.23
'''
from aliyun.api.base import RestApi
class Ecs20130110GetMonitorDataRequest(RestApi):
	def __init__(self,domain='ecs.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.InstanceId = None
		self.PageNumber = None
		self.PageSize = None
		self.RegionId = None
		self.Time = None

	def getapiname(self):
		return 'ecs.aliyuncs.com.GetMonitorData.2013-01-10'
