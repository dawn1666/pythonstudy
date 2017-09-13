#!/usr/bin env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author：       Dawn Yan 
   Email：       402184660@qq.com
   date：          2017/9/13
-------------------------------------------------
"""
__author__ = 'Dawn Yan'
i=0
j=0
while i <9:
    i += 1
    while j<9:
        j += 1
        print( "%s*%s=%s"  %  (j,i,j*i),end=" ")
        if i==j:
            j=0
            print("-")
            break
