#!/usr/bin env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author：       Dawn Yan 
   Email：       402184660@qq.com
   date：          2017/9/18
-------------------------------------------------
"""
__author__ = 'Dawn Yan'
menu={
    '深圳':{
        "宝安":{
            '西乡':{
                '坪洲':{},
                '步行街':{},
            },
            '福永':{
                '机场':{},
                '固戍':{},
            },
            '新安':{}
        },
        '龙岗':{
            '坂田':{},
            '杨美':{},
        },
        '南山':{
            '科技园':{
                '腾讯':{},
                '中兴':{},
                '金蝶':{},
            },
            '大冲':{},
            '桃园':{},
        },
        },
    '长沙':{
        '岳麓':{
            '中南':{},
            '湖大':{},
        },
        '芙蓉':{
            '一中':{},
            '田家炳':{},
        },
    },
    '株洲':{
        '茶陵':{},
        '荷塘':{
            '中心广场':{},
            '火车站':{},
        },
    },
    }

current_layer=menu
parent_layer=[]
while True:
    for key in current_layer:
        print(key)
    choice = input(">>>:").strip()
    if len(choice)==0:
        continue
    if choice in current_layer:
        parent_layer.append(current_layer)   #将父层存入到列表里
        current_layer = current_layer[choice]
    elif choice == "b":
        if parent_layer:
            current_layer = parent_layer.pop()  #输入b后将父层赋值给当前层
    else:
        print("Please input again")
