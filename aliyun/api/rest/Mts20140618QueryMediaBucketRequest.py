'''
Created by auto_sdk on 2015.06.23
'''
from aliyun.api.base import RestApi
class Mts20140618QueryMediaBucketRequest(RestApi):
	def __init__(self,domain='mts.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)

	def getapiname(self):
		return 'mts.aliyuncs.com.QueryMediaBucket.2014-06-18'
