#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018年4月29日

@author: The Dust
'''
import database
#使用orm中的Model基类进行创建类
class ImageAttrs():
#__init__ 要求创建实例必须传递对应参数
#     def __init__(self, title , dscurl):
#         self.title = title      #图片主题
#         self.dscurl = dscurl    #详细描述地址
    name = None             #图片名
    title = None            #图片主题
    width = None            #图片宽度
    height = None           #图片高度
    format = None           #图片格式
    description = None      #图片描述
    descrurl = None         #图片详细描述地址
    thumburl = None         #缩略图片下载地址
    downurl = None          #图片下载地址
             
    def show(self):
        str = ''
        if self.name != None:
            str += 'name = %s' % self.name
        if self.title != None:
            str += 'title = %s' % self.title
        if self.description != None:
            str += 'description = %s' % self.description 
        if self.thumburl != None:
            str += 'thumburl = %s' % self.thumburl
        if self.descrurl != None:
            str += 'descrurl = %s' % self.descrurl
        if self.downurl != None:
            str += 'downurl = %s' % self.downurl
        print str
 
    def save(self):
        save_sql = '''insert into image (`name`, `title`, `width`, `height`,
                                        `format`, `description`, `descrurl`,
                                        `thumburl`, `downurl`)
                                        values(?,?,?,?,?,?,?,?,?)'''
        data = (self.name, self.title, self.width, self.height, self.format,
                self.description,self.descrurl, self.thumburl, self.downurl)
        conn = database.get_conn()
        database.save(conn, save_sql, data)
        
    def getOneFromDB(self):
        pass
#     @property
#     def name(self):
#         return self._score
#  
#     @name.setter
#     def name(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value

if __name__ == "__main__":
#     img = ImageAttrs()
#     img.title = 1
#     print img.title
    pass
