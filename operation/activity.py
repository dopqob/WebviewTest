#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 9:51
# @Author  : Bilon
# @File    : activity.py
import random
import logging
from time import sleep
from common.driver import *
from common.public import Common, error_shot
from util.tools import create_phone, create_name, create_gbk, format_str
from config.eleconfig import *


class ActivityCommon(Common):
    """活动基类，封装一些公共方法"""

    def choose_activity(self):
        """选择活动"""
        logging.info(format_str('choose_activity'))

        self.click(ACTIVITY['活动'])
        sleep(1)
        acts = self.find_elements(ACTIVITY['列表'])
        random.choice(acts).click()
        sleep(1)

    def choose_expense(self):
        """选择费用明细"""
        logging.info(format_str('choose_expense'))

        self.click(ACTIVITY['费用明细'])
        sleep(1)
        costs = self.find_elements(ACTIVITY['列表'])
        random.choice(costs).click()
        self.click(ACTIVITY['确定'])

    def present_num(self):
        """赠送数量"""
        logging.info(format_str('present_num'))

        if self.is_exists(ACTIVITY['赠送数量']):  # 非补录时数量输入框的id是apply_num1
            if self.element_is_dispalyed(ACTIVITY['赠送数量']):
                available_num = int(self.get_text(ACTIVITY['可用数量'])[1:-1])  # 可用数量
                if available_num <= 0:
                    self.clear_and_sendkeys(ACTIVITY['赠送数量'], '0')
                else:
                    self.clear_and_sendkeys(ACTIVITY['赠送数量'], random.randint(1, 5))

        if self.is_exists(ACTIVITY['补录赠送数量']):  # 非补录时数量输入框的id是apply_num1
            if self.element_is_dispalyed(ACTIVITY['补录赠送数量']):
                available_num = int(self.get_text(ACTIVITY['可用数量'])[1:-1])  # 可用数量
                if available_num <= 0:
                    self.clear_and_sendkeys(ACTIVITY['补录赠送数量'], '0')
                else:
                    self.clear_and_sendkeys(ACTIVITY['补录赠送数量'], random.randint(1, 5))

    def present_money(self):
        """赠送金额"""
        logging.info(format_str('present_money'))

        if self.is_exists(ACTIVITY['赠送金额']):   # 非补录时金额输入框的id是apply_amount1
            if self.element_is_dispalyed(ACTIVITY['赠送金额']):
                money = [10, 20, 30, 50, 80, 100]
                available_money = int(self.get_text(ACTIVITY['可用金额'])[1:-1])  # 可用赠送金额
                while True:
                    amount = random.choice(money)  # 从列表中随机选择一个元素
                    if amount <= available_money:
                        self.clear_and_sendkeys(ACTIVITY['赠送金额'], amount)
                        break

        if self.is_exists(ACTIVITY['补录赠送金额']):  # 非补录时金额输入框的id是apply_amount1
            if self.element_is_dispalyed(ACTIVITY['补录赠送金额']):
                money = [10, 20, 30, 50, 80, 100]
                available_money = int(self.get_text(ACTIVITY['可用金额'])[1:-1])  # 可用赠送金额
                while True:
                    amount = random.choice(money)  # 从列表中随机选择一个元素
                    if amount <= available_money:
                        self.clear_and_sendkeys(ACTIVITY['补录赠送金额'], amount)
                        break

    def submit_and_confirm(self):
        """提交活动"""
        logging.info(format_str('submit_and_confirm'))
        if self.is_exists(ACTIVITY['提交']):
            self.click(ACTIVITY['提交'])
            # 如果出现继续上传的提示，点击继续上传
            if self.is_exists(ACTIVITY['继续上传']):
                self.click(ACTIVITY['继续上传'])
                sleep(5)
                self.click(ACTIVITY['提交'])
        else:
            self.click(ACTIVITY['营销提交'])
        self.click(ACTIVITY['确定'])
        sleep(2)


