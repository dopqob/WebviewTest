#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 16:39
# @Author  : Bilon
# @File    : test_z_output_qywx.py
import logging
import unittest
from HTMLTestRunner import HTMLTestRunner
from common.myunit import MyTestEW
from operation.output import Output
from util.tools import create_report_file


class OutputTest(MyTestEW):
    """APP端出库"""

    def test_single_output(self):
        """单个出库"""
        logging.info('******************** 单个出库 ********************')
        o = Output(self.driver)
        o.open_wechat_ccloud(flag=False)
        o.enter_user_center()
        o.enter_output()
        o.single_output()
        o.return_home_page()

    def test_batch_output(self):
        """批量出库"""
        logging.info('******************** 批量出库 ********************')
        o = Output(self.driver)
        o.open_wechat_ccloud(flag=False)
        o.enter_user_center()
        o.enter_output()
        o.batch_output()
        o.return_home_page()


if __name__ == '__main__':
    file_path = create_report_file()
    with open(file_path, 'wb') as f:
        unittest.main(testRunner=HTMLTestRunner(stream=f, title=u'Ccloud测试报告', description=u'测试结果:'))
