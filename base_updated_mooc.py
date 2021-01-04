# -*- coding:utf-8 -*-
# Author:Marlon Kang
# 模拟手机已经更新app后，进入后的登录操作
# 需要先手动点击，把初次进页面引导提示取消掉
import time
from appium import webdriver


#mCurrentFocus = "Window{3c696c4u0cn.com.open.mooc / com.imooc.component.imoocmain.index.MCMainActivity}"
def get_driver():
    capabilities = {
        "platformName": "Android",
        "platformVersion": "6.0.1",
        "deviceName": "127.0.0.1:7555",
        "appPackage":'cn.com.open.mooc',
        "appActivity": "com.imooc.component.imoocmain.index.MCMainActivity",
        "noReset": 'true',
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
    return driver

def login_by_node():
    element1 = driver.find_element_by_id('cn.com.open.mooc:id/tab_layout')
    #通过层级关系和index定位页面元素
    element2 = element1.find_element_by_android_uiautomator('new UiSelector().index(0)')
    element3 = element2.find_element_by_android_uiautomator('new UiSelector().index(4)')
    element3.click()
    #点击登录
    login_by_password()
    return print("login_by_node()点击账号")

def login_by_index():
    element1 = driver.find_element_by_id('cn.com.open.mooc:id/tab_layout')
    #通过层级关系和index定位页面元素
    element2 = element1.find_element_by_android_uiautomator('new UiSelector().index(0)')
    elements = element2.find_elements_by_class_name('androidx.appcompat.app.ActionBar$Tab')
    #账号的索引4
    elements[4].click()
    # 点击登录
    login_by_password()
    return print("login_by_index()点击账号")


def login_by_password():
    time.sleep(1)
    driver.find_element_by_id('cn.com.open.mooc:id/header_line').click()
    time.sleep(1)
    driver.find_element_by_id('cn.com.open.mooc:id/tvPassLogin').click()
    #填入信息
    driver.find_element_by_id('cn.com.open.mooc:id/accountEditChannel2').send_keys('15652236641')
    time.sleep(1)
    driver.find_element_by_id('cn.com.open.mooc:id/passwordEditChannel2').send_keys('KYH0403a')
    #点击登录
    time.sleep(1)
    driver.find_element_by_id('cn.com.open.mooc:id/login').click()

def get_web_view():
    time.sleep(8)
    webview = driver.contexts
    print(webview)



if __name__ == '__main__':
    driver = get_driver()
    time.sleep(3)
    #切换到“账号”底边选项
    login_by_node()

