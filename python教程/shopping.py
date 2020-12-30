# -*- codeing = utf-8 -*-
# @Time : 2020/12/22  20:20
# @Author : cyz
# @FIle : shopping.py
# @Software: PyCharm
g_z = input("请输入你的工资:")
s_p = [
    ('iPhone7',4800),
    ('MAC',10900),
    ('iPhone5',4000),
    ('iPhone4',3800),
    ('iPhone8',6800),
    ('iPhone11',8800),
    ('iPhoneX',7800),
]
s_p_list=[]
if g_z.isdigit():#判断输入是否为数字
    g_z=int(g_z) #强制转化为int型
    while True:
        for index,item in enumerate(s_p):
            print(index,item)
        user_choice=input("选择要购买的商品序号，退出请按Q")
        if user_choice.isdigit():
           user_choice=int(user_choice)
           if user_choice<len(s_p) and user_choice>=0:
                p_item=s_p[user_choice]
                if p_item[1]<=g_z:
                    s_p_list.append(p_item)
                    g_z-=p_item[1]
                    print("已购买的商品价格：%s,你剩下的余额：\033[31;1m%s\033[0m"%(p_item,g_z))
                else:
                    print("\033[31;1m你的余额[%s]不够卖所选的商品，请量力而行，慎重慎重！！！\033[0m" % g_z)
           else:
               print("商品不存在[%s]，请重新输入，退出请按Q"%user_choice)
        elif user_choice=='q':
            print("--------已购买的商品------")
            for i in s_p_list:
                print(i)
            print("你剩下的余额：%s" %g_z)
            exit()
        else:
             print("没有找到输入的商品序号")

