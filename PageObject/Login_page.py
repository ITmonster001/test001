# -*- coding:utf-8 -*-
# @Time:2020/3/13 13:33
# @Author:xuzy
# @Email:1186136511@qq.com
# @File:Login_page.py
# @Software:PyCharm Community Edition
'''
登录界面操作
 loc_choosebutton_login = (By.XPATH,'//*[@class="login" ]',"登录按钮")
    loc_user = (By.XPATH,'//*[@name="account" ]','登录窗口：账户输入框')
    loc_pwd = (By.XPATH, '//*[@name="pass" ]" ]', '登录窗口：密码输入框')
    loc_button_login = (By.XPATH, '//*[@class="padding-cont pt-login"]//*[@class="btn-btn"]', '登录窗口：登录按钮')
'''
from PageObjectLocator.Login_page_locator import Login_page_locator as loc
from Common.basepage import BasePage
import time

class Login_page(BasePage):

    def login(self,user,pwd):
        self.ele_click(loc.loc_choosebutton_login,"点击登录页面登录按钮")
        time.sleep(1)
        self.ele_sendkeys(loc.loc_user,"输入账户",user)
        self.ele_sendkeys(loc.loc_pwd,"输入密码",pwd)
        self.ele_click(loc.loc_button_login,"点击登录按钮")

