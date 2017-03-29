# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 22:25:25 2017

@author: weizihan
"""

from weibo import Client
import itchat
from time import sleep

Appkey='2964944126'
Apppsw='33e0b000a542fe8daaa2fa60da79dda0'
Redirect='https://api.weibo.com/oauth2/default.html'
userid='13913016343'
userpas='jianai@543'

huge='1223178222'

#与服务器建立联系
c = Client(Appkey, Apppsw, Redirect,username=userid, password=userpas)

itchat.auto_login(hotReload=True)
    

#获得当前时间线上的微博，默认20条
hl=c.get('statuses/home_timeline')

#打印当前时间线上的20条微博
for i in range(0,20):
    msg=''
    itchat.send(u'来自%s的: %s'%(hl['statuses'][i]['user']['name'],hl['statuses'][i]['text']),toUserName='filehelper')
            