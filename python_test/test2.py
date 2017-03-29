# -*- coding: utf-8 -*-
"""
Created on Mon Mar 06 22:07:37 2017
•连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理
@author: weizihan
"""

word1=raw_input()
word2=raw_input()
def change(word):
    if len(word)>8:
        print word[:8]
        word_temp=word[8:]
        if len(word_temp)>8:
            change(word_temp)
        else:
            print word[8:]+'0'*(16-len(word))
    else:
          print word+'0'*(8-len(word))
change(word1)
change(word2)