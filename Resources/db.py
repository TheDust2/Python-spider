#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018年5月13日

@author: The Dust
'''

#db.py 主要代码，第一次执行时，把 “# create_table()”中的#去掉，执行完后，在加上
import sqlite3

def create_table():
    conn = sqlite3.connect('test.db')
    cur=conn.cursor()
    # cur=conn.cursor()
    try:
        create_tb_cmd='''
         CREATE TABLE IF NOT EXISTS student_info 
         (id INTEGER PRIMARY KEY AUTOINCREMENT, 
           name          text, 
           phone         text,
           qq            text,
           weixin        text,
           prid_school   text,
           cslt_course   text,
           cslt_from     text,
           dt            text,
           provider      text,
           note          text
          )
        '''
        #create table
        # cur.execute(create_tb_cmd)
        cur.execute(create_tb_cmd) 
        print('create table sucess') 
    except Exception as e:  
        print ("Create table failed" )
        print(e)
        pass
        # return False
    conn.commit()
    cur.close()
    conn.close()

def drop_table():  
    conn = sqlite3.connect('test.db')
    cur=conn.cursor()
    try:
        drop_cmd='''drop table student_info'''
        #create table
        cur.execute(drop_cmd)  
    except:  
        print ("drop table failed" )
        pass
        # return False
    conn.commit()
    cur.close()
    conn.close()    

def select_data():
    conn = sqlite3.connect('test.db')
    cur=conn.cursor()
    select_cmd=''' select * from student_info order by id desc'''  
    cur.execute(select_cmd)
    res = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return res

def edit_data(id):
    name_para={'id':id}
    conn = sqlite3.connect('test.db')
    cur=conn.cursor()
    select_cmd=''' select * from student_info where id=:id'''  
    cur.execute(select_cmd,name_para)
    res = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return res

def insert_data(name,phone,qq,weixin,prid_school,cslt_course,cslt_from,dt,provider,note):
    name_para={'name':name,'phone':phone,'qq':qq,'weixin':weixin,'prid_school':prid_school,\
     'cslt_course':cslt_course,'cslt_from':cslt_from,'dt':dt,'provider':provider,'note':note}
    conn = sqlite3.connect('test.db')
    cur=conn.cursor()
    insert_dt_cmd=''' 
      INSERT INTO student_info (name,phone,qq,weixin,prid_school,cslt_course,cslt_from,dt,provider,note)
      VALUES (:name,:phone,:qq,:weixin,:prid_school,:cslt_course,:cslt_from,:dt,:provider,:note)
    '''
    print(insert_dt_cmd)      
    cur.execute(insert_dt_cmd,name_para)  
    conn.commit()
    cur.close()  
    conn.close() 

def delete_data(sdt_id,name):
    name_para={'sdt_id':sdt_id,'name':name}
    conn = sqlite3.connect('test.db')
    cur=conn.cursor()
    # cur=conn.cursor()
    del_cmd=''' delete from student_info where id=:sdt_id and name=:name  '''  
    cur.execute(del_cmd,name_para)
    conn.commit()
    cur.close()
    conn.close()
 
def update_data(std_id,name,phone,qq,weixin,prid_school,cslt_course,cslt_from,dt,provider,note):
    name_para={'name':name,'phone':phone,'qq':qq,'weixin':weixin,'prid_school':prid_school,
                'cslt_course':cslt_course,'cslt_from':cslt_from,'dt':dt,'provider':provider,
                'note':note,'std_id':std_id
             }
    print(name_para)         
    conn = sqlite3.connect('test.db')
    cur=conn.cursor()
    update_cmd=''' update student_info set name=:name,phone=:phone,qq=:qq,
                 weixin=:weixin,prid_school=:prid_school,
               cslt_course=:cslt_course,cslt_from=:cslt_from,dt=:dt,
               provider=:provider,note=:note where id=:std_id '''  
    print(update_cmd)
    cur.execute(update_cmd,name_para)
    conn.commit()
    cur.close()
    conn.close()

# drop_table()
# create_table()
# name,phone,qq,weixin,prid_school,cslt_course,cslt_from,dt,provider,note

# insert_data('jonsen3','15920056968','794554422','weixin','shenzhen_school','english','shanghai','2018-03-30','tom','note')
# rs=select_data() 
# std = []
# for idt,name,phone,qq,weixin,prid_school,cslt_course,cslt_from,dt,provider,note in rs:
#     # print(idt,name,phone,qq,weixin,prid_school,cslt_course,cslt_from,dt,provider,note)
#     std.append((idt,name,phone,qq,weixin,prid_school,cslt_course,cslt_from,dt,provider,note))
# # print(std)
# for i in range(len(rs)):
#     print(std[i][0],std[i][1],std[i][2],std[i][3],std[i][4],std[i][5],std[i][6],std[i][7],std[i][8],std[i][9],std[i][10])
    # pritn(dt)
# print(rs)