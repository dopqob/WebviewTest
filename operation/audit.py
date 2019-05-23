#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 19:00
# @Author  : Bilon
# @File    : audit.py
import random
import logging
from time import sleep
from selenium.webdriver.support.select import Select
from common.driver import driver
from common.public import Common, error_shot
from util.tools import create_gbk, format_str
from config.eleconfig import *


class Audit(Common):
    """审核"""

    def audit_pass(self):
        logging.info(format_str('audit_pass'))
        self.click(AUDIT['同意'])
        self.click(AUDIT['通过'])

    def return_index(self):
        sleep(2)
        self.click(AUDIT['返回首页'])

    @error_shot
    def order_audit(self, flag=True):
        """
        订单审核
        :param flag: True代表审核通过，False代表审核拒绝
        """
        self.click(AUDIT['订单审核'])
        if not self.is_exists(AUDIT['拒绝']):
            logging.warning('{:*^56}'.format(' 订单审核列表为空 '))
            return

        if flag:
            self.audit_pass()
        else:
            logging.info(format_str('audit_refuse'))
            self.click(AUDIT['拒绝'])
            reasons = self.find_elements(AUDIT['订单拒绝理由'])
            random.choice(reasons).click()
            self.click(AUDIT['确认'])
        self.return_index()

    @error_shot
    def customer_audit(self, flag=True):
        """
        客户审核
        :param flag: True代表审核通过，False代表审核拒绝
        """
        self.click(AUDIT['客户审核'])

        if not self.is_exists(AUDIT['拒绝']):
            logging.warning('{:*^56}'.format(' 客户审核列表为空 '))
            return
        if flag:
            self.audit_pass()
        else:
            logging.info(format_str('audit_refuse'))
            self.click(AUDIT['拒绝'])
            self.clear_and_sendkeys(AUDIT['备注'], create_gbk(10))
            self.click(AUDIT['确认'])
        self.return_index()

    @error_shot
    def visit_audit(self, flag=True):
        """
        客户拜访审核
        :param flag: True代表审核通过，False代表审核拒绝
        """
        self.click(AUDIT['拜访审核'])

        if not self.is_exists(AUDIT['拒绝']):
            logging.warning('{:*^56}'.format(' 拜访审核列表为空 '))
            return
        if flag:
            self.audit_pass()
        else:
            logging.info(format_str('audit_refuse'))
            self.click(AUDIT['拒绝'])
            sel = self.find_element(AUDIT['拜访拒绝理由'])
            Select(sel).select_by_value(str(random.randint(1, 3)))
            self.clear_and_sendkeys(AUDIT['备注'], create_gbk(10))
            self.click(AUDIT['确认'])
        self.return_index()

    @error_shot
    def activity_audit(self, flag=None):
        """
        活动审核
        :param flag: True代表审核通过，False代表审核拒绝
        """
        self.click(AUDIT['活动审核'])

        if not self.is_exists(AUDIT['拒绝']):
            logging.warning('{:*^56}'.format(' 活动审核列表为空 '))
            return
        if flag:
            self.audit_pass()
        else:
            logging.info(format_str('audit_refuse'))
            self.click(AUDIT['拒绝'])
            self.clear_and_sendkeys(AUDIT['备注'], create_gbk(10))
            self.click(AUDIT['确认'])
        self.return_index()


if __name__ == '__main__':
    driver = driver()
    audit = Audit(driver)
    audit.open_wechat_ccloud()
    # audit.order_audit()
    audit.order_audit(flag=True)

    # audit.visit_audit()
    # audit.visit_audit(flag=False)
