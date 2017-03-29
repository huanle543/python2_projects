# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 20:07:30 2017

@author: weizihan
"""

def equal(list1,list2):
    if len(list1)!=len(list2):
        return 0
    for i in list1:
        if i not in list2:
            return 0
    return 1
        
while True:
    try:
        count=int(raw_input())
        str=[]
        exist=[]
        
        classn=1
        for i in range(count):
            str.append(raw_input())
        exist.append(str[0])
        for i in range(count):
            if i !=0:
                if str[i] in exist:
                    break
            for k in range(i+1,count):
                if str[k] in exist:
                    break
                print str[i],str[k]
                if not equal(str[i],str[k]):
                    classn +=1
                    exist.append(str[k])
                print classn
        print classn
    except:
        break