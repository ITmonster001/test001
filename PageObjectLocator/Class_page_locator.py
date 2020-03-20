# -*- coding:utf-8 -*-
# @Time:2020/3/13 13:33
# @Author:xuzy
# @Email:1186136511@qq.com
# @File:Class_page.py
# @Software:PyCharm Community Edition
'''
这是课程界面元素表单
进入课堂：//*[@class="jumptoclass"]
切换到作业界面：//*[@class="nav gWidth"]//a[contains(text(),"作业")]
上传作业按钮：//*[@class="sc-btn"]  是个列表
添加附件：//*[@class="sc-btn webuploader-container"]//*[@class="webuploader-pick"]
添加附件需要进行上传操作的功能封装
作业留言：//*[@id="comment"]
作业留言保存按钮：//*[@class="sure active" and contains(text(),"保存")]
提交按钮 //*[@class="tj-btn"]
私信：//*[@class="privateLetter"]//*[@target="_blank"]
提交作业后的提示框 //*[@class="weui_btn_dialog primary"]
返回上一页（查看作业状态使用） //*[@class="iconfont iconfanhui"]
查看作业状态 //*[@class="work-new-r fl "]//a
返回课堂页面 //p//*[@href="/Main/index.html"]
'''
from selenium.webdriver.common.by import By

class Class_page_locator:

    loc_jumptoclass = (By.XPATH,'//*[@class="jumptoclass"]')
    loc_homework = (By.XPATH,'//*[@class="nav gWidth"]//a[contains(text(),"作业")]')
    loc_up_homework = (By.XPATH,'//*[@class="sc-btn"]')
    loc_add_attachment = (By.XPATH,'//*[@class="sc-btn webuploader-container"]//*[@class="webuploader-pick"]')

    loc_homework_msg = (By.XPATH,'//*[@id="comment"]')
    loc_homework_msg_savebutton = (By.XPATH,'//*[@class="sure active" and contains(text(),"保存")]')
    loc_homework_submit = (By.XPATH,'//*[@class="tj-btn"]')
    loc_send_msg = (By.XPATH,'//*[@class="privateLetter"]//*[@target="_blank"]')
    loc_success_msg = (By.XPATH,'//*[@class="weui_btn_dialog primary"]')
    loc_backpage = (By.XPATH,'//*[@class="iconfont iconfanhui"]')
    loc_state = (By.XPATH,'//*[@class="work-new-r fl "]//a')
    loc_return_home = (By.XPATH,'//p//*[@href="/Main/index.html"]')