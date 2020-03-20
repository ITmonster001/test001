# -*- coding:utf-8 -*-
# @Time:2020/3/14 15:37
# @Author:xuzy
# @Email:1186136511@qq.com
# @File:Homework_page.py
# @Software:PyCharm Community Edition
'''
作业界面元素

    loc_add_attachment = (By.XPATH, '//*[@class="sc-btn webuploader-container"]//*[@class="webuploader-pick"]', '添加附件')
    loc_homework_msg = (By.XPATH, '//*[@id="comment"]', '作业留言')
    loc_homework_msg_savebutton = (By.XPATH, '//*[@class="sure active" and contains(text(),"保存")]', '作业留言保存按钮')
    loc_homework_submit = (By.XPATH, '//*[@class="tj-btn"]', '作业提交按钮')
    loc_send_msg = (By.XPATH, '//*[@class="privateLetter"]//*[@target="_blank"]', '作业页面点击私信按钮')
    loc_success_msg = (By.XPATH, '//*[@class="weui_btn_dialog primary"]', '提交作业后的提示框')
    loc_backpage = (By.XPATH, '//*[@class="iconfont iconfanhui"]', '返回上一页（查看作业状态使用)')
    loc_state = (By.XPATH,'//*[@class="status fr"]//span','查看作业状态')
'''

from Common.basepage import BasePage
from PageObjectLocator.Homework_page_locator import Homework_page_locator as loc

class Home_page(BasePage):

    def add_h_attachment(self,filename):
        self.ele_add_attachment(filename,loc.loc_add_attachment,"上传附件")

    def leave_msg(self,msg):
        self.ele_sendkeys(msg,loc.loc_homework_msg,"输入作业留言")
        self.ele_click(loc.loc_homework_msg_savebutton, "保存作业留言")


    def homework_submit(self):
        self.ele_click(loc.loc_homework_submit,"点击提交按钮")

    def close_frame(self):
        self.ele_click(loc.loc_success_msg,"关闭提交作业成功后的提示框")

    def get_state(self):
        self.ele_get_text(loc.loc_state,"查看作业提交状态")