# -*- coding: utf-8 -*-
__author__ = 'admin'

import os
import unittest
import time
import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

cur_path = os.path.dirname(os.path.realpath(__file__)) # 返回当前绝对路径,去最后一个路径

def add_case(caseName="case",rule="test*.py"):
    case_path = os.path.join(cur_path,caseName) # 用例文件夹
    if not os.path.exists(case_path):os.mkdir(case_path)    # 不存在就自动创建
    print("test case path:%s"%case_path)
    discover = unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)   # 定义discover方法的参数
    print(discover)
    return discover # 遍历用例

def run_case(all_case,reportName="report"):
    now = time.strftime("%Y_%m_%d_%H_%M_%S")    # 获取当前时间
    report_path = os.path.join(cur_path,reportName) # report文件夹
    if not os.path.exists(report_path):os.mkdir(report_path) # 如果没有report文件夹就新建一个
    report_abspath = os.path.join(report_path,now+"result.html")    # 以当前时间+result.html为报告名称生成报告
    print("report path:%s"%report_abspath)  # 打印报告名称
    fp = open(report_abspath,"wb")  # 二进制打开报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"自动化测试报告，测试结果如下：",description=u"用例执行情况") #调用HTMLTestRunner
    runner.run(all_case)    # 运行用例
    fp.close()  # 关闭报告

def get_report_file(report_path):
    lists = os.listdir(report_path) # 获得report的名称列表
    print lists
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path,fn)))   # 按序排列生成的文件列表
    print("new test report:"+lists[-1]) # 找到最新生成的报告文件
    report_file = os.path.join(report_path,lists[-1])
    return report_file

def send_mail(sender,psw,receiver,smtpserver,report_file,port):
    with open(report_file,"rb") as f:
        mail_body = f.read()    # 打开邮件报告
    msg = MIMEMultipart()
    body = MIMEText(mail_body,_subtype="html",_charset="utf-8")
    msg["Subject"] = u"自动化测试报告"
    msg["from"] = sender
    msg["to"] = receiver
    msg.attach(body)    # 添加附件
    att = MIMEText(open(report_file,"rb").read(),"base64","utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment;filename="report.html"'
    msg.attach(att)

    try:
        smtp = smtplib.SMTP_SSL(smtpserver,port)    # 与服务器传输加密的数据
    except:
        smtp = smtplib.SMTP() # 普通邮件发送
        smtp.connect(smtpserver,port)
    smtp.login(sender,psw) # 登录邮箱
    smtp.sendmail(sender,receiver,msg.as_string()) # 发送邮件
    smtp.quit()
    print("test report email has send out !")

if __name__ == "__main__":
    all_case = add_case()   # 加载用例
    run_case(all_case)  # 执行用例
    report_path = os.path.join(cur_path,"report")   # 用例文件夹
    report_file = get_report_file(report_path)  # 获取最新的测试报告
    from config import readConfig   # 导入config包中的readConfig模块
    sender = readConfig.sender  # 获取寄件人
    psw = readConfig.psw    # 获取授权码
    smtp_server = readConfig.smtp_server    # 获取服务器
    port = readConfig.port  # 获取端口
    receiver = readConfig.receiver  # 获取发件人数据
    # print sender,psw,receiver,smtp_server,report_file,port
    send_mail(sender,psw,receiver,smtp_server,report_file,port)  # 最后发送报告

