# -*- coding:utf-8 -*-
# @Time:2020/3/14 19:51
# @Author:xuzy
# @Email:1186136511@qq.com
# @File:conftest.py
# @Software:PyCharm Community Edition
'''
这是一个pytest的fixture函数，定义各个测试用例中的前置后置
'''
import pytest

from selenium import webdriver
from TestDatas import Global_datas as gd
from PageObject.Login_page import Login_page
from PageObject.Home_page import Home_page
import time


@pytest.fixture(scope="class")
def web_driver():
    # 启动浏览器会话，访问地址
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(gd.basic_url)
    time.sleep(1)
    yield driver


@pytest.fixture(scope="class")
def login_driver(web_driver):
    # 登录页面实例化
    login = Login_page(web_driver)
    login.login(gd.login_data['user'], gd.login_data['pwd'])
    yield web_driver
    web_driver.quit()

@pytest.fixture
def class_driver(login_driver):
    homePage = Home_page(login_driver)
    yield login_driver,homePage


# 每次加入课程失败后，要做取消后置
@pytest.fixture
def joinclass_off(login_driver):
    homePage = Home_page(login_driver)
    yield login_driver,homePage
    time.sleep(1)
    homePage.add_class_off() # 点击取消按钮





