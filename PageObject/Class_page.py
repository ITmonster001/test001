# -*- coding:utf-8 -*-
# @Time:2020/3/13 13:33
# @Author:xuzy
# @Email:1186136511@qq.com
# @File:Class_page.py
# @Software:PyCharm Community Edition
'''
课堂界面操作
上传作业、作业留言、查看作业提交状态

进入课堂：//*[@class="jumptoclass"]
切换到作业界面：//*[@class="nav gWidth"]//a[contains(text(),"作业")]
上传作业按钮：//*[@class="sc-btn"]  是个列表

查看作业状态 //*[@class="work-new-r fl "]//a
返回课堂页面 //p//*[@href="/Main/index.html"]
'''
from Common.basepage import BasePage
from PageObjectLocator.Class_page_locator import Class_page_locator as loc
from PageObject.Home_page import Home_page as hp
class Class_page(BasePage):

    def into_homework(self):
        self.ele_click(loc.loc_homework,"切换到作业界面")

    def add_attachment(self,filename):
        self.ele_click(loc.loc_up_homework,"点击上传作业按钮")
        self.ele_add_attachment(filename, loc.loc_add_attachment, "上传附件")
        self.ele_click(loc.loc_homework_submit, "点击提交按钮")


    def get_state(self):
        state = self.ele_get_text(loc.loc_state,"获取作业状态")
        return state

    def return_homepage(self):
        self.ele_click(loc.loc_return_home,"返回课堂页面")
