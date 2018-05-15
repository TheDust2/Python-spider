#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018年4月29日

@author: The Dust
'''
from mylog import MyLog as mylog
from parseRegulation import ParseRegulation as ParseR
from constants import  *    #常量配置
import urllib
import urllib2
import os
import config_default       #config文件
from spider import model
#import chardet
#chardet.detect(str) #判断字符编码方式

hostNo = HOST_SCCNN_IMG             #网站源
configs = config_default.configs
THUM_DIR = configs['image_storge_path']['thumb_dir']
pageNum = 0
imageNum = 0
global_images = []
        
class GetImageInfo(object):
    def __init__(self):
        self.title = u'风景'                      #爬取图片的主题
        self.imageNum = 100                 #限定爬取数量
        #self.pageNum = 10                        #爬取网页数
        self.choice = GET_THUMB_IMG                 #爬取文件的选择（如图片有预览或原图）
        self.hostNo = HOST_123RF_IMG
        self.LOG = mylog()                      #自定义日志类生成一个实例
        self.PR = ParseR(self.LOG)              #自定义parseRegulation类生成一个实例
        #self.pipelines(self.items)
        #self.pipelines(self.items)              #输出爬取的数据
            
    def setImageNum(self, num):
        self.imageNum = num
        
    def setTitle(self, title):
        self.title = title
    #获取待访问网站的urls, 
    def getNextUrl(self):
        global pageNum 
        pageNum +=1
        if self.hostNo == HOST_SCCNN_IMG:
            url = self.getHost(HOST_SCCNN_IMG) + '/search/%s/%d.html' %(self.title, pageNum)
        elif self.hostNo == HOST_123RF_IMG:
            url = self.getHost(HOST_123RF_IMG) + '/search.php?keyword=%s&page=%d' %(self.title, pageNum)
        elif self.hostNo == HOST_NIPIC_IMG:
            url = self.getHost(HOST_NIPIC_IMG) + '/?q=%s&k=2&page=%d' %(self.title, pageNum)
        self.LOG.info(u'Python 拼接 URL:%s 成功' % url)  
        return url

    def spiderImg(self): 
        global global_images
        global imageNum
        images = []
        while(imageNum < self.imageNum):
            if self.hostNo == HOST_SCCNN_IMG:
                images.extend(self.PR.parseSCCNN(self.getNextUrl(), GET_THUMB_IMG))
            elif self.hostNo == HOST_123RF_IMG:
                images.extend(self.PR.parse123RF(self.getNextUrl(), GET_THUMB_IMG))
            elif self.hostNo == HOST_NIPIC_IMG:
                images.extend(self.PR.parseNIPIC(self.getNextUrl(), GET_THUMB_IMG))
            imageNum += len(images)
        global_images =  images[:self.imageNum]
            
    #获取配置文件中的host
    def getHost(self, hostNo):
        global configs
        if self.hostNo == HOST_SCCNN_IMG:
            host = configs['imagehost']['sccnn_base']
        elif self.hostNo == HOST_123RF_IMG:
            host = configs['imagehost']['123rf_base']
        elif self.hostNo == HOST_NIPIC_IMG:
            host = configs['imagehost']['nipic_base']
        return host
    
    def pipelines(self, items):
        name = ''
        try:
            x = 0
            for item in items:
                name = '\%d-%s.jpg' % (x , item.name)
                print 'name = '+ name
                
                f = urllib2.urlopen(item.thumburl) 
                with open("test.jpg", "wb") as code:
                    code.write(f.read())
                x += 1
        except Exception as e:
            print e
            self.LOG.error(u'Python 下载 图片:%s 失败' % name)
        else:
            self.LOG.info(u'Python 下载 图片:%s 成功' % name)
            
if __name__ == "__main__":
    GI = GetImageInfo()
    pass
