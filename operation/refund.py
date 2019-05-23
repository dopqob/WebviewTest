#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 15:28
# @Author  : Bilon
# @File    : refund.py
import random
import logging
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from common.driver import driver
from common.public import Common, error_shot
from config.eleconfig import *
from util.tools import format_str


class Refund(Common):

    @error_shot
    def application_for_refund(self):
        """申请退货"""
        self.click(REFUND['申请退货'])

    def add_product(self, kinds):
        """
        添加商品到购物车
        :param kinds: 商品种类,默认为1
        """
        logging.info(format_str('add_product'))

        big = self.find_elements(ORDER['大单位输入框'])  # 获取所有大单位输入框
        small = self.find_elements(ORDER['小单位输入框'])  # 获取所有大单位输入框
        for k in range(kinds):
            sleep(1)
            _i = random.randint(0, len(big)-1)
            big[_i].click()
            self.clear_and_sendkeys(ORDER['输入商品数量'], random.randint(0, 3))
            self.click(ORDER['确认输入'])

            sleep(0.5)
            small[_i].click()
            self.clear_and_sendkeys(ORDER['输入商品数量'], random.randint(1, 3))
            self.click(ORDER['确认输入'])
        sleep(1)

    @error_shot
    def order_refund(self):
        """订单退货"""
        logging.info(format_str('order_refund'))

        if not self.is_exists(REFUND['退货按钮']):
            for i in range(4):
                self.click(REFUND['日期筛选'])
                sleep(0.5)
                conditions = self.find_elements(PUBLIC['列表'])
                conditions[i].click()
                if self.is_exists(REFUND['退货按钮']):
                    break
            if not self.is_exists(REFUND['退货按钮']):
                logging.warning('{:*^56}'.format(' 没有可退货的订单 '))
                return
        self.click(REFUND['退货按钮'])
        self.click(REFUND['提交订单'])
        # sleep(0.5)
        self.click(REFUND['确定'])
        self.click(REFUND['否'])

    @error_shot
    def free_refund(self):
        """自由退货"""
        logging.info(format_str('free_refund'))

        self.click(REFUND['自由退货'])
        self.add_product(random.randint(1, 3))
        self.click(REFUND['下一步'])
        # sleep(0.5)
        self.click(ORDER['选择客户'])
        sleep(0.5)
        self.switch_to_native()  # 切换到APP视图做swipe操作
        self.swipe_up()  # 上滑加载更多客户
        sleep(3)
        self.switch_to_webview()  # 切换到H5视图继续后面的操作

        customers = self.find_elements(ORDER['客户'])  # 获取客户列表
        random.choice(customers).click()
        sleep(0.5)

        while True:
            if self.element_is_dispalyed(ORDER['侧边客户列表']):
                logging.warning('{:*^56}'.format(' 重新选择客户 '))
                random.choice(customers).click()
            else:
                break

        self.click(REFUND['退货仓库'])
        sleep(0.5)
        warehouses = self.find_elements(PUBLIC['列表'])
        random.choice(warehouses).click()
        self.click(REFUND['下一步'])
        # sleep(0.5)
        self.click(REFUND['确定'])
        # sleep(0.5)
        self.click(REFUND['查看订单'])


if __name__ == '__main__':
    driver = driver()
    r = Refund(driver)
    r.open_wechat_ccloud()
    r.enter_user_center()
    r.application_for_refund()
    r.order_refund()
    # r.free_refund()
