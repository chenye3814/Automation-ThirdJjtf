import unittest
import HTMLTestReportCN
import time
import os,sys
from test_case.common.aaa import My_test
from config import config_data
from config import config_email

report_path = config_data.once_repath()
html_report = config_data.html_repath(report_path)

def run():
    html_file = open(html_report,'wb')
    suite = unittest.TestSuite()
    suite.addTests(map(My_test['test3_open','test2_login','test1_screen'])) #依次添加测试用例
    runner = HTMLTestReportCN.HTMLTestRunner(stream=html_file,title='测试报告',verbosity=1,description='执行情况',tester='chenye')
    runner.run(suite)
    html_file.close()

def sendmail():
    email = config_email.email_use(**config_email.email_163_info,reman='582594381@qq.com',file_path=html_report)
    email.send_info()
    email.send_mail()
'''
def run2():
    html_file = open(html_report,'wb')
    suite = unittest.defaultTestLoader.discover(config_data.case_path(),pattern='a*.py') #加载类下所有用例到套件中，但是可能顺序有问题而造成错误
    # suite.addTest(unittest.makeSuite(My_test))  #加载类下所有用例到套件中，但是可能顺序有问题而造成错误   
    runner = HTMLTestReportCN.HTMLTestRunner(stream=html_file,title='测试报告',verbosity=1,description='执行情况',tester='chenye')
    runner.run(suite)
    html_file.close()
'''



