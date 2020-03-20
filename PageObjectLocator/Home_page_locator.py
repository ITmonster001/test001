# -*- coding:utf-8 -*-
# @Time:2020/3/13 13:34
# @Author:xuzy
# @Email:1186136511@qq.com
# @File:Home_page.py
# @Software:PyCharm Community Edition
'''
这是主页界面元素表单
加入课程：//*[@class="ktcon1l fr"]
课程加课验证码输入框 //*[@placeholder="请输入课程加课验证码"]
添加成功后的跳过：//*[@class="introjs-button introjs-skipbutton"]
加入按钮 //*[@class="cjli2"]//a
取消按钮 //*[@class="cjli1"]//a
加入失败的错误提示框 //*[@class = 'gTips']
进入课程：//*[@class="jumptoclass"]【列表】
更多：//*[@class="kdmore"]//span  【列表】
退课：//*[@class="kdli3"]
退课弹出框中的密码输入框  //*[@type="password"]
退课弹出框中的退课按钮  //*[@class="btn btn-positive" and contains(text(),"退课")]
退课错误提示 //*[@class = 'gTips']
'''

from selenium.webdriver.common.by import By

class Home_page_locator:

    loc_joinclass_button = (By.XPATH,'//*[@class="ktcon1l fr"]')
    loc_codeinput = (By.XPATH,'//*[@placeholder="请输入课程加课验证码"]')
    loc_button = (By.XPATH,'//*[@class="cjli2"]//a')
    loc_skip = (By.XPATH,'//*[@class="introjs-button introjs-skipbutton"]')
    loc_off = (By.XPATH,'//*[@class="cjli1"]//a')
    loc_errormsg = (By.XPATH,"//*[@class = 'gTips']//span")
    loc_jumptoclass = (By.XPATH,'//*[@class="jumptoclass"]')
    loc_kdmore = (By.XPATH,'//*[@class="kdmore"]//span')
    loc_dropclass = (By.XPATH,'//*[@class="kdli3"]')
    loc_dropclass_pwd = (By.XPATH,'//*[@type="password"]')
    loc_dropclass_button = (By.XPATH,'//*[@class="btn btn-positive" and contains(text(),"退课")]')
    loc_intoclass = (By.XPATH,'进入课堂：//*[@class="jumptoclass"]')
    loc_code = (By.XPATH,'//*[@class="iconfont iconketangma1"]')