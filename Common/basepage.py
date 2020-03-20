# -*- coding:utf-8 -*-
# @Time:2020/3/13 13:40
# @Author:xuzy
# @Email:1186136511@qq.com
# @File:basepage.py
# @Software:PyCharm Community Edition
'''
这是基础页面
主要封装访问页面功能
'''
import selenium
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
import time
from TestDatas.Path import screenshot_path


class BasePage:

    def __init__(self,driver:WebDriver):
        self.driver = driver

    # 等待元素可见
    def ele_wait_visible(self,loc,doc,timeout=10,frequency=0.5):
        start_time = time.time()
        try:
            WebDriverWait(self.driver,timeout,frequency).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            print("等待“{}”元素可见失败，详见报错信息{}".format(loc[1],{e}))
            self.save_img(doc)
            raise e
        else:
            end_time = time.time()
            print("等待元素“{}”可见成功，用时{}".format(loc[1],end_time-start_time))

    # 找到元素
    def ele_find(self,loc,doc,timeout=10,frequency=0.5):
        start_time = time.time()
        self.ele_wait_visible(loc,doc,timeout,frequency)
        try:
           ele = self.driver.find_element(*loc)
        except Exception as e:
            print("找到“{}”元素失败，详见报错信息{}".format(loc[1],e))
            self.save_img(doc)
            raise e
        else:
            end_time = time.time()
            print("找到元素“{}”成功，用时{}".format(loc[1],end_time-start_time))
            return ele

    # 元素点击操作
    def ele_click(self,loc,doc,timeout=10,frequency=0.5):
        start_time = time.time()
        ele = self.ele_find(loc,doc,timeout,frequency)
        try:
           ele.click()
        except Exception as e:
            print("点击“{}”元素失败，详见报错信息{}".format(loc[1],e))
            self.save_img(doc)
            raise e
        else:
            end_time = time.time()
            print("元素“{}”点击成功，用时{}".format(loc[1],end_time-start_time))
    # 元素输入操作
    def ele_sendkeys(self,loc, doc,msg,timeout=10, frequency=0.5):
        start_time = time.time()
        ele = self.ele_find(loc,doc,timeout,frequency)
        try:
            ele.send_keys(msg)
        except Exception as e:
            print("元素“{}”输入内容“{}”失败，详见报错信息{}".format(loc[1],msg,e))
            self.save_img(doc)
            raise e
        else:
            end_time = time.time()
            print("元素“{}”输入内容“{}”，用时{}".format(loc[1],msg,end_time - start_time))

    # 获取元素文本
    def ele_get_text(self,loc,doc,timeout=10,frequency=0.5):
        start_time = time.time()
        ele = self.ele_find(loc,doc,timeout,frequency)
        try:
           text = ele.text
        except Exception as e:
            print("获取元素“{}”文本失败，详见报错信息{}".format(loc[1],e))
            self.save_img(doc)
            raise e
        else:
            end_time = time.time()
            print("获取元素“{}”文本内容成功，文本内容为“{}”，用时{}".format(loc[1], text, end_time - start_time))
            return text

    # 上传附件
    def ele_add_attachment(self,filename,loc,doc,timeout=10,frequency=0.5):
        start_time = time.time()
        ele = self.ele_find(loc, doc, timeout, frequency)
        try:
            pass
        except Exception as e:
            pass
            self.save_img(doc)
            raise e
        else:
            end_time = time.time()
            pass

    # 保存错误截图
    def save_img(self,doc):
        start_time = time.time()
        error_time = time.strftime('%Y%m%d.%H%M%S')
        img_name = doc + error_time
        path = screenshot_path + "\\{}.png".format(img_name)
        try:
            self.driver.save_screenshot(path)
        except:
            print("截图失败！")
        else:
            end_time = time.time()
            print("截图成功，截图名称为“{}”，存储路径为“{}”，截图用时{}".format(img_name,path,(end_time-start_time)))




