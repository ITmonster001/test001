# -*- coding:utf-8 -*-
# @Time:2020/3/13 13:33
# @Author:xuzy
# @Email:1186136511@qq.com
# @File:Login_page.py
# @Software:PyCharm Community Edition
'''
这是登录界面Login_page元素表单
链接：https://www.ketangpai.com/
登录按钮：//*[@class="login" ]
登录窗口：账户输入框：//*[@name="account" ]
密码输入框：//*[@name="pass" ]
登录按钮 //*[@class="padding-cont pt-login"]//*[@class="btn-btn"]
'''
from selenium.webdriver.common.by import By



class Login_page_locator:

    loc_choosebutton_login = (By.XPATH,'//*[@class="login" ]')
    loc_user = (By.XPATH,'//*[@name="account" ]')
    loc_pwd = (By.XPATH, '//*[@name="pass"]')
    loc_button_login = (By.XPATH, '//*[@class="padding-cont pt-login"]//*[@class="btn-btn"]')