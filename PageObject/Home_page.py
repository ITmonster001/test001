# -*- coding:utf-8 -*-
# @Time:2020/3/13 13:34
# @Author:xuzy
# @Email:1186136511@qq.com
# @File:Home_page.py
# @Software:PyCharm Community Edition
'''
主页界面操作
1、加入课程
2、加入课程--输入课程验证码--点击加入按钮
3、获取“加入验证码错误的验证提示”文本
4、点击更多
5、更多页面点击退课按钮
6、更多页面点击退课按钮--录入密码-点击退课
7、进入课堂 进入课堂：//*[@class="jumptoclass"]
'''
from Common.basepage import BasePage
from PageObjectLocator.Home_page_locator import Home_page_locator as loc
import time

class Home_page(BasePage):

    def add_class(self,code):
        self.ele_click(loc.loc_joinclass_button, "主页加入课程操作")
        time.sleep(1)
        self.ele_sendkeys(loc.loc_codeinput, "主页面输入课程邀请码操作", code)
        time.sleep(1)
        self.ele_click(loc.loc_button, "输入课程邀请码页面点击加入按钮")
        time.sleep(1)

    def skip(self):
        self.ele_click(loc.loc_skip,"加入课程成功后弹出提示中点击跳过")
        time.sleep(1)

    def add_class_off(self):
        self.ele_click(loc.loc_off,"输入课程邀请码页面点击取消按钮")
        time.sleep(1)

    def error_msg(self):
        error_msg = self.ele_get_text(loc.loc_errormsg,"主页面获取输入错误邀请码时的提示文本")
        time.sleep(1.5)
        return error_msg

    def get_more(self):
        self.ele_click(loc.loc_kdmore,"主页面点击课程下的更多选项")

    def dropclass(self,pwd):
        self.ele_click(loc.loc_dropclass,"更多页面点击退课按钮")
        self.ele_sendkeys(loc.loc_dropclass_pwd,"退课界面输入密码",pwd)
        self.ele_click(loc.loc_dropclass_button, "退课界面点击退课按钮")


    def get_code(self):
        code = self.ele_get_text(loc.loc_code,"获取第一个课程加课码")
        return code




    def into_class(self):
        self.ele_click(loc.loc_intoclass,'进入课堂')




