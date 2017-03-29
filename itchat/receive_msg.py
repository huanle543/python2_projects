# -*- coding: utf-8 -*-
"""
Created on Wed Mar 08 19:38:42 2017

@author: weizihan
"""

import itchat

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])

itchat.auto_login()
itchat.run()