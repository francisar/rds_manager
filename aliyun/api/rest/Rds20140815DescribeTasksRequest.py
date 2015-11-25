'''
Created by auto_sdk on 2015.06.23
'''
from aliyun.api.base import RestApi
class Rds20140815DescribeTasksRequest(RestApi):
	def __init__(self,domain='rds.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.DBInstanceId = None
		self.EndTime = None
		self.Page = None
		self.PageSize = None
		self.StartTime = None
		self.Status = None
		self.TaskAction = None
		self.ownerId = None
		self.resourceOwnerAccount = None
		self.resourceOwnerId = None

	def getapiname(self):
		return 'rds.aliyuncs.com.DescribeTasks.2014-08-15'
