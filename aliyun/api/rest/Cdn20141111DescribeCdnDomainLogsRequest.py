'''
Created by auto_sdk on 2015.06.23
'''
from aliyun.api.base import RestApi
class Cdn20141111DescribeCdnDomainLogsRequest(RestApi):
	def __init__(self,domain='cdn.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.DomainName = None
		self.LogDay = None

	def getapiname(self):
		return 'cdn.aliyuncs.com.DescribeCdnDomainLogs.2014-11-11'
