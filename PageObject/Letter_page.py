# -*- coding:utf-8 -*-
# @Time:2020/3/13 15:33
# @Author:xuzy
# @Email:1186136511@qq.com
# @File:Letter_page.py
# @Software:PyCharm Community Edition
'''
私信界面
    loc_contact = (By.XPATH,'//*[@class="classp active"]','点击联系人选项')
    loc_contact_directory = (By.XPATH,'//*[@class="text-overflow coursename down"]','点击通讯目录节点')
    loc_the_first = (By.XPATH,'//*[@class="re-ul"]//p',"点击当前通讯节点下的第一个人")
    loc_sendmsg = (By.XPATH,'//*[@class="ps-container"]','发送内容输入域')
    loc_submit_button = (By.XPATH,'//*[@class="btn btn-positive disabled"]','发送按钮')
    loc_add_attachment = (By.XPATH,'//*[@id="rt_rt_1e3c93klotic10ildpr1ohs1cpf1"]//label','上传附件')
'''

from Common.basepage import BasePage
from PageObjectLocator.Letter_page_locator import Letter_page_locator as loc

class Letter_page(BasePage):

    def choose_contact(self):
        self.ele_click(loc.loc_contact,"点击联系人选项")
        self.ele_click(loc.loc_contact_directory,'点击通讯目录节点')
        self.ele_click(loc.loc_the_first, '点击当前通讯节点下的第一个人')

    def send_msg(self,msg):
        self.ele_sendkeys(loc.loc_sendmsg,"发送内容输入域输入msg",msg)
        self.ele_click(loc.loc_submit_button,"点击发送按钮")


    def send_attachment(self,filename):
        self.ele_add_attachment(filename,loc.loc_add_attachment,"发送附件")