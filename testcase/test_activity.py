#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 11:21
# @Author  : Bilon
# @File    : test_activity.py
import logging
import unittest
from HTMLTestRunner import HTMLTestRunner
from common.myunit import MyTest
from operation.activity import NormalActivity, MarketingCampaign
from util.tools import create_report_file


class ActivityTest(MyTest):
    """活动测试"""

    def test_normal_activity(self):
        """活动快捷执行"""
        logging.info('{:*^60}'.format(' 活动快捷执行 '))
        act = NormalActivity(self.driver)
        act.open_wechat_ccloud()
        act.clear_drafts()
        act.enter_customer_visit()
        act.normal_activity()

    # @unittest.skip('消费培育活动')
    def test_cultivate_activity(self):
        """消费培育活动"""
        logging.info('{:*^60}'.format(' 消费培育活动 '))
        act = MarketingCampaign(self.driver)
        act.open_wechat_ccloud()
        act.clear_drafts()
        act.enter_user_center()
        act.cultivate_activity()
        self.assertEqual(self.driver.title, '营销推广')

    # @unittest.skip('团购直销活动')
    def test_groupon_activity(self):
        """团购直销活动"""
        logging.info('{:*^60}'.format(' 团购直销活动 '))
        act = MarketingCampaign(self.driver)
        act.open_wechat_ccloud()
        act.clear_drafts()
        act.enter_user_center()
        act.groupon_activity()
        self.assertEqual(self.driver.title, '营销推广')

    # @unittest.skip('宴席推广活动')
    def test_feast_activity(self):
        """宴席推广活动"""
        logging.info('{:*^60}'.format(' 宴席推广活动 '))
        act = MarketingCampaign(self.driver)
        act.open_wechat_ccloud()
        act.clear_drafts()
        act.enter_user_center()
        act.feast_activity()
        self.assertEqual(self.driver.title, '营销推广')

    def test_cultivate_supplement(self):
        """消费培育活动-补录"""
        logging.info('{:*^60}'.format(' 消费培育活动-补录 '))
        act = MarketingCampaign(self.driver)
        act.open_wechat_ccloud()
        act.enter_user_center()
        act.cultivate_activity_supplement()
        self.assertEqual(self.driver.title, '营销推广补录')

    def test_groupon_supplement(self):
        """团购直销活动-补录"""
        logging.info('{:*^60}'.format(' 团购直销活动-补录 '))
        act = MarketingCampaign(self.driver)
        act.open_wechat_ccloud()
        act.enter_user_center()
        act.groupon_activity_supplement()
        self.assertEqual(self.driver.title, '营销推广补录')

    def test_feast_supplement(self):
        """宴席推广活动-补录"""
        logging.info('{:*^60}'.format(' 宴席推广活动-补录 '))
        act = MarketingCampaign(self.driver)
        act.open_wechat_ccloud()
        act.enter_user_center()
        act.feast_activity_supplement()
        self.assertEqual(self.driver.title, '营销推广补录')


if __name__ == '__main__':
    file_path = create_report_file()
    with open(file_path, 'wb') as f:
        unittest.main(testRunner=HTMLTestRunner(stream=f, title=u'Ccloud测试报告', description=u'测试结果:'))
