# -*- coding: utf-8 -*-
__author__ = 'admin'

import logging,time
import os

cur_path = os.path.dirname(os.path.realpath(__file__))  # 获取当前文件上一个文件夹目录
log_path = os.path.join(os.path.dirname(cur_path), 'logs')  # 存放日志文件夹的路径

if not os.path.exists(log_path):os.mkdir(log_path)  # 如果没有这个文件夹，则新建

class Log():
    def __init__(self):

        self.logname = os.path.join(log_path, '%s.log'%time.strftime('%Y_%m_%d'))   # 文件命名
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')    # 日志格式
        #   [2018 - 07 - 19 09:47:41, 479] - logger.py] - WARNING: ----test end - ---
    def __console(self,level,message):
        fh = logging.FileHandler(self.logname,'a')  # 创建一个fileHandler写到本地
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        ch = logging.StreamHandler()    # 创建一个streamHandler输出到控制台
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        self.logger.removeHandler(ch)   # 避免日志输出重复
        self.logger.removeHandler(fh)
        fh.close()  # 关闭打开的文件

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)

if __name__ == "__main__":
    log = Log()
    log.info("---test start----")
    log.info("value 1,2,3")
    log.warning("----test end----")