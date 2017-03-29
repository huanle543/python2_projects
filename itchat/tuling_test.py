# -*- coding: utf-8 -*-
"""
Created on Wed Mar 08 19:46:10 2017

@author: weizihan
"""

import requests

apiUrl = 'http://www.tuling123.com/openapi/api'
data = {
    'key'    : '8edce3ce905a4c1dbb965e6b35c3834d', # 如果这个Tuling Key不能用，那就换一个
    'info'   : 'bye', # 这是我们发出去的消息
    'userid' : 'wechat-robot', # 这里你想改什么都可以
}
# 我们通过如下命令发送一个post请求
r = requests.post(apiUrl, data=data).json()

# 让我们打印一下返回的值，看一下我们拿到了什么
print(r)