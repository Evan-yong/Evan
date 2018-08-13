__author__ = 'admin'
#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtpserver = "smtp.qq.com"
port = 465
sender = "756978382@qq.com"
psw = "kkxzzgcjbhekbeej"
receiver = ["756978382@qq.com","184415454@qq.com"]

file_path = "C:\\Evan\\report\\result.html"
with open(file_path,"rb") as fp:
    mail_body = fp.read()
msg = MIMEMultipart()
msg["from"] = sender
msg["to"] = ";".join(receiver)
msg["subject"] = "4threport"

body = MIMEText(mail_body,"html","utf-8")
msg.attach(body)

att = MIMEText(mail_body,"base64","utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment;filename="result.html"'
msg.attach(att)

try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(sender,psw)
except:
    smtp = smtplib.SMTP_SSL(smtpserver,port)
    smtp.login(sender,psw)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()

