#!/usr/bin env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author：       Dawn Yan 
   Email：       402184660@qq.com
   date：          2017/10/5
-------------------------------------------------
"""
__author__ = 'Dawn Yan'
import time
def decoretor(f):
    def test(*a,**b):
        print('begin call')

        time.sleep(1)
        f(*a,**b)
        print('end call')

    return test
@decoretor
def func(*args,**kwargs):
    s=0
    for i in args:
        s+=i
    print(s)

func(1,2,3,4)

