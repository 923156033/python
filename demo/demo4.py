#-*- codeing = utf-8 -*-
#@Time : 2020/11/16  11:16
#@Author : cyz
#@FIle : demo4.py
#@Software: PyCharm
products = [["iphone",6888],["Macpro",14800],["小米6",2499],["coffee",31],["book",60],["nike",699]]
i=0
for number in products:
    print("%d "%(i),end='\t')
    i += 1
    for numbe in number:
        print("%s"%numbe,end='\t')
    print('\n')

shopping = []
a = 1
num = 0
shoppingname = ""
while(a < len(products)):
    print("请输入产品编号,退出按Q")
    a = input()
    if(a == "q"):
        for y in range(0,len(shopping)):
            num = shopping[y][1] + num
            shoppingname +="\n" + shopping[y][0]
        print("你所买的产品有：%s ,\n需要支付价格是：%d" % (shoppingname,num))
        break

    else:
        try:
            a = int(a)
            if (a > 0 and a < 6):
                shopping.append(products[a])
                print(shopping)
        except ValueError:
            print("输出错误")