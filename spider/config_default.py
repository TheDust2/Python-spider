#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018年5月1日

@author: The Dust
'''

configs = {
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'database': 'awesome'
    },
    'session': {
        'secret': 'AwEsOmE'
    },
    'imagehost': {
        'sccnn_base': 'so.sccnn.com',
        '123rf_base': 'www.123rf.com.cn',
        'nipic_base': 'soso.nipic.com',
        'bing_base': 'cn.bing.com/images/search?'
    },
    'image_storge_path': {
        'thumb_dir': 'F:\Creation\spider_downloadfile\thumb_Image',
        'natural_dir': 'F:\Creation\spider_downloadfile\original_Image'
    }
}

if __name__ == "__main__":
    #print configs['db']
    pass
