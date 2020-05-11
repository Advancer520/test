# coding:utf-8
import unittest
from common import HTMLTestRunner
import os
from common.send_mail import *

test_case_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_case')
report_path = os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'report'), 'result.html')


# 加载测试用例
discover = unittest.defaultTestLoader.discover(start_dir=test_case_path,  # 测试用例位置
                                               pattern='test*.py',  # test开头.py结尾的文件
                                               top_level_dir=None)

fb = open(report_path, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fb,
                                       title="自动化测试报告",
                                       verbosity=2,
                                       description="用例执行情况",
                                       retry=1,
                                       save_last_try=True)


runner.run(discover)
result_mail = send_mail()
