#coding:utf-8
from selenium import webdriver

def browser_choose(str='chrome'):
    "通过传递的参数确定选择的浏览器"
    if str.lower()=="chrome":       #将传递的字符串全部小写进行比较，避免大小写引起启动不成功的问题
        browser = webdriver.Chrome()
    elif str.lower()=="ie":
        browser = webdriver.Ie()
    elif str.lower()=="firefox":
        browser = webdriver.Firefox()
    else:
        print("no this browser_driver")
    return browser
