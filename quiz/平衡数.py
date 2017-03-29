# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 19:30:49 2017

@author: weizihan
"""

def sep(num):
    alllist=[]
    while num:
        alllist.append(num%10)
        num=num/10
    return alllist
def count_sum(list1):
    sum1=1
    for i in list1:
        sum1 *= i
    return sum1
def balance(list2):
    left=[]
    right=[]
    left.append(list2[0])
    right=list2[1:]
    for it in range(len(right)-1):
        leftsum=count_sum(left)
        rightsum=count_sum(right)
        if leftsum==rightsum:
            return 'Yes'
        left.append(right[0])
        right=right[1:]
        print left,right
    return 'No'  
while True:
    try:
        ori=int(raw_input())
        
        alllist=sep(ori)
        print balance(alllist)
        
    except:
        break