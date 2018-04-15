#coding:utf-8
from selenium import webdriver

def browser_choose(str):
    if str=="Chrome":
        browser = webdriver.Chrome()
    elif str=="ie":
        browser = webdriver.Ie()
    elif str=="firefox":
        browser = webdriver.Firefox()
    else:
        print("no this driver")

    return browser


