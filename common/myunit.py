#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 11:32
# @Author  : Bilon
# @File    : myunit.py
import logging
import unittest
import warnings
from time import sleep
from .driver import *


class MyTest(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)    # 忽略ResourceWarning警告
        self.driver = driver()

    def tearDown(self):
        logging.info('{:*^60}'.format(' 用例执行完毕 ') + '\n')
        sleep(1)
        self.driver.quit()


class MyTestEW(unittest.TestCase):
    """企业微信"""
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)  # 忽略ResourceWarning警告
        self.driver = qywx_driver()

    def tearDown(self):
        logging.info('{:*^60}'.format(' 用例执行完毕 ') + '\n')
        sleep(1)
        self.driver.quit()
