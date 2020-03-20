# -*- coding:utf-8 -*-
# @Time:2020/3/13 15:33
# @Author:xuzy
# @Email:1186136511@qq.com
# @File:Letter_page_locator.py
# @Software:PyCharm Community Edition
'''
私信界面
点击联系人：//*[@class="classp active"]
点击通讯节点：//*[@class="text-overflow coursename down"]
点击第一个人：//*[@class="re-ul"]//p
发送内容输入域：//*[@class="ps-container"]
发送按钮：//*[@class="btn btn-positive disabled"]
上传附件：//*[@id="rt_rt_1e3c93klotic10ildpr1ohs1cpf1"]//label

'''
from selenium.webdriver.common.by import By

class Letter_page_locator:

    loc_contact = (By.XPATH,'//*[@class="classp active"]')
    loc_contact_directory = (By.XPATH,'//*[@class="text-overflow coursename down"]')
    loc_the_first = (By.XPATH,'//*[@class="re-ul"]//p')
    loc_sendmsg = (By.XPATH,'//*[@class="ps-container"]')
    loc_submit_button = (By.XPATH,'//*[@class="btn btn-positive disabled"]')
    loc_add_attachment = (By.XPATH,'//*[@id="rt_rt_1e3c93klotic10ildpr1ohs1cpf1"]//label')