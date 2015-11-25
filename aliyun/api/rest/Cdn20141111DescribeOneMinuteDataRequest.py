'''
Created by auto_sdk on 2015.06.23
'''
from aliyun.api.base import RestApi
class Cdn20141111DescribeOneMinuteDataRequest(RestApi):
	def __init__(self,domain='cdn.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.DataTime = None
		self.DomainName = None

	def getapiname(self):
		return 'cdn.aliyuncs.com.DescribeOneMinuteData.2014-11-11'
