# -*- coding: utf-8 -*-
__author__ = 'admin'

import os
import ConfigParser

cur_path = os.path.dirname(os.path.realpath(__file__))  # 去当前目录的上一个目录
configPath = os.path.join(cur_path,"cfg.ini")   # 创建cfg.ini文件
conf = ConfigParser.ConfigParser()
conf.read(configPath)   # 读取cf.ini

smtp_server = conf.get("email","smtp_server") # 传入信息
sender = conf.get("email","sender")
psw = conf.get("email","psw")
receiver = conf.get("email","receiver")
port = conf.get("email","port")
