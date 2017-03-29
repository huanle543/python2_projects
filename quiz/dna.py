# -*- coding: utf-8 -*-
"""
Created on Tue Mar 07 19:25:27 2017

@author: weizihan
"""

dna_all=raw_input()
dna1,dna2=dna_all.split()
dna_test=zip(dna1,dna2)
count = 0
dnadict={'A':'T','T':'A','C':'G','G':'C'}
for i,j in dna_test:
    if dnadict[i]!=j:
        count +=1
print count