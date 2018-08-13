__author__ = 'admin'
#coding=utf-8
import unittest

def all_case():
    case_dir = "C:\\Evan\\4thReport\\test_case"
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,pattern="test*.py",top_level_dir=None)

    # for test_suite in discover:
    #     for test_case in test_suite:
    #         testcase.addTests(test_case)
    testcase.addTests(discover)
    print testcase
    return testcase
if __name__ == "__main__":
    # runner = unittest.TextTestRunner()
    import HTMLTestRunner
    report_path = "C:\\Evan\\4thReport\\report\\result.html"

    fp = open(report_path,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"test",description=u"test")

    runner.run(all_case())
    fp.close()