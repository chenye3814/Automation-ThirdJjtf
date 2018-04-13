#-*- coding:UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
# from email.mime.image import MIMEImage
# from email.mime.base import MIMEBase
# from email import encoders
import time

email_qq_info = {
    'user':'582594381@qq.com',
    'pwd':'ggwqlsclupsgbeja',
    'ssl':'smtp.qq.com'
    }
email_163_info = {
    'user':'13551833814@163.com',
    'pwd':'cc19345017',
    'ssl':'smtp.163.com'
    }

class email_use:
    def __init__(self,user,pwd,ssl,reman,file_path):
        self.user = user
        self.pwd = pwd
        self.ssl = ssl
        self.reman = reman
        self.file_path = file_path
        self.meat =''

    def send_info(self):
        "发送带附件的报告"
        #创建一个带附件邮件的实例
        self.meat = MIMEMultipart('related')
        self.meat['Subject'] = Header('自动化测试报告','utf-8')
        self.meat['From'] = self.user
        self.meat['To'] = self.reman
        #邮件正文内容
        self.meat.attach(MIMEText('执行详情见附件'))
        #构造文本附件，传送文件，文件路径不要有中文
        att_txt = MIMEText(open(self.file_path,'rb').read(),'base64', 'utf-8')
        att_txt['Content-Type'] = 'application/octet-stream'
        att_txt['Content-Disposition'] = 'attachment; filename="{}"'.format(self.file_path)
        self.meat.attach(att_txt)

    def send_mail(self):
        try:
            send_mail = smtplib.SMTP_SSL(self.ssl,465)
            send_mail.login(self.user,self.pwd)
            send_mail.sendmail(self.user,self.reman,self.meat.as_string())
            send_mail.quit()
            print('sendmail success')
        except Exception as e:
            print('sendmail fail:{}'.format(e))

    def example(self):
        path = 'D:\\Desktop\\a\\report-180326-141749.html'
        a = email_use(**email_qq_info, reman='chy_chenye@live.com', file_path=path)
        a.send_info()
        a.send_mail()
