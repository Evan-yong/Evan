# -*- coding: utf-8 -*-
__author__ = 'admin'

import os
import ConfigParser

cur_path = os.path.dirname(os.path.realpath(__file__))  # 去当前目录的上一个目录
configPath = os.path.join(cur_path,"cookie.ini")   # 创建cfg.ini文件
conf = ConfigParser.ConfigParser()
conf.read(configPath)   # 读取cfg.ini

cookie = conf.get("email","smtp_server") # 传入信息