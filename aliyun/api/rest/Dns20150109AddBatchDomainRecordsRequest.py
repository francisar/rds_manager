'''
Created by auto_sdk on 2015.06.23
'''
from aliyun.api.base import RestApi
class Dns20150109AddBatchDomainRecordsRequest(RestApi):
	def __init__(self,domain='dns.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.Records = None

	def getapiname(self):
		return 'dns.aliyuncs.com.AddBatchDomainRecords.2015-01-09'
