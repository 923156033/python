#-*- codeing = utf-8 -*-
#@Time : 2020/11/17  11:36
#@Author : cyz
#@FIle : try.py
#@Software: PyCharm
try:
    a = int(input("请输入一个数:"))
    if (a > 0 and a < 6):
        print("正确")
except Exception as result:
     print("错误")
     print(result)