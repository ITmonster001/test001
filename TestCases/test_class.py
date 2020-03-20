# -*- coding:utf-8 -*-
# @Time:2020/3/13 13:37
# @Author:xuzy
# @Email:1186136511@qq.com
# @File:test_class.py
# @Software:PyCharm Community Edition

'''
测试用例：加入班级、退课、进入班级
前置：
（1）启动浏览器会话，访问网址【会话级】
（2）登录成功【会话级】
（3）

后置：
（1）退出会话【会话级】
'''

from TestDatas.datas_class import ClassDatas as cd
from PageObject.Home_page import Home_page
import pytest
import time

@pytest.mark.usefixtures("login_driver")

class Test_class:

    # 加入课程成功
    @pytest.mark.usefixtures("class_driver")
    def test_joinclass_success(self,class_driver):
        class_driver[1].add_class(cd.right_code['code'])
        time.sleep(1)
        class_driver[1].skip()
        time.sleep(1)
        code = class_driver[1].get_code()
        assert cd.right_code["msg"] in code


    # 加入课程失败
    @pytest.mark.parametrize("data",cd.wrong_code)
    @pytest.mark.usefixtures("joinclass_off")
    def test_joinclass_false(self,data,joinclass_off):
        joinclass_off[1].add_class(data['code'])
        time.sleep(1)
        error_msg = joinclass_off[1].error_msg()
        time.sleep(2)
        assert  error_msg == data["msg"]

    # 退课成功
    @pytest.mark.usefixtures("class_driver")
    def test_dropclass_success(self,class_driver):
        class_driver[1].get_more()
        time.sleep(1)
        class_driver[1].dropclass(cd.drop_class_success["pwd"])


    # 退课失败
    @pytest.mark.parametrize("data", cd.drop_class_error)
    @pytest.mark.usefixtures("class_driver")
    def test_dropclass_false(self,data,class_driver):
        class_driver[1].get_more()
        time.sleep(1)
        class_driver[1].dropclass(data["pwd"])
        error_msg = class_driver[1].error_msg()
        assert error_msg == data["msg"]


    # 进入班级
    @pytest.mark.usefixtures("class_driver")
    def test_intoclass(self):
        pass
