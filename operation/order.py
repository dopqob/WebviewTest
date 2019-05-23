#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 11:37
# @Author  : Bilon
# @File    : order.py
import random
import logging
from time import sleep
from common.driver import driver
from common.public import Common, error_shot
from config.eleconfig import *
from util.tools import format_str


class Order(Common):

    def enter_normal_order(self):
        """通过首页进入下单页面"""
        logging.info(format_str('enter_normal_order'))
        self.click(ORDER['首页下单'])

    @error_shot
    def add_product(self, kinds=1):
        """
        添加商品到购物车
        :param kinds: 商品种类,默认为1
        """
        # 查看合计数量，如果数量不为0，先进购物车清空商品
        content = self.find_element(ORDER['合计数量']).text
        if content[1] != '0':
            self.empty_cart()

        logging.info(format_str('add_product'))
        # 选择商品
        sleep(0.5)
        big = self.find_elements(ORDER['大单位输入框'])  # 获取所有大单位输入框
        small = self.find_elements(ORDER['小单位输入框'])  # 获取所有大单位输入框
        if big:
            for k in range(kinds):
                sleep(1)
                _i = random.randint(1, len(big)-1)
                big[_i].click()
                self.clear_and_sendkeys(ORDER['输入商品数量'], random.randint(0, 3))
                self.click(ORDER['确认输入'])

                sleep(0.5)
                small[_i].click()
                self.clear_and_sendkeys(ORDER['输入商品数量'], random.randint(1, 3))
                self.click(ORDER['确认输入'])
        sleep(1)

    # @error_shot
    def empty_cart(self):
        """ 清空购物车 """
        logging.info(format_str('empty_cart'))
        if self.driver.title == '产品列表':
            self.click(ORDER['购物车'])

            # 通过循环删除购物车所有商品
            if self.driver.title == '购物车':
                del_icons = self.find_elements(ORDER['删除商品'])
                for icon in del_icons:
                    icon.click()
                    self.click(ORDER['删除确认'])
                    sleep(0.5)
                self.click(ORDER['添加商品'])

    # @error_shot
    def add_gift(self):
        """ 随机将购物车商品设为赠品 """
        logging.info(format_str('add_gift'))
        if self.driver.title == '产品列表':
            self.click(ORDER['购物车'])

            # 获取所有的赠品框，随机勾选
            if self.driver.title == '购物车':
                select_gift = self.find_elements(ORDER['勾选赠品'])
                random.choice(select_gift).click()

                self.click(ORDER['添加商品'])

    @error_shot
    def place_order(self, isgift=True):
        """首页下单"""
        logging.info(format_str('place_order'))
        if isgift:
            sleep(0.5)
            self.add_gift()

        self.click(ORDER['下单'])
        self.click(ORDER['选择客户'])
        self.switch_to_native()  # 切换到APP视图做swipe操作
        self.swipe_up()     # 上滑加载更多客户
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

        self.click(ORDER['提交订单'])
        sleep(0.5)
        self.click(ORDER['下单二次确认'])
        sleep(0.5)
        self.click(ORDER['跳转订单列表'])

    @error_shot
    def enter_mashup_order(self):
        """进入聚合下单"""
        logging.info(format_str('enter_mashup_order'))
        self.click(ORDER['聚合下单'])
        sleep(1)

    @error_shot
    def mashup_order(self, isgift=True):
        """聚合下单"""
        logging.info(format_str('mashup_order'))
        if isgift:
            sleep(0.5)
            self.add_gift()

        self.click(ORDER['下单'])
        sleep(1)
        self.click(ORDER['提交订单'])
        sleep(0.5)
        self.click(ORDER['下单二次确认'])
        sleep(1)
        self.click(ORDER['拜访完成'])
        sleep(0.5)
        self.click(ORDER['拜访完成二次确认'])


if __name__ == '__main__':
    driver = driver()
    order = Order(driver)
    flag = [True, False]
    order.open_wechat_ccloud()
    for i in range(1):
        order.enter_normal_order()
        order.add_product(3)
        # order.place_order(isgift=random.choice(flag))
        order.return_home_page()

    # order.enter_customer_visit()
    # order.enter_mashup_order()
    # order.add_product(random.randint(1, 3))
    # order.mashup_order(isgift=random.choice(flag))
    # order.return_home_page()
    # order.enter_normal_order()
    # order.add_product(3)
    # order.empty_cart()
