'''
Created by auto_sdk on 2015.06.23
'''
from aliyun.api.base import RestApi
class Rds20140815DescribeVpcZoneNosRequest(RestApi):
	def __init__(self,domain='rds.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.Region = None
		self.ZoneId = None

	def getapiname(self):
		return 'rds.aliyuncs.com.DescribeVpcZoneNos.2014-08-15'
