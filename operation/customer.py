#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 15:05
# @Author  : Bilon
# @File    : customer.py
import random
import logging
from time import sleep
from common.driver import driver
from common.public import Common, error_shot
from util.tools import create_gbk, create_name, create_phone, format_str
from config.eleconfig import *


class Customer(Common):

    @error_shot
    def new_customer(self, flag=None):
        """新增客户"""
        logging.info(format_str('new_customer'))

        self.click(CUSTOMER['新增客户'])
        sleep(0.5)

        subname = ['小店', '副食', '酒楼', '批发', '烟酒', '便利店', '小卖部', '超市', '百货']
        customer_name = create_name() + random.choice(subname)
        self.clear_and_sendkeys(CUSTOMER['客户名'], customer_name)
        self.clear_and_sendkeys(CUSTOMER['联系人'], create_name())
        self.clear_and_sendkeys(CUSTOMER['电话'], create_phone())

        self.click(CUSTOMER['客户类型'])
        sleep(0.5)
        subtype = ['零售终端', '批发', '餐饮', '其他', '商超']
        types = self.find_elements(CUSTOMER['列表'])
        while True:
            t = random.choice(types)
            if t.text in subtype:
                t.click()
                break
        sleep(0.5)

        self.click(CUSTOMER['客户等级'])
        sleep(0.5)
        rank = self.find_elements(CUSTOMER['列表'])
        random.choice(rank).click()

        # 选择配送地址
        self.click(CUSTOMER['省市区'])
        self.switch_to_native()  # 切换到APP视图做swipe操作，滑动选择省市区
        width = self.driver.get_window_size().get('width')  # 获取屏幕宽度
        height = self.driver.get_window_size().get('height')  # 获取屏幕高度
        self.driver.swipe(width * 0.25, height * 0.9, width * 0.25, height * 0.1)
        self.driver.swipe(width * 0.9, height * 0.9, width * 0.9, height * 0.7)
        self.switch_to_webview()  # 切换到H5视图继续后面的操作
        self.click(CUSTOMER['完成'])
        self.clear_and_sendkeys(CUSTOMER['详细地址'], create_gbk(8))

        if flag:
            for _ in range(random.randint(1, 3)):
                self.click(CUSTOMER['添加图片'])
                self.switch_to_native()  # 切换到微信视图控制相机拍照
                self.click(PUBLIC['拍照'])
                self.click(PUBLIC['确认照片'])
                sleep(3)  # 等待图片上传完成
                self.switch_to_webview()  # 切换到H5视图继续操作

        self.click(CUSTOMER['新增'])
        sleep(0.5)
        self.click(CUSTOMER['确定'])
        sleep(1)

    @error_shot
    def customer_visit(self, flag=None):
        """常规拜访"""
        logging.info(format_str('customer_visit'))

        self.click(CUSTOMER['常规拜访'])
        self.clear_and_sendkeys(CUSTOMER['备注'], create_gbk(30))
        self.take_photo(flag)
        self.click(CUSTOMER['提交'])
        sleep(1)
        self.click(CUSTOMER['确定'])
        self.click(CUSTOMER['拜访完成'])
        self.click(CUSTOMER['确定'])

    @error_shot
    def customer_visit_replenish(self, flag=None):
        """常规拜访-补录"""
        logging.info(format_str('customer_visit_replenish'))

        self.click(CUSTOMER['拜访补录'])
        self.clear_and_sendkeys(CUSTOMER['备注'], create_gbk(30))   # 添加备注信息
        self.upload_photo(flag)     # 添加照片
        self.click(CUSTOMER['提交'])
        sleep(1)
        self.click(CUSTOMER['确定'])
        self.click(CUSTOMER['拜访完成'])
        self.click(CUSTOMER['确定'])


if __name__ == '__main__':
    driver = driver()
    customer = Customer(driver)
    customer.open_wechat_ccloud()

    # 新增客户
    # customer.new_customer(flag=1)
    customer.enter_customer_visit()
    # customer.customer_visit()
    customer.customer_visit_replenish()
    customer.return_home_page()

    # for _ in range(100):
    #     # 常规拜访
    #     customer.enter_customer_visit()
    #     customer.customer_visit()
    #     customer.exit()
    #     print('第 {} 次执行完毕'.format(_+1))

    # 常规拜访补录
    # for _ in range(100):
    #     print('Start run loop {} '.format(_+1))
    #     customer.enter_customer_visit()
    #     sleep(1)
    #     customer.customer_visit_replenish()
    #     customer.return_home_page()
    #     sleep(1)
