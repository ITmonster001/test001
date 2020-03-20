# -*- coding:utf-8 -*-
# @Time:2020/3/14 16:08
# @Author:xuzy
# @Email:1186136511@qq.com
# @File:Path.py
# @Software:PyCharm Community Edition
import os

# 基础路径
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 截图路径
screenshot_path = os.path.join(base_path, "OutPuts\img")