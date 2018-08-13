# -*- coding: utf-8 -*-
__author__ = 'admin'

import requests
import unittest
from common.logger import Log

class Blog():
    # s = requests.session()
    log = Log()
    def __init__(self,s):
        self.s = s
    def login(self):
        url = "http://tac.deloitte.com/4thTest/user/login"
        headers = {
                    "Connection": "keep-alive",
                    "Content-Length": "158",
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Origin": "http://tac.deloitte.com",
                    "X-Requested-With": "XMLHttpRequest",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Referer": "http://tac.deloitte.com/4thTest/login.html",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9",
        }
        a = str({"userName":"18883754450","password":"200820e3227815ed1756a6b531e7e0d2","verificationCode":"e6dc169a788dddaf65d2a185e06a9c48","isAuto":0})
        b = a.replace(" ","")
        c = b.replace('\'','\"')
        d = {"args":c}
        s = requests.session()
        r = s.post(url,headers=headers,data=d,verify=False)
        print r.content
        self.s = r.cookies
    def creatorder(self):
        url = "http://tac.deloitte.com/4thTest/orders/createOrder"
        headers = {
                    "Connection": "keep-alive",
                    "Content-Length": "173",
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Origin": "http://tac.deloitte.com",
                    "X-Requested-With": "XMLHttpRequest",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Referer": "http://tac.deloitte.com/4thTest/submitOrder.html?version=0",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.8",
            "Cookie": "bi_cookieid = 1533003777330187731618;4thCookieTracker = 4thCookieTrackerValue;JSESSIONID = 8DF48589B2DF7E921572BDBA9C17D421;4thCookieAd =;experience = submitOrder.html % 3Fversion % 3D0;BIGipServerRA_Nginx_98_pool =!SBprtgpZoaHO2EJfPQCamq130Nw0smny4TtiFhi8eYW / Yy85Jrr9UkPTDFW4YGDJDSxu2d1 / yqpUlAQ =;i18next = ch;mobile = 18883754450"
        }
        a = str({"mianIndustry":"法律服务","mianCateId":"1041295","orderType":0,"payAmount":0,"payType":0})
        b = a.replace(" ","")
        c = b.replace('\'','\"')
        d = {"args":c}
        print d
        s = requests.session()
        f = s.post(url,headers=headers,data=d,cookies=self.s,verify=False)
        print f.content
        print f.status_code

        # self.assertEqual(r.status_code,200,data="false")
if __name__ == "__main__":
        s = requests.session()
        blog = Blog(s)
        blog.login()
        blog.creatorder()
