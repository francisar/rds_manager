'''
Created by auto_sdk on 2015.06.23
'''
from aliyun.api.base import RestApi
class Odps20141215DescribeOdpsServiceRequest(RestApi):
	def __init__(self,domain='odps.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)

	def getapiname(self):
		return 'odps.aliyuncs.com.DescribeOdpsService.2014-12-15'
