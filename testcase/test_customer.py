#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 9:41
# @Author  : Bilon
# @File    : test_customer.py
import logging
import unittest
from HTMLTestRunner import HTMLTestRunner
from common.myunit import MyTest
from operation.customer import Customer
from util.tools import create_report_file


class CustomerTest(MyTest):
    """客户/拜访"""

    def test_add_customer_with_photo(self):
        """新增客户-带照片"""
        logging.info('{:*^60}'.format(' 新增客户-带照片 '))
        c = Customer(self.driver)
        c.open_wechat_ccloud()
        c.new_customer(flag=1)
        c.return_home_page()
        # self.assertEqual(self.driver.title, '客户列表')

    def test_add_customer_without_photo(self):
        """新增客户-不带照片"""
        logging.info('{:*^60}'.format(' 新增客户-不带照片 '))
        c = Customer(self.driver)
        c.open_wechat_ccloud()
        c.new_customer()
        c.return_home_page()
        # self.assertEqual(self.driver.title, '客户列表')

    def test_customer_visit(self):
        """常规拜访"""
        logging.info('{:*^60}'.format(' 常规拜访 '))
        c = Customer(self.driver)
        c.open_wechat_ccloud()
        c.enter_customer_visit()
        c.customer_visit()
        c.return_home_page()

    def test_customer_visit_supplement(self):
        """常规拜访-补录"""
        logging.info('{:*^60}'.format(' 常规拜访-补录 '))
        c = Customer(self.driver)
        c.open_wechat_ccloud()
        c.enter_customer_visit()
        c.customer_visit_replenish()
        c.return_home_page()


if __name__ == '__main__':
    file_path = create_report_file()
    with open(file_path, 'wb') as f:
        unittest.main(testRunner=HTMLTestRunner(stream=f, title=u'Ccloud测试报告', description=u'测试结果:'))
