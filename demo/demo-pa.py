#-*- codeing = utf-8 -*-
#@Time : 2020/11/18  13:50
#@Author : cyz
#@FIle : demo-pa.py
#@Software: PyCharm

import  bs4
import  re
import urllib.request,urllib.error
import xlwt

def main():
    baseurl="https://gmon.jiaxianghudong.com/#/monitor_server_hall"
    datalist= getdata(baseurl)
    savepath =".\\weile.xls"
    savedata()
def getdata(baseurl):
    datalist = []
    return datalist

def savedata(savepath):
    print("save")

if __name__=="__main__":
    main()