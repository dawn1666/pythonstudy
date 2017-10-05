#!/usr/bin env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author：       Dawn Yan 
   Email：       402184660@qq.com
   date：          2017/9/16
-------------------------------------------------
"""
product_list=[
    ('book',100),
    ('Mac Pro',9000),
    ('watch',500),
    ('coffee',30),
    ('Python',106),]

saving=input('input your saving:')
shopping_car=[]

if saving.isdigit():
    saving=int(saving)
    while True:
        for i,v in enumerate(product_list):
            print(i,v)
        user_choice=input('选择购买商品编号[退出:q]:')

        if user_choice.isdigit():
            user_choice=int(user_choice)
            if user_choice<len(product_list) and user_choice>=0:
                product_item=product_list[user_choice]
                if product_item[1]<saving:
                    saving-=product_item[1]
                    shopping_car.append(product_item)
                    print('您当前的余额为%s'%saving)
            else:
                print('编号错误')
        elif user_choice=='q':
            print('---------您已经购买如下商品-----------')
            for i in shopping_car:
                print(i)
            print('您的余额为%s'%saving)
            break

        else:
            print('invalid choice')
