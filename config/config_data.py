#coding:utf-8
import os
import time
'''
a = os.getcwd()                 #获取当前所在目录
print("a:{}".format(a))

b = os.path.dirname(os.getcwd())    #获取当前所在的目录所在的目录，即当前目录的上一级目录
print("b:{}".format(b))

c = os.path.join(a,"geckodriver.log")   #获取当前所在目录并添加path完成拼接
print('c:{}'.format(c))

# 执行结果：
# a:E:\py3-jiaoben\Automation-ThirdJjtf\config
# b:E:\py3-jiaoben\Automation-ThirdJjtf
# c:E:\py3-jiaoben\Automation-ThirdJjtf\config\geckodriver.log
'''

def pro_root_dir():                 #获取项目根目录，返回根目录的路径
    current_path = os.getcwd()
    while (current_path[-9:] != R'ThirdJjtf') and (len(current_path) > 9):   #判断长度为了防止目录名称错误造成死循环
        current_path = os.path.dirname(current_path)
    return current_path

def config_path():                  #获取config目录的路径
    rootdir = pro_root_dir()
    config_path = os.path.join(rootdir,"config")
    return config_path

def report_path():               #获取report目录的路径
    rootdir = pro_root_dir()
    report_path = os.path.join(rootdir,'report')
    return report_path

def once_repath():              #创建本次执行结果的报告所在目录，用于在执行本次脚本前创建
    repath = report_path()
    once_repath = R'{}/report-{}'.format(repath,get_time())
    if os.path.exists(once_repath):
        pass
    else:
        os.mkdir(once_repath)
    return once_repath

def html_repath(once_repath):       #创建报告路径,需要传本次执行的报告所在目录
    html_repath = os.path.join(once_repath,'report_{}.html'.format(get_time()))
    return html_repath

def screen_path(once_repath):       #创建截图路径,需要传本次执行的报告所在目录
    screen_path = os.path.join(once_repath,'screen_{}.png'.format(get_time()))
    return screen_path

def log_path(str):                  #获取log目录的路径
    rootdir = pro_root_dir()
    log_path = os.path.join(rootdir,'log')
    return log_path

def case_path():                  #获取test_case目录的路径
    rootdir = pro_root_dir()
    case_path = os.path.join(rootdir,'test_case')
    return case_path

def get_time():                     #获取当前时间
    now = time.strftime("%Y%m%d-%H%M%S",time.localtime())
    return now

