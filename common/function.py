# -*- coding: utf-8 -*-
'''
#=============================================================================
#
#     FileName: function.py
#         Desc: 功能函数
#
#       Author:francis
#
#      Created: 2014-8-17
#      Version: 1.0.0
#      History:
#               1.0.0 | francis
#
#=============================================================================
'''
import urllib2,re,string
from time import sleep
import md5
import os
import json
########################
##
##
import time 
########################
 
# (1)function  get_md5 ：获取一个文件的MD5值
def get_md5(full_filename):
    f=file(full_filename,'rb')
    return md5.new(f.read()).hexdigest()
 
# (2)function  check_md5：判断一个文件的MD5值是否正确
def check_md5(correct_md5,full_filename):
    my_md5= get_md5(full_filename)
    if(my_md5.upper()==correct_md5.upper()):
        return True
    else:
        return False 
    
# (3)function  getItemValueFromURL：从网页上获取关键项item对应的值,不存在返回None
def getItemValueFromURL(urlpath,item):
    urlpath=urlpath
    item=item
    request=urllib2.Request(urlpath)
    html_str=urllib2.urlopen(request).read()
    #print html_sr
    jsonDict =json.loads(html_str)
    for key in jsonDict:
        if(key==item):
            return jsonDict[item]
    return None
 
# (4)function downloadfile :用于下载文件
 
def downloadfile(file_url,filename,download_path):
    try:
        request = urllib2.Request(file_url) 
        f=open(download_path+filename,'wb')
        start_time=time.time()
        #print 'time stamp is : ',time.time()
        print start_time 
        size =0
        speed=0
        data_lines = urllib2.urlopen(request).readlines()
        #data = urllib2.urlopen(request).read() 
        for data in data_lines:
            f.write(data)
            size = size + len(data)
            dural_time=float(time.time()) - float(start_time)
            if(dural_time>0):
                speed = float(size)/float(dural_time)/(1000*1000)
                while(speed >1):
                    print 'speed lagger than 1MB/s , sleep(0.1).....'
                    print 'sleep .....'
                    sleep(0.1)
                    dural_time=float(time.time()) - float(start_time)
                    speed = float(size)/float(dural_time)/(1000*1000)
        print 'total time is : ',dural_time ,'seconds'
        print 'size is       : ',size ,'KB'
        print 'speed is      : ',speed ,'MB/s'  
    except Exception,e:
        print 'download error: ',e
        return False
    return True
 
#(5) download: 调用上述函数下载文件
def download(path,download_path,attempt=5):
    
    #1.init parameter :
    path=path
    download_path=download_path
    attempt=attempt
    #2. download 
      
    # download and check md5
    while(attempt>0):
        #
        attempt=attempt-1
        #.get download parameter
	re_str = '.*(.*gz)\?'
	#re_pat = re.compile(re_str)
	#print path
	filename= os.path.basename(path)
        filename=   re.search(re_str,filename).group(0)
	filename = filename.rstrip('\?')
        #correct_md5=getItemValueFromURL(path,"md5")
        #filepath=getItemValueFromURL(path,"filepath")
	print filename
        if(filename==None or path==None):
           print " download parameter not correct "
           continue
        #download
        print 'begin the ',5-attempt,'time download'
        if( (downloadfile(path,filename,download_path)) ==False ):
            print "download failed ..continue"
            continue
        #check_md5
        #if(check_md5(correct_md5,download_path+filename)):
            #print "download ok ...."
        return True
    return False
 