class NormalActivity(ActivityCommon):
    """普通活动"""
    @error_shot
    def normal_activity(self, flag=None):
        """活动快捷执行"""

        # 进入"活动快捷执行"
        self.click(ACTIVITY['活动快捷执行'])
        sleep(1)

        # 选择活动
        self.choose_activity()
        self.choose_expense()
        self.present_num()
        self.present_money()
        self.take_photo(flag)
        self.submit_and_confirm()
        self.click(ACTIVITY['关闭弹层'])


class MarketingCampaign(ActivityCommon):
    """营销推广活动"""

    def choose_activity_type(self, index):
        """进入营销推广并选择活动类型"""
        logging.info(format_str('choose_activity_type'))

        # 进入营销推广
        self.click(ACTIVITY['营销推广'])
        sleep(0.5)
        self.find_elements(ACTIVITY['选择营销活动'])[index].click()
        sleep(3)

    def choose_activity_supplement_type(self, index):
        """进入营销补录并选择活动类型"""
        logging.info(format_str('choose_activity_supplement_type'))

        # 进入营销推广
        self.click(ACTIVITY['营销补录'])
        sleep(0.5)
        self.find_elements(ACTIVITY['选择营销活动'])[index].click()
        sleep(1)

    @error_shot
    def cultivate_activity(self, flag=None):
        """消费培育活动"""
        # 选择消费培育活动
        self.choose_activity_type(0)
        logging.info(format_str('cultivate_activity'))

        self.choose_activity()  # 选择活动
        self.choose_expense()  # 选择费用明细
        self.clear_and_sendkeys(ACTIVITY['联系人'], create_name())
        self.clear_and_sendkeys(ACTIVITY['电话'], create_phone())
        self.clear_and_sendkeys(ACTIVITY['地址'], create_gbk(6))
        self.clear_and_sendkeys(ACTIVITY['人数'], random.randint(1, 3))
        self.present_num()  # 赠送数量
        self.present_money()  # 赠送金额
        self.take_photo(flag)  # 上传照片
        self.submit_and_confirm()

    @error_shot
    def groupon_activity(self, flag=None):
        """团购直销活动"""
        # 进入团购直销活动
        self.choose_activity_type(1)
        logging.info(format_str('groupon_activity'))

        self.choose_activity()  # 选择活动
        self.choose_expense()   # 选择费用明细
        self.clear_and_sendkeys(ACTIVITY['单位名称'], create_gbk(5))
        self.clear_and_sendkeys(ACTIVITY['联系人'], create_name())
        self.clear_and_sendkeys(ACTIVITY['电话'], create_phone())
        self.present_num()  # 赠送数量
        self.present_money()    # 赠送金额
        self.take_photo(flag)   # 拍照上传
        self.submit_and_confirm()

    @error_shot
    def feast_activity(self, flag=None):
        """宴席推广活动"""
        # 进入宴席推广活动
        self.choose_activity_type(2)
        logging.info(format_str('feast_activity'))

        # 选择宴席类型
        self.click(ACTIVITY['宴席类型'])
        sleep(1)
        banquets = self.find_elements(ACTIVITY['列表'])
        random.choice(banquets).click()
        sleep(0.5)

        self.choose_activity()  # 选择活动
        self.choose_expense()  # 选择费用明细
        self.clear_and_sendkeys(ACTIVITY['联系人'], create_name())
        self.clear_and_sendkeys(ACTIVITY['电话'], create_phone())
        self.clear_and_sendkeys(ACTIVITY['地址'], create_gbk(6))
        self.clear_and_sendkeys(ACTIVITY['人数'], random.randint(1, 3))
        self.present_num()  # 赠送数量
        self.present_money()  # 赠送金额
        self.take_photo(flag)  # 上传照片
        self.submit_and_confirm()

    @error_shot
    def cultivate_activity_supplement(self, flag=None):
        """消费培育活动-补录"""
        # 选择消费培育活动
        self.choose_activity_supplement_type(0)
        logging.info(format_str('cultivate_activity_supplement'))
        self.choose_activity()  # 选择活动
        self.choose_expense()   # 选择费用明细
        self.clear_and_sendkeys(ACTIVITY['联系人'], create_name())
        self.clear_and_sendkeys(ACTIVITY['电话'], create_phone())
        self.clear_and_sendkeys(ACTIVITY['地址'], create_gbk(6))
        self.clear_and_sendkeys(ACTIVITY['人数'], random.randint(1, 3))
        self.present_num()  # 赠送数量
        self.present_money()    # 赠送金额
        self.upload_photo(flag)  # 上传照片
        self.submit_and_confirm()
        sleep(2)

    @error_shot
    def groupon_activity_supplement(self, flag=None):
        """团购直销活动-补录"""
        # 进入团购直销活动
        self.choose_activity_supplement_type(1)
        logging.info(format_str('groupon_activity_supplement'))

        self.choose_activity()  # 选择活动
        self.choose_expense()  # 选择费用明细
        self.clear_and_sendkeys(ACTIVITY['单位名称'], create_gbk(5))
        self.clear_and_sendkeys(ACTIVITY['联系人'], create_name())
        self.clear_and_sendkeys(ACTIVITY['电话'], create_phone())
        self.present_num()  # 赠送数量
        self.present_money()  # 赠送金额
        self.upload_photo(flag)  # 上传照片
        self.submit_and_confirm()
        sleep(2)

    @error_shot
    def feast_activity_supplement(self, flag=None):
        """宴席推广活动-补录"""
        # 进入宴席推广活动
        self.choose_activity_supplement_type(2)
        logging.info(format_str('feast_activity_supplement'))

        # 选择宴席类型
        self.click(ACTIVITY['宴席类型'])
        sleep(1)
        banquets = self.find_elements(ACTIVITY['列表'])
        random.choice(banquets).click()
        sleep(0.5)

        self.choose_activity()  # 选择活动
        self.choose_expense()  # 选择费用明细
        self.clear_and_sendkeys(ACTIVITY['联系人'], create_name())
        self.clear_and_sendkeys(ACTIVITY['电话'], create_phone())
        self.clear_and_sendkeys(ACTIVITY['地址'], create_gbk(6))
        self.clear_and_sendkeys(ACTIVITY['人数'], random.randint(1, 3))
        self.present_num()  # 赠送数量
        self.present_money()  # 赠送金额
        self.upload_photo(flag)  # 上传照片
        self.submit_and_confirm()
        sleep(2)


