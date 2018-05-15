#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018年4月30日

@author: The Dust
'''

import urllib2
import urllib
from bs4  import BeautifulSoup
from model import ImageAttrs as image
from constants import  *

class ParseRegulation:
    def __init__(self, log):
        self.log = log
        
    def getOriginSCCNNURL(self, descrurl):
        htmlContent = self.getResponseContent(descrurl)
        soup = BeautifulSoup(htmlContent, 'lxml')
        content = soup.find('div', attrs={'class':'down'}) if soup != None else None
        downbox = content.find('div', attrs={'id':'downbox'}) if content != None else None
        downurl = downbox.find_next('a').attrs['href'] if downbox != None else None
        self.log.info(u'Python 返回DownloadURL:%s 成功' % downurl)
        return downurl
        
    
    def parseSCCNN(self, url, choice = GET_THUMB_IMG): 
        items = []
        self.log.info(u'Python 请求 URL:%s ' % url)
        url = u'http://' + urllib.pathname2url(url.encode('utf-8'))  #将带中文的url 转换为 %十六进制 形式
        htmlContent = self.getResponseContent(url)
        soup = BeautifulSoup(htmlContent, 'lxml')
        try:
            content = soup.find('table', attrs={'style':'BORDER-COLLAPSE: collapse'})
            tagsli = content.find_all('img',  attrs={'border':'0'}) if content != None else None
            for tag in tagsli:
                item = image()
                item.descrurl = tag.find_parent('a', attrs={'target':'_blank'}).attrs['href']  if tag != None else None
                item.thumburl = tag.attrs['src']  if tag != None else None
                item.description = tag.attrs['alt']  if tag != None else None
                if(choice == GET_REAL_IMG):#需要获取原图则再次解析下载原图下载地址
                    item.downurl = self.getOriginNIPICURL(item.descrurl)
                    if item.downurl != None:
                        items.append(item)
                else:
                    items.append(item)
            self.log.info(u'Python 解析URL:%s 完成' % url)
        except:
            self.log.error(u'Python 解析 URL:%s 错误' % url)
            return None
        else:
            return items     
         
    def parse123RF(self, url, choice = GET_THUMB_IMG):
        items = []
        self.log.info(u'Python 请求 URL:%s ' % url)
        url = u'http://' + url #123rf不需要将中文转化为16进制表示
        htmlContent = self.getResponseContent(url)
        soup = BeautifulSoup(htmlContent, 'lxml')
        try:
            tagsli = soup.find_all('img',  attrs={'class':'uitooltip'})
            for tag in tagsli:
                item = image()
                item.descrurl = tag.find_parent('a').attrs['href']  if tag != None else None
                item.thumburl = tag.attrs['src']  if tag != None else None
                item.name = tag.attrs['picid']
                if(choice == GET_REAL_IMG):#需要获取原图则再次解析下载原图下载地址
                    item.downurl = 'restrict'
                    items.append(item)
                else:
                    items.append(item)
                item.show()
            self.log.info(u'Python 解析URL:%s 完成' % url)
        except:
            self.log.error(u'Python 解析 URL:%s 错误' % url)
            return None
        else:
            return items     
    
    def parseNIPIC(self, url, choice = GET_THUMB_IMG):
        items = []
        self.log.info(u'Python 请求 URL:%s ' % url)
        url = u'http://' + url #nipic不需要将中文转化为16进制表示
        htmlContent = self.getResponseContent(url)
        soup = BeautifulSoup(htmlContent, 'lxml')
        try:
            tagsli = soup.find_all('img',  attrs={'class':'lazy'})
            for tag in tagsli:
                item = image()
                item.descrurl = tag.find_parent('a').attrs['href']  if tag != None else None
                item.thumburl = tag.attrs['data-original']  if tag != None else None
                item.description =  tag.attrs['alt'] if tag != None else None
                if(choice == GET_REAL_IMG):#需要获取原图则再次解析下载原图下载地址
                    item.downurl = 'restrict'
                    items.append(item)
                else:
                    items.append(item)
                item.show()
                item.save()
            self.log.info(u'Python 解析URL:%s 完成' % url)
        except:
            self.log.error(u'Python 解析 URL:%s 错误' % url)
            return None
        else:
            return items 
        
    def getResponseContent(self, url):
        try:
            response = urllib2.urlopen(url.encode('utf-8'))
        except:
            self.log.error(u'Python 返回 URL:%s 数据失败' % url)
        else:
            self.log.info(u'Python 返回 URL:%s 数据成功' % url)
            return response.read()


if __name__ == "__main__":
#     url = 'so.sccnn.com/search/风景/1.html'
#     print urllib.pathname2url(url)
    pass
