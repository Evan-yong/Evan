__author__ = 'admin'
#coding=utf-8
import requests
import unittest
from bs4 import BeautifulSoup

class Test(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test01(self):
        u'''4thReport login test'''
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
                    "Cookie": "bi_cookieid=15312066551784671718900; JSESSIONID=BE4AEC522F283186B315DA5F2E2CF16D; 4thCookieAd=; BIGipServerRA_Nginx_98_pool=!6QEU9fBK2WV4AdpfPQCamq130Nw0skj3uLZLS1VlVzFwcVu6IEixgaEVAH9AuYyyPmjLDUjX466QgDM=; i18next=ch"
        }
        url = "http://tac.deloitte.com/4thTest/user/login"
        a = str({"userName":"sarahtest","password":"200820e3227815ed1756a6b531e7e0d2","verificationCode":"1503","isAuto":0})

        b = a.replace(" ","")
        c = b.replace('\'','\"')
        d = {"args":c}
        print d
        s = requests.session()
        r = s.post(url,headers=headers,data=d,verify=False)
        print r.content
        print r.status_code

        # self.assertEqual(r.status_code,200,data="false")
if __name__ == "__main__":
    unittest.main()

