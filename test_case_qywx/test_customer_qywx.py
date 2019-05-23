#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 9:41
# @Author  : Bilon
# @File    : test_customer_qywx.py
import logging
import unittest
from time import sleep
from HTMLTestRunner import HTMLTestRunner
from common.myunit import MyTestEW
from operation.customer import Customer
from util.tools import create_report_file


class CustomerTest(MyTestEW):
    """客户/拜访"""
    FLAG = True

    def test_add_customer_with_photo(self):
        """新增客户-带照片"""
        logging.info('******************** 新增客户-带照片 ********************')
        c = Customer(self.driver)
        c.open_qywx_ccloud()
        c.new_customer()
        sleep(3)
        self.assertEqual(self.driver.title, '客户列表')

    def test_add_customer_without_photo(self):
        """新增客户-不带照片"""
        logging.info('******************** 新增客户-不带照片 ********************')
        c = Customer(self.driver)
        c.open_qywx_ccloud()
        c.new_customer(photo=False)
        self.assertEqual(self.driver.title, '客户列表')

    def test_customer_visit(self):
        """常规拜访"""
        logging.info('******************** 常规拜访 ********************')
        c = Customer(self.driver)
        c.open_qywx_ccloud()
        c.enter_customer_visit()
        c.customer_visit()
        c.return_home_page()

    def test_customer_visit_supplement(self):
        """常规拜访-补录"""
        logging.info('******************** 常规拜访-补录 ********************')
        c = Customer(self.driver)
        c.open_qywx_ccloud()
        c.enter_customer_visit()
        c.customer_visit_replenish()
        c.return_home_page()


if __name__ == '__main__':
    file_path = create_report_file()
    with open(file_path, 'wb') as f:
        unittest.main(testRunner=HTMLTestRunner(stream=f, title=u'Ccloud测试报告', description=u'测试结果:'))
