#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018年5月1日

@author: The Dust
'''
# import database
# 
# class Field(object):
#     def __init__(self, name, column_type):
#         self.name = name
#         self.column_type = column_type
#     def __str__(self):
#         return '<%s:%s>' % (self.__class__.__name__, self.name)
# 
# class StringField(Field):
#     def __init__(self, name):
#         super(StringField, self).__init__(name, 'varchar(100)')
# 
# class IntegerField(Field):
#     def __init__(self, name):
#         super(IntegerField, self).__init__(name, 'bigint')
# 
# class ModelMetaclass(type):
# 
#     def __new__(cls, name, bases, attrs):
#         if name=='Model':
#             return type.__new__(cls, name, bases, attrs)
#         print('Found model: %s' % name)
#         mappings = dict()
#         for k, v in attrs.iteritems():
#             if isinstance(v, Field):
#                 print('Found mapping: %s ==> %s' % (k, v))
#                 mappings[k] = v
#         for k in mappings.iterkeys():
#             attrs.pop(k)
#         attrs['__mappings__'] = mappings # 保存属性和列的映射关系
#         attrs['__table__'] = name # 假设表名和类名一致
#         return type.__new__(cls, name, bases, attrs)
# 
# class Model(dict):
#     __metaclass__ = ModelMetaclass
# 
#     def __init__(self, **kw):
#         super(Model, self).__init__(**kw)
# 
#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Model' object has no attribute '%s'" % key)
# 
#     def __setattr__(self, key, value):
#         self[key] = value
#     
#    
#     @database.with_connection    
#     def save(self):
#         fields = []
#         params = []
#         args = []
#         for k, v in self.__mappings__.iteritems():
#             fields.append(v.name)
#             params.append('?')
#             args.append(getattr(self, k, None))
#         sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
#         
#         #使用了with_connection装饰器,global 会在函数进入前被赋值 
#         global _db_ctx
#         cursor = None
#         sql = sql.replace('?', '%s')
#         print('SQL: %s, ARGS: %s' % (sql, args))
#         try:
#             cursor = _db_ctx.connection.cursor()
#             cursor.execute(sql, args)
#             r = cursor.rowcount
#             if _db_ctx.transactions==0:
#                 # no transaction enviroment:
#                 print('auto commit')
#                 _db_ctx.connection.commit()
#             return r
#         finally:
#             if cursor:
#                 cursor.close()
#         #print('SQL: %s' % sql)
#         #print('ARGS: %s' % str(args))
# 
# if __name__ == "__main__":
#     pass