if __name__ == '__main__':
    # driver = driver()
    driver = qywx_driver()
    # act = NormalActivity(driver)
    # act.open_wechat_ccloud()
    # for _ in range(1):
    # act.enter_customer_visit()
    # act.normal_activity()
    # act.return_home_page()
    market = MarketingCampaign(driver)
    # market.open_wechat_ccloud()
    market.open_qywx_ccloud()
    # for _ in range(2):
    market.enter_user_center()
    # market.cultivate_activity()
    # market.groupon_activity()
    # market.feast_activity()
    # market.cultivate_activity_supplement()
    market.groupon_activity_supplement(flag=1)
    # market.feast_activity_supplement()
    market.return_home_page()
    #     market.enter_user_center()
    #     market.groupon_activity()
    #     market.return_home_page()
    #     market.enter_user_center()
    #     market.feast_activity()
    #     market.return_home_page()
    #     market.enter_user_center()
    #     market.cultivate_activity_supplement()
    #     market.return_home_page()
    #     market.enter_user_center()
    #     market.groupon_activity_supplement()
    #     market.return_home_page()
    #     market.enter_user_center()
    #     market.feast_activity_supplement()
    #     market.return_home_page()
    #     logging.info('************* 第 {} 次执行完毕 *************'.format(_+1))
