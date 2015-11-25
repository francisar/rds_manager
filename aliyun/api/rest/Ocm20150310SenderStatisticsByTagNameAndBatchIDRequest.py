'''
Created by auto_sdk on 2015.06.23
'''
from aliyun.api.base import RestApi
class Ocm20150310SenderStatisticsByTagNameAndBatchIDRequest(RestApi):
	def __init__(self,domain='ocm.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.BatchID = None
		self.DateTime = None
		self.FromAddress = None
		self.TagName = None

	def getapiname(self):
		return 'ocm.aliyuncs.com.SenderStatisticsByTagNameAndBatchID.2015-03-10'
