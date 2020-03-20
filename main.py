# -*- coding:utf-8 -*-
# @Time:2020/3/13 13:42
# @Author:xuzy
# @Email:1186136511@qq.com
# @File:main.py
# @Software:PyCharm Community Edition
import pytest
if __name__ == '__main__':
    pytest.main(["-s","-v",
                 "--html=OutPuts/reports/pytest.html",
                 "--alluredir=OutPuts/allure",
                ])

