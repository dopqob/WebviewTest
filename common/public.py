#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 10:08
# @Author  : Bilon
# @File    : public.py
import random
import time
import logging
from common.base import BaseOperate
from common.decorator import error_shot
from config.eleconfig import *
from common.driver import *
from util.tools import format_str


class Common(BaseOperate):
    """封装公共方法类"""

    @error_shot
    def open_wechat_ccloud(self):
        """进入微信公众号'武汉珈研'里的订单云平台"""
        logging.info(format_str('open_wechat_ccloud'))

        # self.click(PUBLIC['武汉珈研'])
        m_list = self.find_elements(PUBLIC['消息列表'])
        for m in m_list:
            if m.text == '武汉珈研':
                m.click()
                break
        self.find_elements(PUBLIC['订单云平台'])[0].click()
        time.sleep(2)
        self.switch_to_webview()    # 切换到H5视图
        self.choose_accout()

    @error_shot
    def open_qywx_ccloud(self):
        """企业微信进入'慧订货'"""
        logging.info(format_str('open_qywx_ccloud'))

        self.click(PUBLIC['工作台'])
        self.click(PUBLIC['慧订货'])
        self.switch_to_webview()  # 切换到h5视图
        self.choose_accout()
        self.clear_drafts()

    @error_shot
    def choose_accout(self, name=None):
        """
        如果出现选账套页面，进入name账套，如果没指定name，默认选第一个
        :param name: 账套名称
        """
        title = self.driver.title  # 获取当前页面title
        if title == '选择用户':     # 如果页面title是选择用户，说明是进入了选择账套页面
            logging.info(format_str('choose_accout'))
            sets = self.find_elements(PUBLIC['账套列表'])
            if name:
                for s in sets:
                    if s.text == name:
                        s.click()
                        return
            sets[0].click()

    @error_shot
    def return_home_page(self):
        """返回首页"""
        logging.info(format_str('return_home_page'))

        time.sleep(2)
        if self.is_exists(PUBLIC['底部首页菜单']):
            self.click(PUBLIC['底部首页菜单'])
        elif self.is_exists(PUBLIC['悬浮图标']):
            self.click(PUBLIC['悬浮图标'])
            self.click(PUBLIC['返回首页'])
        else:
            self.click(PUBLIC['底部首页按钮'])

    @error_shot
    def enter_user_center(self):
        """进入个人中心"""
        logging.info(format_str('enter_user_center'))
        self.click(PUBLIC['个人中心'])

    @error_shot
    def enter_customer_visit(self):
        """
        进入(聚合)客户列表并随机选择一个客户
        """
        logging.info(format_str('enter_customer_visit'))

        self.click(PUBLIC['客户拜访'])
        time.sleep(2)

        customers = self.find_elements(PUBLIC['客户列表'])  # 获取当前页客户
        random.choice(customers).click()  # 随机选一个用户
        time.sleep(1)

        self.switch_to_frame(PUBLIC['弹层'])  # 切换到弹层

        if self.is_exists(PUBLIC['确定按钮']):  # 如果出现上个拜访未完成的提示，点击确定
            self.click(PUBLIC['确定按钮'])

        # 定位失败时刷新定位
        if self.is_text_in_element(PUBLIC['定位地址'], '请手动刷新定位'):
            self.click(PUBLIC['刷新定位'])
            time.sleep(3)

    def clear_drafts(self):
        """清空草稿箱"""
        if self.element_is_dispalyed(PUBLIC['草稿箱角标']):
            logging.info(format_str('start clear drafts...'))
            self.click(PUBLIC['草稿箱'])
            self.click(PUBLIC['清空草稿箱'])
            self.click(PUBLIC['确定按钮'])
            self.return_home_page()

    def take_photo(self, flag=None):
        """
        拍照上传
        :param flag: 用来标识是否是企业微信，默认微信
        """
        logging.info(format_str('take_photo'))

        for i in range(random.randint(1, 5)):
            self.click(PUBLIC['新增照片'])
            time.sleep(1)

            self.switch_to_native()  # 切换到NATIVE视图控制相机拍照
            self.click(PUBLIC['拍照'])
            time.sleep(1)
            self.click(PUBLIC['确认照片'])
            if flag:
                self.click(PUBLIC['企业微信二次确认'])
            time.sleep(3)  # 等待图片上传完成
            self.switch_to_webview()  # 切换到H5视图继续操作

    def upload_photo(self, flag=None):
        """
        从相册选择文件上传
        :param flag: 用来标识是否是企业微信，默认微信
        """
        logging.info(format_str('upload_photo'))

        for i in range(random.randint(1, 4)):
            self.click(PUBLIC['新增照片'])
            time.sleep(1)
            self.switch_to_native()  # 切换到NATIVE_APP视图控制照片选择
            if flag:
                self.click(PUBLIC['选择其他方式上传'])  # 企业微信选择其他方式上传
                self.click(PUBLIC['企业微信步骤二'])   # 企业微信步骤二
            else:
                self.click(PUBLIC['选择从文件上传'])    # 微信选择从文件上传图片
            time.sleep(1)
            photos = self.find_elements(PUBLIC['获取照片列表'])
            random.choice(photos).click()
            time.sleep(3)  # 等待图片上传完成

            self.switch_to_webview()  # 切换到H5视图继续操作
            time.sleep(0.5)
            if self.is_exists(PUBLIC['关闭按钮']):
                self.click(PUBLIC['关闭按钮'])

    @error_shot
    def exit(self):
        """退出应用"""
        self.switch_to_native()
        self.click(PUBLIC['退出应用'])


if __name__ == '__main__':
    driver = driver()
    # driver = qywx_driver()
    common = Common(driver)
    common.open_wechat_ccloud()
    time.sleep(5)
