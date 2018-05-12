#!/usr/bin env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author：       Dawn Yan 
   Email：       402184660@qq.com
   date：          2018/4/27
-------------------------------------------------
"""
__author__ = 'Dawn Yan'

import requests
from lxml import etree
url=requests.get('https://movie.douban.com/subject/26683723/comments?sort=new_score&status=P').text
#print(url)
s=etree.HTML(url)
file=s.xpath('//*[@id="comments"]/div/div[2]/p/text()')
import pandas as pd
fd= pd.DataFrame(file)
fd.to_csv('pdas4.csv')

