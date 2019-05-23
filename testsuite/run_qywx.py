#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/14 17:33
# @Author  : Bilon
# @File    : run_qywx.py
import unittest
from HTMLTestRunner import HTMLTestRunner
from ..util.tools import create_report_file
from ..util.mail import Email


# 企业微信用例目录
dir_path = '../test_case_qywx'

# 加载测试用例，目录下以 "test" 开头的 ".py"文件
discover = unittest.defaultTestLoader.discover(dir_path, pattern='test*.py')
# discover = unittest.defaultTestLoader.discover(dir_path, pattern='test_customer_qywx.py')

# 报告输出路径
file = create_report_file()

# 运行用例并生成测试报告
with open(file, 'wb') as f:
    runner = HTMLTestRunner(stream=f, title=u'企业微信测试报告', description=u'测试结果:')
    runner.run(discover)

# 自动发送邮件
manager = Email()
manager.send()
