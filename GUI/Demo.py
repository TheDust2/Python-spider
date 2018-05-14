#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018年5月13日

@author: The Dust
'''
import ttk 
from Tkinter import *

class AutoDownloader(object):
    def __init__(self, object):
        self.lb1=LabelFrame(object, width=200, height=160, text='选项')  
        self.lb1.grid(row=0,column=0,padx=10)  
        self.colors =  ['图片', '论文', '小说']# 定义几个资源类型  
        
        def radCall(self):  # 单选按钮回调函数,就是当单选按钮被点击会执行该函数  
            radSel = self.radVar.get()  
            print radSel 
            
        self.radVar = IntVar()  # 通过IntVar() 获取单选按钮value参数对应的值  
        self.radVar.set(99)  
        for col in range(3):  
            curRad = Radiobutton(self.lb1, text=self.colors[col], variable=self.radVar,value=col,command=radCall)# 当该单选按钮被点击时，会触发参数command对应的函数  
            curRad.place(x=0,y=col*35)  # 参数sticky对应的值参考复选框的解释      
    
        self.lb2 = LabelFrame(object, width=200, height=240, text='条件')  
        self.lb2.grid(row=1, column=0)  
        
        self.label1 = Label(self.lb2, text='主题：').place(x=0, y=0)
        self.label2 = Label(self.lb2, text='数量：').place(x=0, y=35)
        self.input1 = Entry(self.lb2).place(x=40, y=0)
        self.input2 = Entry(self.lb2).place(x=40, y=35)
        
        
        self.lb3 = LabelFrame(object, width=400, height=400, text='预览')  
        self.lb3.grid(row=0, column=1,rowspan=2)  
        # Treeview  
        self.tree = ttk.Treeview(self.lb3, selectmode='browse')  
        self.vsb =Scrollbar(self.lb3,width=400, orient="vertical",command=self.tree.yview)  
        self.tree.configure(yscrollcommand=self.vsb.set)  
        self.vsb.place(x=-5, y=0, height=370)  
        self.tree["columns"] = ("1", "2")  
        self.tree['show'] = 'headings'  
        self.tree.column("1", width=100, anchor='c')  
        self.tree.column("2", width=100, anchor='c')  
        self.tree.heading("1", text="Account")  
        self.tree.heading("2", text="Type")  
        for i in range(30):  
            self.tree.insert("", 'end', text="L1", values=(i, "Best"))  
        self.tree.place(x=10, y=0,width=370,height=370)  
        
        
        self.fr=Frame(height = 40,width = 600)  
        self.fr.grid(row=2, column=0,columnspan=2, pady=10)  
  
        def clickMe():  
            print "click"
        self.action1 = ttk.Button(self.fr, text="开始嗅探", command=clickMe)  # 创建一个按钮, text   
        self.action1.place(x=0,y=0) 
        
        self.action2 = ttk.Button(self.fr, text="全部下载", command=clickMe)  # 创建一个按钮, text   
        self.action2.place(x=220,y=0) 
        
def center_window(root, width, height):  
    screenwidth = root.winfo_screenwidth()  
    screenheight = root.winfo_screenheight()  
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)  
    #print(size)  
    root.geometry(size) 
  
if __name__ == "__main__":
    root = Tk()  
    root.title("自动化资源嗅探下载器")   
    center_window(root, 650, 460)
    app = AutoDownloader(root)  
    root.mainloop() 
    pass
