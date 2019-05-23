#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 17:36
# @Author  : Bilon
# @File    : test_refund_qywx.py
import logging
import unittest
from HTMLTestRunner import HTMLTestRunner
from common.myunit import MyTestEW
from operation.refund import Refund
from util.tools import create_report_file


class RefundTest(MyTestEW):
    """退货"""

    def test_order_refund(self):
        """订单退货"""
        logging.info('******************** 订单退货 ********************')
        r = Refund(self.driver)
        r.open_wechat_ccloud(flag=False)
        r.enter_user_center()
        r.application_for_refund()
        r.order_refund()
        self.assertEqual(self.driver.title, '申请退货')

    def test_free_refund(self):
        """自由退货"""
        logging.info('******************** 自由退货 ********************')
        r = Refund(self.driver)
        r.open_wechat_ccloud(flag=False)
        r.enter_user_center()
        r.application_for_refund()
        r.free_refund()
        self.assertEqual(self.driver.title, '退货列表')


if __name__ == '__main__':
    file_path = create_report_file()
    with open(file_path, 'wb') as f:
        unittest.main(testRunner=HTMLTestRunner(stream=f, title=u'Ccloud测试报告', description=u'测试结果:'))