# -*- coding:UTF-8 -*-
'''
Created on 2018年4月22日

@author: The Dust
'''

from wsgiref.simple_server import make_server
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']


class User(object):
    def __init__(self, username, password):
        self._username =  username
        self._password = password
     
    @property
    def username(self):
        return self._username
     
    @username.setter
    def username(self, username):
        self._username = username
     
    @property
    def password(self):
        return self._password
     
    @password.setter
    def password(self, password):
        self._password = password
     
    def __enter__(self):
        print('auto do something before statements body of with executed')
        return self
     
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('auto do something after statements body of with executed')
        print('exc_type:', exc_type)
        print('exc_val:', exc_val)
        print('exc_tb:', exc_tb)
        return True
    
if __name__ == "__main__":
    #L2 = sorted(L, key=by_name)
    #print(L2)
    #httpd = make_server('', 8000, application)
    #print('Serving HTTP on port 8000...')
    # 开始监听HTTP请求:
    #httpd.serve_forever()
    boy = User('shouke', 'shouke2014')
    print(boy.password)
     
    with User('shouke', '2014') as user:
        print(user.password)
    
    
    12/0
     
    print('---------end-----------')
    pass
