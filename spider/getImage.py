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
import config_default       #config文件
#import chardet
#chardet.detect(str) #判断字符编码方式

hostNo = HOST_SCCNN_IMG             #网站源
configs = config_default.configs
THUM_DIR = configs['image_storge_path']['thumb_dir']
        
class GetImageInfo(object):
    def __init__(self, title = u'风景', imageNum = 100, choice = GET_THUMB_IMG , hostNo = HOST_123RF_IMG):
        self.title = title                      #爬取图片的主题
        self.imageNum = imageNum                #限定爬取数量
        #self.pageNum = 10                        #爬取网页数
        self.choice = choice                    #爬取文件的选择（如图片有预览或原图）
        self.hostNo = hostNo
        self.LOG = mylog()                      #自定义日志类生成一个实例
        self.PR = ParseR(self.LOG)              #自定义parseRegulation类生成一个实例
        self.urls = self.getUrls(self.title, self.hostNo)
        self.items = self.spiderImg(self.hostNo, self.urls, nums =self.imageNum)#根据url获取数据
        #self.pipelines(self.items)
        #self.pipelines(self.items)              #输出爬取的数据
            
    #获取待访问网站的urls, 
    def getUrls(self, title, hostNo, pageNum = 100):
        urls = []
        for i in range(pageNum):
            if hostNo == HOST_SCCNN_IMG:
                url = self.getHost(HOST_SCCNN_IMG) + '/search/%s/%d.html' %(title, i+1)
            elif hostNo == HOST_123RF_IMG:
                url = self.getHost(HOST_123RF_IMG) + '/search.php?keyword=%s&page=%d' %(title, i+1)
            elif hostNo == HOST_NIPIC_IMG:
                url = self.getHost(HOST_NIPIC_IMG) + '/?q=%s&k=2&page=%d' %(title, i+1)
            self.LOG.info(u'Python 拼接 URL:%s 成功' % url)
            urls.append(url)    
        return urls

    def spiderImg(self, hostNo , urls, nums = 100): 
        images = []
        getNum = 0
        for url in urls:
            if(getNum < nums):
                if hostNo == HOST_SCCNN_IMG:
                    images.extend(self.PR.parseSCCNN(url, GET_THUMB_IMG))
                elif hostNo == HOST_123RF_IMG:
                    images.extend(self.PR.parse123RF(url, GET_THUMB_IMG))
                elif hostNo == HOST_NIPIC_IMG:
                    images.extend(self.PR.parseNIPIC(url, GET_THUMB_IMG))
                getNum = len(images)
            else:
                return images[:nums]
            
    #获取配置文件中的host
    def getHost(self, hostNo):
        global configs
        if hostNo == HOST_SCCNN_IMG:
            host = configs['imagehost']['sccnn_base']
        elif hostNo == HOST_123RF_IMG:
            host = configs['imagehost']['123rf_base']
        elif hostNo == HOST_NIPIC_IMG:
            host = configs['imagehost']['nipic_base']
        return host
    
    def pipelines(self, items):
        try:
            x = 0
            for item in items:
                name = THUM_DIR + '/%s.jpg' % x 
                urllib.urlretrieve(item.thumburl, name)
                x += 1
        except:
            self.LOG.info(u'Python 下载 图片:%s 成功' % name)
        else:
            self.LOG.error(u'Python 下载 图片:%s 失败' % name)
            
if __name__ == "__main__":
    GI = GetImageInfo()
    pass
