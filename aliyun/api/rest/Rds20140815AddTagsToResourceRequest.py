'''
Created by auto_sdk on 2015.06.23
'''
from aliyun.api.base import RestApi
class Rds20140815AddTagsToResourceRequest(RestApi):
	def __init__(self,domain='rds.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.DBInstanceId = None
		self.Tag_1_key = None
		self.Tag_1_value = None
		self.Tag_2_key = None
		self.Tag_2_value = None
		self.Tag_3_key = None
		self.Tag_3_value = None
		self.Tag_4_key = None
		self.Tag_4_value = None
		self.Tag_5_key = None
		self.Tag_5_value = None

	def getapiname(self):
		return 'rds.aliyuncs.com.AddTagsToResource.2014-08-15'

	def getTranslateParas(self):
		return {'Tag_1_value':'Tag.1.value','Tag_3_value':'Tag.3.value','Tag_2_key':'Tag.2.key','Tag_5_value':'Tag.5.value','Tag_3_key':'Tag.3.key','Tag_1_key':'Tag.1.key','Tag_5_key':'Tag.5.key','Tag_4_value':'Tag.4.value','Tag_4_key':'Tag.4.key','Tag_2_value':'Tag.2.value'}
