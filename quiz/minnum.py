# -*- coding: utf-8 -*-
"""
Created on Tue Mar 07 19:56:42 2017

@author: weizihan
"""

import math

input_ = raw_input()
num,lens=map(int,input_.split())
#print 'num:',num,'lens:',lens
minlen=1000
tarset=[]
for i in xrange((num/lens)+1,int(math.sqrt(num))-1,-1):
    numset=[]
    numset.append(i)
    #print i
    sum=i
    for j in range(200):
        i -= 1
        #print i
        numset.append(i)
        sum += i
        #print 'sum:',sum,'len(numset):',len(numset)
        #print (sum==num),(len(numset)<minlen),(len(numset)>lens)
        if (sum == num) & (len(numset)<minlen) & (len(numset)>lens):
            tarset = numset
            minlen = len(numset)
            #print 'done'
            break
        elif sum<num:
            continue
        elif sum>num:
            break
      
if (len(tarset)==0) | (len(tarset)>100):
      print 'No'
else :
      for nums in sorted(tarset):
          print nums,
            
