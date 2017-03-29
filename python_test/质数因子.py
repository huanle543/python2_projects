# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

while True:
    try:
        num=int(raw_input())
        i=2
        while num!=1:
            while num%i ==0:
                print i,
                num/=i
            i+=1
        print '',
    except:
        break