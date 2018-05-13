#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018年5月13日

@author: The Dust
'''

#stjy.py
# import tkinter as tkt
from tkinter import  *
from tkinter import Tk, Scrollbar, Frame,ttk
import tkinter
from tkinter.ttk import Treeview
import time
import db as sql
from tkinter import messagebox


MENU_ITEMS = [ '常用', '帮助']
MENU_CY_ITEMS = ['查看','录入','编辑','导出数据','exit']
MENU_HELP_ITEMS=['about','help']

def select_action():

    frame=Frame(root)
    frame.place(x=0, y=10)
    # frame.grid(row=0,column=0)
    #滚动条

    scrollBar = tkinter.Scrollbar(frame)
    scrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    # scrollBar.grid(row=0,column=1)
    scrollBar_sp=tkinter.Scrollbar(frame,orient='horizontal')
    # scrollBar_sp.pack(side=tkinter.RIGHT,fill=tkinter.X)
    #Treeview组件，11列，显示表头，带垂直滚动条
    tree = Treeview(frame,height=500,
                          columns=('c1', 'c2', 'c3', 'c4', 'c5', 'c6','c7','c8','c9','c10','c11'),
                          show="headings",
                          yscrollcommand=scrollBar.set,
                          
                        #   xscrollcommand=scrollBar_sp.set
    )
                          
    #设置每列宽度和对齐方式
    tree.column('c1', width=20, anchor='center') 
    tree.column('c2', width=100, anchor='center')
    tree.column('c3', width=100, anchor='center')
    tree.column('c4', width=120, anchor='center')
    tree.column('c5', width=100, anchor='center')
    tree.column('c6', width=100, anchor='center') 
    tree.column('c7', width=100, anchor='center') 
    tree.column('c8', width=100, anchor='center') 
    tree.column('c9', width=100, anchor='center') 
    tree.column('c10', width=100, anchor='center')
    tree.column('c11', width=100, anchor='center') 


    #设置每列表头标题文本
    tree.heading('c1',text='序号')
    tree.heading('c2', text='姓名')
    tree.heading('c3', text='手机号')
    tree.heading('c4', text='QQ')
    tree.heading('c5', text='微信')
    tree.heading('c6', text='提供分校')
    tree.heading('c7', text='咨询科目')
    tree.heading('c8',text='咨询来自')
    tree.heading('c9',text='提供日期')
    tree.heading('c10',text='提供人')
    tree.heading('c11',text='备注')
    tree.pack(side=tkinter.LEFT, fill=tkinter.Y)
    def treeviewClick(event):
        #获取行的索引值
        iid=tree.identify_row(event.y)
        xy=tree.identify_element(event.x,event.y)
        s=tree.selection()
        # print(iid,xy )
        print(s)
        pass
    tree.bind('<Button-1>', treeviewClick)
    #插入数据
    res=sql.select_data()
    #for i in range(len(PrinterPywin32.get_enumjobs())):
    #     self.tree.insert("", "end", values=(i + 1, PrinterPywin32.get_enumjobs()[i]["Submitted"],
    # PrinterPywin32.get_enumjobs()[i]["pPrinterName"],
    # PrinterPywin32.get_enumjobs()[i]["JobId"],
    # PrinterPywin32.get_enumjobs()[i]["Status"]))
    # for i in range(len(res)):
        # tree.insert('', i, values=[str(i)]*11)
    std=[]
    for idt,name,phone,qq,weixin,prid_school,cslt_course,cslt_from,dt,provider,note in res:
        std.append((idt,name,phone,qq,weixin,prid_school,cslt_course,cslt_from,dt,provider,note))
    for i in range(len(res)):
        tree.insert("",i,values=(std[i][0],std[i][1],std[i][2],std[i][3],std[i][4],std[i][5],std[i][6],std[i][7],std[i][8],std[i][9],std[i][10]))    
        
def insert_action():
    def save_student():
        #name,phone,qq,weixin,prid_school,cslt_course,cslt_from,dt,provider,note)
        user_name=ent_name.get()
        phone=ent_phone.get()
        qq=ent_qq.get()
        weixin=ent_weixin.get()
        cbl_fx.bind("<<ComboboxSelected>>")
        fenxiao=cbl_fx.get()
        cbl_km.bind("<<ComboboxSelected>>")
        kemu=cbl_km.get()
        comboxlist.bind("<<ComboboxSelected>>")
        laizi=comboxlist.get()
        riqi=ent_dt.get()
        provider=ent_pr.get()
        beizhu=tx.get()
        try:
            sql.insert_data(user_name,phone,qq,weixin,fenxiao,kemu,laizi,riqi,provider,beizhu)
            messagebox.showinfo("info","保存成功")
        except:
            print("写入数据失败")     
    def cancel_student():
        pass    
    ins_dat=Tk()
    # ins_dat.geometry(400*400)
    # ins_dat.geometry('400*400')

    # ins_dat=Frame(ins_dat)
    # ins_dat.place(x=0, y=10)
    ins_dat.title('数据录入')
     #(ins_dat, '数据录入')
    # ins_dat.pack()
    #'姓名','手机号','QQ','微信', '提供分校', '咨询科目','咨询来自','提供日期', '提供人', '备注'
    lab_name   =Label(ins_dat,text='姓名:')
    lab_phone  =Label(ins_dat,text='手机号:')
    lab_qq     =Label(ins_dat,text='QQ:')
    lab_wexin  =Label(ins_dat,text='微信:')
    lab_fx     =Label(ins_dat,text='提供分校:')
    lab_km     =Label(ins_dat,text='咨询科目:')
    lab_lz     =Label(ins_dat,text='咨询来自:')
    lab_dt     =Label(ins_dat,text='提供日期:')
    lab_pr     =Label(ins_dat,text='提供人:')
    lab_nt     =Label(ins_dat,text='备注:')
    
    ent_name = Entry(ins_dat)
    ent_phone=Entry(ins_dat)
    ent_qq=Entry(ins_dat)  
    ent_weixin=Entry(ins_dat)
    # ent_fx=Entry(ins_dat)  
    # ent_km=Entry(ins_dat)
    # ent_lz=Entry(ins_dat)
    comval_fx=tkinter.StringVar()
    cbl_fx=ttk.Combobox(ins_dat,textvariable=comval_fx) #初ymf始化
    cbl_fx["values"]=("西乡校区","布吉校区","车公庙校区","白石洲校区")
    cbl_fx.current(0) 

    com_val = tkinter.StringVar()
    cbl_km=ttk.Combobox(ins_dat,textvariable=com_val) #初始化
    cbl_km["values"]=("提升学历","代办入户","会计考证","网络考试")
    cbl_km.current(0)

    comvalue = tkinter.StringVar()
    comboxlist=ttk.Combobox(ins_dat,textvariable=comvalue) #初始化
    comboxlist["values"]=("官网后台","在线调查后台","移动官网后台","地铁广告","百度金融"\
          ,"EC离线留言","离线宝","微信客服","PC网站-百度推广")
    comboxlist.current(0)  #选择第一个  

    # now = time.strftime("%H:%M:%S")
    # now_val=StringVar()
    # now_val.set(now)

    ent_dt=Entry(ins_dat)  
    ent_pr=Entry(ins_dat)  
    # ent_nt=Entry(ins_dat)
    tx=Entry(ins_dat)
    # tx=tkinter.Text(ins_dat,height=5)
    btn = Button(ins_dat,text = '保存',command = save_student)
    btn2 = Button(ins_dat,text = '取消',command = cancel_student)    
    lab_name.grid(row = 0,column = 0,sticky =W)
   
    lab_phone.grid(row = 1,column = 0,sticky = W)
    lab_qq.grid(row = 2,column = 0,sticky = W)
    lab_wexin.grid(row = 3,column = 0,sticky = W)
    lab_fx.grid(row = 4,column = 0,sticky = W)
    lab_km.grid(row = 5,column = 0,sticky = W)
    lab_lz.grid(row = 6,column = 0,sticky = W)
    lab_dt.grid(row = 7,column = 0,sticky = W)
    lab_pr.grid(row = 8,column = 0,sticky = W)
    lab_nt.grid(row = 9,column = 0,sticky = W)
   
    ent_name.grid(row = 0,column = 1,sticky = W)
    ent_phone.grid(row = 1,column = 1,sticky = W)
    ent_qq.grid(row = 2,column =1 ,sticky = W)
    ent_weixin.grid(row =3 ,column = 1,sticky = W)
    # ent_fx.grid(row =4 ,column = 1,sticky = W)
    cbl_fx.grid(row=4,column=1,sticky=W)
    # ent_km.grid(row =5 ,column = 1,sticky = W)
    cbl_km.grid(row =5 ,column = 1,sticky = W)
    # ent_lz.grid(row =6 ,column = 1,sticky = W)
    comboxlist.grid(row=6,column=1,sticky=W)
    ent_dt.grid(row =7 ,column = 1,sticky = W)  
    ent_pr.grid(row =8 ,column = 1,sticky = W) 
    # ent_nt.grid(row =9 ,column = 1,sticky = W) 
    tx.grid(row =9 ,column = 1,sticky = W) 
    btn.grid(row =10,column = 1,sticky = W)
    btn2.grid(row =10,column = 2,sticky = W) 



    ins_dat.mainloop()
def delete_action():
    pass
def edit_action():
    def edit_fd_info():
        std_id=ent_id.get()
        res=sql.edit_data(std_id)
        for idt,name,phone,qq,weixin,prid_school,cslt_course,cslt_from,dt,provider,note in res:
            ent_name_ed.insert(0,name)
            ent_phone_ed.insert(0,phone)
            ent_qq_ed.insert(0,qq)
            ent_weixin_ed.insert(0,weixin)
            ent_fx_ed.insert(0,prid_school)
            ent_km_ed.insert(0,cslt_course)
            ent_lz_ed.insert(0,cslt_from)
            ent_pr_ed.insert(0,provider)
            ent_dt_ed.insert(0,dt)
            ent_nt_ed.insert(0,note)
            # sql.update_data(id,name,phone,qq,weixin,prid_school,cslt_course,cslt_from,dt,provider,note) 
            print(name,phone,weixin)



            
        # print(res)
    def save_info():
        std_id=ent_id.get()
        uname=ent_name_ed.get()
        uphone=ent_phone_ed.get()
        uqq=ent_qq_ed.get()
        uweixin=ent_weixin_ed.get()
        ufx=ent_fx_ed.get()
        ukm=ent_km_ed.get()
        ulz=ent_lz_ed.get()
        upr=ent_pr_ed.get()
        udt=ent_dt_ed.get()
        ued=ent_nt_ed.get()
        
        if(uname and uphone):
            try:
                sql.update_data(std_id,uname,uphone,uqq,uweixin,ufx,ukm,ulz,udt,upr,ued)
                messagebox.showinfo("info","保存成功") 
            except:
                messagebox.showerror("info","保存失败")
                pass

        print(uname,udt)
    def del_info():
        std_id=ent_id.get()
        uname=ent_name_ed.get()
        if(uname and std_id):
            try:
                sql.delete_data(std_id,uname)
                messagebox.showinfo('infor','删除成功')
            except Exception as e:
                messagebox.showerror('info',e)
                pass




                
    edit_dat=Tk()
    edit_dat.title("信息维护")
    # edit_dat.geometry('','300*400')
    lab_id=Label(edit_dat,text='请输入编辑ID:')
    ent_id=Entry(edit_dat) 
    btn_fd=Button(edit_dat,text='查询',command=edit_fd_info)
    lab_id.grid(row = 0,column = 0,sticky = W)
    ent_id.grid(row = 0,column = 1,sticky = W)
    btn_fd.grid(row = 0,column = 2,sticky = W)

    # vl_name=StringVar()
    lab_name   =Label(edit_dat,text='姓名:')
    ent_name_ed=Entry(edit_dat,textvariable=edit_fd_info )
    lab_name.grid(row = 2,column = 0,sticky = W)
    ent_name_ed.grid(row = 2,column = 1,sticky = W)
   



    # vl_phone=StringVar()
    lab_phone  =Label(edit_dat,text='手机号:')
    ent_phone_ed=Entry(edit_dat,textvariable=edit_fd_info)
    lab_phone.grid(row = 3,column = 0,sticky = W)
    ent_phone_ed.grid(row = 3,column = 1,sticky = W)

    lab_qq_ed     =Label(edit_dat,text='QQ:')
    ent_qq_ed=Entry(edit_dat,textvariable=edit_fd_info)
    lab_qq_ed.grid(row = 4,column = 0,sticky = W)
    ent_qq_ed.grid(row = 4,column = 1,sticky = W)

    lab_wexin_ed  =Label(edit_dat,text='微信:')
    ent_weixin_ed=Entry(edit_dat,textvariable=edit_fd_info)
    lab_wexin_ed.grid(row = 5,column = 0,sticky = W)
    ent_weixin_ed.grid(row = 5,column = 1,sticky = W)

    # lab_fx_ed     =Label(edit_dat,text='提供分校:')
    # ent_fx_ed=Entry(edit_dat)
    # lab_fx_ed.grid(row=11,column=0,sticky=W)
    # ent_fx_ed.grid(row=11,column=1,sticky=W)
    lab_fx_ed  =Label(edit_dat,text='提供分校:')
    ent_fx_ed=Entry(edit_dat,textvariable=edit_fd_info)
    lab_fx_ed.grid(row = 6,column = 0,sticky = W)
    ent_fx_ed.grid(row = 6,column = 1,sticky = W)


    lab_km_ed     =Label(edit_dat,text='咨询科目:')
    ent_km_ed=Entry(edit_dat,textvariable=edit_fd_info)
    lab_km_ed.grid(row = 7,column = 0,sticky = W)
    ent_km_ed.grid(row = 7,column = 1,sticky = W)

    lab_lz_ed     =Label(edit_dat,text='咨询来自:')
    ent_lz_ed=Entry(edit_dat,textvariable=edit_fd_info)
    lab_lz_ed.grid(row = 8,column = 0,sticky = W)
    ent_lz_ed.grid(row = 8,column = 1,sticky = W)

    lab_dt_ed     =Label(edit_dat,text='提供日期:')
    ent_dt_ed=Entry(edit_dat,textvariable=edit_fd_info)
    lab_dt_ed.grid(row = 9,column = 0,sticky = W)
    ent_dt_ed.grid(row = 9,column = 1,sticky = W)
    
    lab_pr_ed     =Label(edit_dat,text='提供人:')
    ent_pr_ed=Entry(edit_dat,textvariable=edit_fd_info)
    lab_pr_ed.grid(row = 10,column= 0,sticky = W)
    ent_pr_ed.grid(row = 10,column = 1,sticky = W)


    lab_nt_ed     =Label(edit_dat,text='备注:')
    ent_nt_ed=Entry(edit_dat,textvariable=edit_fd_info)
    lab_nt_ed.grid(row = 12,column = 0,sticky = W)
    ent_nt_ed.grid(row = 12,column = 1,sticky = W)
    btn_sv=Button(edit_dat,text='保存',command=save_info)
    btn_sv.grid(row=13,column=0)

    btn_del=Button(edit_dat,text='删除',command=del_info)
    btn_del.grid(row=13,column=1,sticky=W)

    




    edit_dat.mainloop()
    pass    

def export_data():
    def exp_dt():
        import pandas as pd
        # import openpyxl  
        path=ent_path.get()
        # file_name=path+"abc.csv"
        rs=pd.DataFrame(res,columns=('id','姓名','手机号','QQ','微信','提供分校','咨询科目',\
           '咨询来自','提供日期','提供人','备注'))
        rs.to_csv(path,index=True,header=True)
        # print(rs)
        # print(file_name)
        # xlsx_file=pd.ExcelFile(file_name)
        # x1=xlsx_file.parse(0)
        # pd.DataFrame(res).to_excel("abc.xlsx",sheet_name="123",index=False,header=True)

    
    exp_dat=Tk()
    exp_dat.title("导出数据")
    lab_path=Label(exp_dat,text='请输入导出路径:')
    ent_path=Entry(exp_dat)
    btn_exp=Button(exp_dat,text='导出',command=exp_dt)
    lab_path.grid(row=0,column=0,sticky=W)
    ent_path.grid(row=0,column=1,sticky=W)
    btn_exp.grid(row=1,column=1,sticky=W)

    
    res=sql.select_data()
    

def get_tk():
    '''获取一个Tk对象'''
    return Tk()

def set_tk_title(tk, title):
    '''给窗口定义title'''
    if title is not None and title != '':
        tk.title(title)
    else:
        tk.title('xxx管理系统 v1.0')

def set_tk_geometry(tk, size):
    '''设置窗口大小，size的格式为：width x height,如：size = '200x100'.'''
    if size is not None and size != '':
        tk.geometry(size)
    else:
        tk.geometry('1024x600')
        # tk.resizable(width=True,height=True) # 宽不可变 高可变  默认True  
def get_menu(tk):
    '''获取一个菜单条'''
    return Menu(tk)
        
def menu_cy(menubar):
    '''定义菜单 常用'''
    #MENU_CY_ITEMS = ['查看','录入','编辑','删除','exit']
    cymenu = Menu(menubar, tearoff=1)
    cymenu.add_command(label=MENU_CY_ITEMS[0],command=select_action)
    cymenu.add_command(label=MENU_CY_ITEMS[1],command=insert_action)  
    cymenu.add_command(label=MENU_CY_ITEMS[2],command=edit_action)
    cymenu.add_command(label=MENU_CY_ITEMS[3],command=export_data)
    cymenu.add_separator()
    cymenu.add_command(label=MENU_CY_ITEMS[4],command=root.destroy)
    menubar.add_cascade(label=MENU_ITEMS[0], menu=cymenu)

def meun_help(menber):
    '''定义菜单Help'''
    help_menu = Menu(menubar, tearoff=1)
    help_menu.add_command(label=MENU_HELP_ITEMS[0])
    help_menu.add_command(label=MENU_HELP_ITEMS[1])
    menubar.add_cascade(label=MENU_ITEMS[1], menu=help_menu)
    


def init_menu_bar(menubar):
    '''初始化菜单条'''
    menu_cy(menubar)     #常用
    meun_help(menubar)     #help
    # menubar.add_cascade(label=MENU_ITEMS[-1], menu=meun_help)
    

#获得窗口对象

root = get_tk()
#设置窗口大小
set_tk_geometry(root, '')
#设置窗口title
set_tk_title(root, 'XXXXX信息管理系统v.1.0')
#获取菜单对象
menubar = get_menu(root)
#初始化菜单
init_menu_bar(menubar)
#加载菜单配置
root.config(menu=menubar)
# root.iconbitmap('D:\\Users\he_zh\\PycharmProjects\\stjx\\logo.bmp')
mainloop()

#     mainloop() 
# def main():
#     #获得窗口对象
#     root = get_tk()
#     #设置窗口大小
#     set_tk_geometry(root, '')
#     #设置窗口title
#     set_tk_title(root, 'Python 3.3.2 Shell')
#     #获取菜单对象
#     menubar = get_menu(root)
#     #初始化菜
#     init_menu_bar(menubar)
#     #加载菜单配置
#     root.config(menu=menubar)

#     mainloop() 


# if __name__ == "__main__":
#     main()