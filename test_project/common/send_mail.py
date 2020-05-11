# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_mail(smtpserver = "smtp.qq.com",
              port=465,
              sender="821187916@qq.com",
              psw="vxidthqdzzmkbfdf",
              receiver="cheng.qi@belle.com.cn",
              cc="liu.yongqiang@belle.com.cn,zeng.gw@belle.com.cn"):

    result_path = os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'report'),'result.html')

    msg = MIMEMultipart()
    msg['Subject'] = "自动化测试报告"
    msg['From'] = sender
    msg['To'] = receiver
    msg['Cc'] = cc
    f = open(result_path, encoding="utf-8")
    mail_body =f.read()
    f.close()
    body = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(body)
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename= "result.html"'
    msg.attach(att)


    smtp = smtplib.SMTP_SSL(smtpserver, port) # 授权码登陆
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

