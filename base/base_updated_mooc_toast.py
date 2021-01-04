# -*- coding:utf-8 -*-
# Author:Marlon Kang
# 什么是toast参考博客https://blog.csdn.net/fitaotao/article/details/82251750
# 测试用例前置条件：退出登陆账号
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def get_driver():
    capabilities = {
        "platformName": "Android",
        "platformVersion": "6.0.1",
        "deviceName": "127.0.0.1:7555",
        "appPackage":'cn.com.open.mooc',
        "appActivity": "com.imooc.component.imoocmain.index.MCMainActivity",
        "noReset": 'true',
        #抓取toast才配置
        "automationName": "UiAutomator2"
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
    return driver


def login_by_node1():
    element1 = driver.find_element_by_android_uiautomator('new UiSelector().resourceId("cn.com.open.mooc:id/tab_layout")')
    #通过层级关系和index定位页面元素
    element2 = element1.find_element_by_android_uiautomator('new UiSelector().index(0)')
    element3 = element2.find_element_by_android_uiautomator('new UiSelector().index(4)')
    element3.click()
    #点击登录
    # login_by_password()
    return print("login_by_node1()点击账号")


def login_by_password_toast():
    time.sleep(1)
    driver.find_element_by_android_uiautomator('new UiSelector().resourceId("cn.com.open.mooc:id/header_line")').click()
    time.sleep(1)
    driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("cn.com.open.mooc:id/tvPassLogin")').click()
    #填入信息
    driver.find_element_by_android_uiautomator('new UiSelector().resourceId("cn.com.open.mooc:id/accountEditChannel2")').send_keys('15652236641')
    time.sleep(1)
    driver.find_element_by_android_uiautomator('new UiSelector().resourceId("cn.com.open.mooc:id/passwordEditChannel2")').send_keys('showthetoast')
    #点击登录触发toast出现
    time.sleep(1)
    driver.find_element_by_android_uiautomator('new UiSelector().resourceId("cn.com.open.mooc:id/login")').click()


def get_toast():
    time.sleep(1)
    toast_element = ("xpath","//*[contains(@text,'登录密码错误')]")
    result = WebDriverWait(driver,10,0.1).until(expected_conditions.presence_of_element_located(toast_element))
    print(result)


if __name__ == '__main__':
    driver = get_driver()
    time.sleep(3)
    #切换到“账号”底边选项
    login_by_node1()
    #错误密码调用触发toast
    login_by_password_toast()
    get_toast()
