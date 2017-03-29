# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 16:12:40 2017

@author: weizihan
"""

while True:
    try:
        dict={}
        num=int(raw_input())
        for i in range(num):
            s=raw_input().split()
            key=s[0]
            value=int(s[1])
            if dict.has_key(key):
                dict[key]+=value
            else:
                dict[key]=value
        sorted(dict)
        for k in dict:
            print k,dict[k]
    except:
        break 