'''
Created by auto_sdk on 2015.06.23
'''
from aliyun.api.base import RestApi
class Ecs20140526AuthorizeSecurityGroupEgressRequest(RestApi):
	def __init__(self,domain='ecs.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.DestCidrIp = None
		self.DestGroupId = None
		self.DestGroupOwnerAccount = None
		self.IpProtocol = None
		self.NicType = None
		self.Policy = None
		self.PortRange = None
		self.Priority = None
		self.RegionId = None
		self.SecurityGroupId = None

	def getapiname(self):
		return 'ecs.aliyuncs.com.AuthorizeSecurityGroupEgress.2014-05-26'
