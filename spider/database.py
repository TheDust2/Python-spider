#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018年5月1日

@author: The Dust
'''
import sqlite3
import os
#from functools import wraps
#global var
#数据库文件绝句路径
DB_FILE_PATH = os.path.dirname(os.path.realpath(__file__)) + '\image.db'
#是否打印sql
SHOW_SQL = True


# # 持有数据库连接的上下文对象:
# class _DbCtx():
#     def __init__(self):
#         self.connection = None
#         self.transactions = 0
# 
#     def is_init(self):
#         return not self.connection is None
# 
#     def init(self):
#         self.connection = get_conn(DB_FILE_PATH)
#         self.transactions = 0
# 
#     def cleanup(self):
#         self.connection.cleanup()
#         self.connection = None
# 
#     def cursor(self):
#         return self.connection.cursor()
# 
# _db_ctx = _DbCtx()
# 
# class _ConnectionCtx(object):
#     def __enter__(self):
#         global _db_ctx
#         self.should_cleanup = False
#         if not _db_ctx.is_init():
#             _db_ctx.init()
#             self.should_cleanup = True
#         return self
# 
#     def __exit__(self, exctype, excvalue, traceback):
#         global _db_ctx
#         if self.should_cleanup:
#             _db_ctx.cleanup()
# 
# def connection():
#     return _ConnectionCtx()
# 
# #wraps 则可以将原函数对象的指定属性复制给包装函数对象 
# #默认有 __module__、__name__、__doc__,或者通过参数选择
# def with_connection(func):
#     @wraps(func)
#     def _wrapper(*args, **kw):
#         with connection():
#             return func(*args, **kw)
#     return _wrapper


def get_conn():
    conn = sqlite3.connect(DB_FILE_PATH)
    if os.path.exists(DB_FILE_PATH) and os.path.isfile(DB_FILE_PATH):
        print ('数据库于硬盘上:[{}]'.format(DB_FILE_PATH))
        return conn
    else:
        conn = None
        print ('数据库于内存上:[:memory:]')
        return sqlite3.connect(':memory:')
    pass

def get_cursor(conn):
    '''该方法是获取数据库的游标对象'''
    if conn is not None:
        return conn.cursor()
    else:
        return get_conn('').cursor()
    pass

def close_all(conn, cu):
    '''关闭数据库游标对象和数据库连接对象'''
    try:
        if cu is not None:
            cu.close()
    finally:
        if conn is not None:
            conn.close()
    pass

def drop_table(conn, table):
    '''如果表存在,则删除表及表中的数据，慎用！'''
    if table is not None and table != '':
        sql = 'DROP TABLE IF EXISTS ' + table
        if SHOW_SQL:
            print('执行sql:[{}]'.format(sql))
        cu = get_cursor(conn)
        cu.execute(sql)
        conn.commit()
        print('删除数据库表[{}]成功!'.format(table))
        close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))
    pass
     
def create_table(conn, sql):
    '''创建数据库表'''
    if sql is not None and sql !='':
        cu = get_cursor(conn)
        if SHOW_SQL:
            print('执行sql:[{}]'.format(sql))
        cu.execute(sql)
        conn.commit()
        print('创建数据库表[student]成功!')
        close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))
    pass
  
def save(conn, sql, data):  
    if sql is not None and sql != '':
        if data is not None:
            cu = get_cursor(conn)
            if SHOW_SQL:
                print('执行sql:[{}],参数:[{}]'.format(sql, data))
            cu.execute(sql, data)
            conn.commit()
        close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))        
    pass

def saveall(conn, sql, data):
    '''插入数据'''
    if sql is not None and sql != '':
        if data is not None:
            cu = get_cursor(conn)
            for d in data:
                if SHOW_SQL:
                    print('执行sql:[{}],参数:[{}]'.format(sql, d))
                cu.execute(sql, d)
                conn.commit()
            close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))        
    pass

def fetchall(conn, sql):
    '''查询所有数据'''
    if sql is not None and sql != '':
        cu = get_cursor(conn)
        if SHOW_SQL:
            print('执行sql:[{}]'.format(sql))
            cu.execute(sql)
            r = cu.fetchall()
            if len(r) > 0:
                for e in range(len(r)):
                    print(r[e])
    else:
        print('the [{}] is empty or equal None!'.format(sql))
    pass

def update(conn, sql, data):
    '''更新数据'''
    if sql is not None and sql != '':
        if data is not None:
            cu = get_cursor(conn)
            for d in data:
                if SHOW_SQL:
                    print('执行sql:[{}],参数:[{}]'.format(sql, d))
                    cu.execute(sql, d)
                    conn.commit()
                close_all(conn, cu)
        else:
            print('the [{}] is empty or equal None!'.format(sql))
    pass

def delete(conn, sql, data):
    '''删除数据'''
    if sql is not None and sql != '':
        if data is not None:
            cu = get_cursor(conn)
            for d in data:
                if SHOW_SQL:
                    print('执行sql:[{}],参数:[{}]'.format(sql, d))
                cu.execute(sql, d)
                conn.commit()
                close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))
    pass
    
    
def create_image_table():
    '''创建数据库表'''
    image_table_sql = '''CREATE TABLE `image` (
                            `id` INTEGER PRIMARY KEY AUTOINCREMENT,
                            `name` text DEFAULT NULL,
                            `title` text DEFAULT NULL,
                            `width` int DEFAULT NULL,
                            `height` int DEFAULT NULL,
                            `format` char(10) DEFAULT NULL,
                            `description` text DEFAULT NULL,
                            `descrurl` text DEFAULT NULL,
                            `thumburl` text DEFAULT NULL,
                            `downurl` text DEFAULT NULL
                            )'''
    conn = get_conn()
    create_table(conn, image_table_sql)
    
def drop_image_table():
    conn = get_conn()
    drop_table(conn, 'image')
    
def save_test():
    save_sql = 'insert into image (`title`, `downurl`) values(?,?)'
    data = [('1', 'http:1'), ('2','http:2')]
    conn = get_conn()
    saveall(conn, save_sql, data)

def init():
    global DB_FILE_PATH
    DB_FILE_PATH = DB_FILE_PATH + '\image.db'
    pass

if __name__ == "__main__":
    init()
    #create_image_table()
    save_test()
    #drop_image_table()
    pass
