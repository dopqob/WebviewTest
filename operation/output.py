#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 11:29
# @Author  : Bilon
# @File    : output.py
import logging
from time import sleep
from common.driver import driver
from common.public import Common, error_shot
from util.tools import format_str
from config.eleconfig import *


class Output(Common):

    @error_shot
    def enter_output(self):
        """进入出库单列表"""
        logging.info(format_str('enter_output'))
        self.click(OUTPUT['出库单'])

    def filter_order(self):
        """筛选待出库的订单"""
        logging.info(format_str('filter_order'))
        self.click(OUTPUT['订单状态'])
        sleep(0.5)
        self.find_elements(PUBLIC['列表'])[1].click()  # 选择待出库
        sleep(0.5)

        # 如果今天没有待出库的订单，循环调整时间直到发现待出库的订单
        if not self.is_exists(OUTPUT['订单列表']):
            i = 1
            while True:
                self.click(OUTPUT['日期筛选'])
                sleep(0.5)
                conditions = self.find_elements(PUBLIC['列表'])
                conditions[i].click()
                sleep(0.5)
                if self.is_exists(OUTPUT['订单列表']):
                    return self.find_elements(OUTPUT['订单列表'])
                i += 1
                if i == len(conditions):
                    break
            return None
        return self.find_elements(OUTPUT['订单列表'])

    @error_shot
    def single_output(self):
        """APP单个出库"""
        logging.info(format_str('single_output'))
        order_list = self.filter_order()
        if order_list:  # 如果存在待出库的订单
            order_list[0].click()   # 点击第一个订单展开详情
            sleep(0.5)
            self.click(OUTPUT['单个出库'])
            sleep(0.5)
            self.click(OUTPUT['确定'])
        else:
            logging.warning('{:*^56}'.format(' 没有待出库的订单 '))

    @error_shot
    def batch_output(self):
        """APP批量出库"""
        logging.info(format_str('batch_outbound'))
        order_list = self.filter_order()
        if order_list:
            self.click(OUTPUT['批量出库'])
            sleep(1)
            self.click(OUTPUT['二次确认'])
            sleep(5)
        else:
            logging.warning('{:*^56}'.format(' 没有待出库的订单 '))


if __name__ == '__main__':
    driver = driver()
    o = Output(driver)
    o.open_wechat_ccloud()
    o.enter_user_center()
    o.enter_output()
    o.single_output()
    # o.batch_output()
    o.return_home_page()
