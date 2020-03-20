# -*- coding:utf-8 -*-
# @Time:2020/3/13 13:37
# @Author:xuzy
# @Email:1186136511@qq.com
# @File:test_class.py
# @Software:PyCharm Community Edition

class ClassDatas:

    right_code = {"code":"UEPLPQ"}
    wrong_code = [
        {"code":"3YZNRM","msg":"老师已经关闭加课"},
        {"code":"3YZNR","msg":"加课验证码必须是6位字符"},
        {"code":"6URLRH","msg":"你已经选过此课程"},
        {"code":"63333333","msg":"该加课码不存在或者已经失效"},
    ]

    drop_class_success = {"pwd": "19920708yao"}

    drop_class_error = [
        {"pwd":"1992yao0708","msg":"密码错误"},
        {"pwd": "19920708yao", "msg": "老师不允许学生进行退课，如需要退课，请找老师进行删除"}
    ]