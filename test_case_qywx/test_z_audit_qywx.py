#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 10:07
# @Author  : Bilon
# @File    : test_z_audit_qywx.py
import logging
import unittest
from HTMLTestRunner import HTMLTestRunner
from common.myunit import MyTestEW
from operation.audit import Audit
from util.tools import create_report_file


class AuditTest(MyTestEW):
    """审核测试"""

    def test_order_audit_pass(self):
        """订单审核-通过"""
        logging.info('******************** 订单审核-通过 ********************')
        audit = Audit(self.driver)
        audit.open_wechat_ccloud(flag=False)
        audit.order_audit()

    def test_order_audit_refuse(self):
        """订单审核-拒绝"""
        logging.info('******************** 订单审核-拒绝 ********************')
        audit = Audit(self.driver)
        audit.open_wechat_ccloud(flag=False)
        audit.order_audit(flag=False)

    def test_customer_audit_pass(self):
        """客户审核-通过"""
        logging.info('******************** 客户审核-通过 ********************')
        audit = Audit(self.driver)
        audit.open_wechat_ccloud(flag=False)
        audit.customer_audit()

    def test_customer_audit_refuse(self):
        """客户审核-拒绝"""
        logging.info('******************** 客户审核-拒绝 ********************')
        audit = Audit(self.driver)
        audit.open_wechat_ccloud(flag=False)
        audit.customer_audit(flag=False)

    def test_visit_audit_pass(self):
        """拜访审核-通过"""
        logging.info('******************** 拜访审核-通过 ********************')
        audit = Audit(self.driver)
        audit.open_wechat_ccloud(flag=False)
        audit.visit_audit()

    def test_visit_audit_refuse(self):
        """拜访审核-拒绝"""
        logging.info('******************** 拜访审核-拒绝 ********************')
        audit = Audit(self.driver)
        audit.open_wechat_ccloud(flag=False)
        audit.visit_audit(flag=False)

    def test_activity_audit_pass(self):
        """活动审核-通过"""
        logging.info('******************** 活动审核-通过 ********************')
        audit = Audit(self.driver)
        audit.open_wechat_ccloud(flag=False)
        audit.activity_audit()

    def test_activity_audit_refuse(self):
        """活动审核-拒绝"""
        logging.info('******************** 活动审核-拒绝 ********************')
        audit = Audit(self.driver)
        audit.open_wechat_ccloud(flag=False)
        audit.activity_audit(flag=False)


if __name__ == '__main__':
    file_path = create_report_file()
    with open(file_path, 'wb') as f:
        unittest.main(testRunner=HTMLTestRunner(stream=f, title=u'Ccloud测试报告', description=u'测试结果:'))