from HTMLTestRunner_cn import HTMLTestRunner
import unittest
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import smtplib
from config import mail
import os,time
from config import config



def send_email(filename):
    mail_host='smtp.qq.com'
    mail_user=mail.mail_user
    mail_pass=mail.mail_pass

    sender=mail.sender #发送邮件的账号
    receivers=['18895356776@163.com']

    message = MIMEMultipart('related')

    f = open(filename,'rb')
    mail_body=f.read()
    att = MIMEText(mail_body,'base64','utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename="report.html"'
    message.attach(att)
    f.close()

    msg = MIMEText(mail_body,'html','utf-8')
    message.attach(msg)
    message['From'] = sender
    message['To'] = ','.join(receivers)
    message['Subject'] = Header('UI自动化测试报告','utf-8')

    smtp = smtplib.SMTP_SSL(mail_host,465)
    smtp.login(mail_user, mail_pass)
    smtp.sendmail(sender, receivers, message.as_string())
    smtp.quit()

def report(testreport):#查找最新的测试报告
    lists = os.listdir(testreport) #返回指定的文件夹包含的文件或文件夹的名字的列表
    lists.sort(key=lambda fn: os.path.getatime(testreport + '\\' + fn))  # 通过sort()方法重新按时间对目录下的文件进行排序
    filename = os.path.join(testreport,lists[-1])#lsit[-1]取最新生成的文件或文件夹
    return filename

if __name__ == '__main__':
    discover = unittest.defaultTestLoader.discover(config.TEST_CASE,pattern='test*')

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/report_html/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='UI自动化测试报告-华泰微网站',
                            description='The results are following:',
                            verbosity=2, retry=1, save_last_try=False)

    runner.run(discover)
    fp.close()

    test_report = config.REPORT_PATH # 定义报告文件目录
    rep = report(test_report)
    print(rep)
    send_email(rep)