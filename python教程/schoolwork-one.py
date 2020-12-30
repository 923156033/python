#-*- codeing = utf-8 -*-
#@Time : 2020/12/18  14:56
#@Author : cyz
#@FIle : schoolwork-one.py
#@Software: PyCharm
import pandas as pd
import xlrd

import openpyxl
import xlwt
from openpyxl.reader.excel import load_workbook
'''
作业一：博客
作业二：编写登入接口
    1、输入用户名密码
    2、认证成功后显示欢迎信息
    3、输错三次后锁定
作业三：多级菜单
    1、三级菜单
    2、可依次选择进入各子菜单
    3、所需新知识点：列表、字典
'''

# 作业一
# 博客地址：
# 作业二：
data = xlrd.open_workbook(r"E:\GitHub\python\python教程\data_user.xlsx")
table=data.sheets()[0]
user= table.col_values(0)
password=str(table.col_values(1))
u_user=input("请输入用户名：")
u_password=input("请输入密码:")
print(data.r)
if u_user in user:
    if u_password in password:
        print("认证成功,欢迎登入")
    else:
        print("密码错误")
else:
    print("用户不存在")