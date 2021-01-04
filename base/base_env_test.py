# coding=utf-8
# appium测试环境的初步验证

from appium import webdriver

capabilities = {
    "platformName": "Android",
    "platformVersion": "6.0.1",
    "deviceName": "127.0.0.1:7555",
    "app": "D:\\Android\\喜马拉雅_6.6.93.3_298_.apk"
    #"appPackage":新版Appium1.19.1无需手动配置
    #"appActivity":新版Appium1.19.1无需手动配置

}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
