#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018年5月2日

@author: The Dust
@version: 2.0
@change: 修改了仅凭借小说名拼接下载地址的不合理之处，
                采用直接获取小说url的方式，进行小说内容爬取
'''
import requests
from bs4 import BeautifulSoup
import os
import logging
import getpass
import sys

#### 定义MyLog类
class MyLog(object):
#### 类MyLog的构造函数
    def __init__(self):
        self.user = getpass.getuser()
        self.logger = logging.getLogger(self.user)
        self.logger.setLevel(logging.DEBUG)

####  日志文件名及格式
        self.logFile = sys.argv[0][0:-3] + '.log'
        self.formatter = logging.Formatter('%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s')

####  日志显示到屏幕上并输出到日志文件内
        self.logHand = logging.FileHandler(self.logFile, encoding='utf8')
        self.logHand.setFormatter(self.formatter)
        self.logHand.setLevel(logging.DEBUG)

        self.logHandSt = logging.StreamHandler()
        self.logHandSt.setFormatter(self.formatter)
        self.logHandSt.setLevel(logging.DEBUG)

        self.logger.addHandler(self.logHand)
        self.logger.addHandler(self.logHandSt)

####  日志的5个级别对应以下的5个函数
    def debug(self,msg):
        self.logger.debug(msg)

    def info(self,msg):
        self.logger.info(msg)

    def warn(self,msg):
        self.logger.warn(msg)

    def error(self,msg):
        self.logger.error(msg)

    def critical(self,msg):
        self.logger.critical(msg)
        
req_header={
'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'accept-encoding':'gzip, deflate, br',
'accept-language':'zh-CN,zh;q=0.9',
'cache-control':'max-age=0',
'cookie':'__cfduid=d29e4b3d6c46ac836785718f2d41f00ea1525363812; pgsrc=m2d.wuxiaworld.offpage.js; __auc=661641ce16326c49d5e1b170bf1; _ga=GA1.2.2000975143.1525363810; _gid=GA1.2.643505457.1525363810; m2dEnabled=true; __gads=ID=e69e9a749ee69c1b:T=1525363817:S=ALNI_MYV81WdPdX_kaFmnTzQvF9LGE_cbw; __asc=1d0f5ac216326ed0c1934ed0df5; session_depth=19; komoonaNullBids=1; sovrnNullBids=1; 152mediaNullBids=1; gumgumNullBids=1; memeglobalNullBids=1; rubiconNullBids=1; openxNullBids=1; defymediaNullBids=1; vertozNullBids=1; criteoNullBids=1; sekindoUMNullBids=1; aolNullBids=1; brealtimeNullBids=1; tripleliftNullBids=1; conversantNullBids=1; springserveANNullBids=1; rhythmoneNullBids=1; appnexusNullBids=1; sonobiNullBids=1; districtmNullBids=1; sharethroughNullBids=1; pulsepointNullBids=1; trionNullBids=1; indexExchangeNullBids=1',
'upgrade-insecure-requests':'1',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}
req_url_base = 'https://www.wuxiaworld.com'

#小说下载函数
# txt_name：小说名
# txt_translator：译者
# txt_intro：小说介绍
# txt_chapters：章节数
# section_name：章节名称
# section_para：章节正文段落
class CrawNovel():
    def __init__(self): 
        self.suburls = []
        self.mylog = MyLog()
        self.getNovelNames()
        
    def getNovel(self,novel_url):
        fo = open('Novel information', "ab+")
        try:
            completion_flag = 0
            res=requests.get(novel_url, params=req_header) 
            soups=BeautifulSoup(res.text, 'lxml')
            content=soups.find('div', attrs={'class':'section'})     
            #获取小说名
            txt_name = content.find('h4').get_text().encode('utf-8')
            print('txt_name = ' + txt_name) 
            #获取小说译者
            txt_translator = content.find('dd').get_text().encode('utf-8')
            print('txt_translator = ' + txt_translator)
            #获取小说简介
            intro_content =  content.find_all('div', attrs={'class':'fr-view'})[1]
            txt_intro = intro_content.get_text().encode('utf-8')
            print('txt_intro = ' + txt_intro)
            #获取小说所有章节信息
            allpages = content.find_all('li', attrs={'class':'chapter-item'})
            #获取小说总章页面数
            txt_chapters = len(allpages)                                                           
            #获取小说第一章页面地址
            first_page = allpages[0].find('a').attrs['href']  
            print 'The first chapter url: %s' % first_page
            #设置现在下载小说章节页面
            txt_url = first_page    
            
            #打开小说文件写入小说相关信息
            fo.write(('Name : ' + txt_name + "\r\n"))
            fo.write(('Translator : ' + txt_translator + "\r\n"))
            fo.write(('Chapters : ' + str(txt_chapters).encode('utf-8') + "\r\n"))
            fo.write(('Description : ' + txt_intro + "\r\n"))
            fo.write("\r\n\r\n")
            #进入循环，写入每章内容
            print(txt_name+" beginning downloading.")
            while(1):
                fo2 = open(txt_name + '.txt.download', "ab+")
                try:
                    print('Current url = ' +req_url_base+ txt_url)
                    #time.sleep(5)
                    r=requests.get(req_url_base+txt_url,params=req_header)#请求当前章节页面
                    soup = BeautifulSoup(r.text,"lxml")   
                    content = soup.find('div', attrs={'class':'p-15'})  
                    section_name = content.find('h4').get_text().encode('utf-8') #获取章节名称  
                    print('Section_name = ' + section_name)
                    #fo2.write((section_name + '\r\n'))
                    section_content = content.find('div',attrs={'class':'fr-view'})
                    para_ok_flag = 0
                    for string in section_content.strings:
                        fo2.write((string+'\n').encode('utf-8'))
                        para_ok_flag+=1
    
                    #获取下一章地址
                    txt_url = content.find_next('li', attrs={'class':'next pull-right'}).find('a')['href']
                    #print('Txt_url = ' + txt_url)   
                    #判断是否最后一章，当为最后一章时，会跳转至目录地址，最后一章则跳出循环               
                    if(txt_url == '#'):                                         
                        if completion_flag == 0:              
                            self.mylog.debug(u" download completion: "+txt_name) 
                        else: 
                            self.mylog.debug(u" download failed: "+txt_name)
                        break                      
                except Exception as e:
                    print('Error in craw txt section:', e)
                    self.mylog.debug(u"Novel '"+txt_name+ u"' chapter download failed.")  
                else:
                    if para_ok_flag < 5: #小于5段的篇章，基本上下载失败了
                        completion_flag = 1
                        self.mylog.info(u'download innormal graphs = %3d'%para_ok_flag+u'=======> '+txt_name +u': '+ section_name)
                    else:
                        self.mylog.info(u'already downloaded graphs = %3d' %para_ok_flag+u'======>'+txt_name + u": " +section_name )                    
                    fo2.write('\r\n\r\n')
                finally:
                    fo2.close()
        except Exception as e:
            print('Error in get info:', e)     
            try:
                self.mylog.debug(novel_url.encode('utf-8')+u" download failed.")
                os.rename(txt_name + '.txt.download', txt_name + '.txt.error')
            except Exception as e:
                print('Error in output error info:', e)     
        else: #下载完成后无异常则更改名字
            os.rename(txt_name + '.txt.download', txt_name + '.txt')  
        finally:
            fo.close() 
            
    def getNovelNames(self):    
        r=requests.get('https://www.wuxiaworld.com/tag/completed',params=req_header)
        soup = BeautifulSoup(r.text,"html.parser")     
        contents = soup.find_all('a', attrs={'class':'text-white'})  
        for content in contents:   
            self.suburls.append(content.attrs['href'])
        print self.suburls
       
def test():
    fo2 = open('test.txt.download', "ab+")
    try:
        r=requests.get('https://www.wuxiaworld.com/novel/blue-phoenix/bp-chapter-0',params=req_header)#请求当前章节页面
        soup = BeautifulSoup(r.text,"lxml")     
        content = soup.find('div', attrs={'class':'p-15'}) 
        section_name = content.find('h4').get_text().encode('utf-8') #获取章节名称  
        print('Section_name = ' + section_name)
        fo2.write((section_name + '\n'))
        section_content = content.find('div',attrs={'class':'fr-view'})
        for string in section_content.strings:
            if string == ' ' or string == '':
                print 'string is none'
            else:     
                print string
                fo2.write((string+'\n').encode('utf-8'))
        
        fo2.write('\r\n')
    except Exception as e:
        print e
    finally:       
        fo2.close()
    #获取下一章地址
#     txt_url = header.find_next('li', attrs={'class':'next pull-right'}).find('a')['href']
    #print('Txt_url = ' + txt_url)   
    #判断是否最后一章，当为最后一章时，会跳转至目录地址，最后一章则跳出循环                               
            
if __name__ == "__main__":
    spider = CrawNovel()
    run_flag = 3
    if run_flag == 1:
        for url in spider.suburls:
            spider.getNovel(req_url_base+url)
    elif run_flag == 2:
        test()
    elif run_flag == 3:    
        spider.getNovel(req_url_base+'/novel/seoul-stations-necromancer')
    pass
