#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 14:03
# @Author  : Bilon
# @File    : run.py
import unittest
from HTMLTestRunner import HTMLTestRunner
from util.tools import create_report_file
from util.mail import Email


# 微信用例目录
dir_path = '../testcase'

# 加载测试用例，目录下以 "test" 开头的 ".py"文件
discover = unittest.defaultTestLoader.discover(dir_path, pattern='test*.py')

# 报告输出路径
file = create_report_file()

# 运行用例并生成测试报告
with open(file, 'wb') as f:
    runner = HTMLTestRunner(stream=f, title=u'APP测试报告', description=u'测试结果:')
    runner.run(discover)

# 自动发送邮件
manager = Email()
manager.send()
