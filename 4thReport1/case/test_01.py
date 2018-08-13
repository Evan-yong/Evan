# -*- coding: utf-8 -*-
__author__ = 'admin'

import requests
import unittest
from bs4 import BeautifulSoup
from case.login import Blog
from common.logger import Log

class Test(unittest.TestCase):
    log = Log()
    def setUp(self):
        s = requests.session()
        self.blog = Blog(s)
    # def tearDown(self):
    #     pass
    def test01(self):
        self.log.info("--------start-------")
        result = self.blog.login()

        # self.assertEqual(r.status_code,200,data="false")
if __name__ == "__main__":
    unittest.main()

