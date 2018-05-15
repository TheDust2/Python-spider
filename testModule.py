# -*- coding:UTF-8 -*-
'''
Created on 2018年4月22日

@author: The Dust
'''
import requests    
import urllib
    
if __name__ == "__main__":
    url = "http://img2d.123rf.com.cn/168nwm/irochka/irochka0912/irochka091200008.jpg"
    r = requests.get(url) 
    with open("demo3.jpg", "wb") as code:
        code.write(r.content)
   
    urllib.urlretrieve(url, "demo3.jpg")
    pass

