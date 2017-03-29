# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Filename: helloworld.py
import wx
class Frame1(wx.Frame):
 def __init__(self,superior):
        wx.Frame.__init__(self, parent = superior, title = "Example", pos= (100,200), size= (500,300))
        panel = wx.Panel(self)
        text1= wx.TextCtrl(panel, value = "Hello, World!", size = (500,300))
if __name__ == '__main__': 
    app =wx.App()
    frame = Frame1(None)
    frame.Show(True)
    app.MainLoop() 