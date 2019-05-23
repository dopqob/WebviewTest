#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 9:36
# @Author  : Bilon
# @File    : base.py
import logging
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from config.sysconfig import *


class BaseOperate(object):
    def __init__(self, driver):
        self.driver = driver

    # 查找元素
    def find_element(self, loc):
        """
        重新封装的find方法，接受元祖类型的参数，默认等待元素10秒，寻找失败时自动截图
        :param loc:元组类型,必须是(By.NAME, 'username')这样的结构
        :return:元素对象webelement
        """
        try:
            webelement = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*loc))
            return webelement
        except (TimeoutException, NoSuchElementException) as e:
            logging.warning(f'页面中未能找到 {loc} 元素：', e)

    # 查找一组元素
    def find_elements(self, loc):
        """
        重新封装find_elements方法
        :param loc: 定位方式，如(By.ID, "kw"),把两个参数合并为一个,*号是把两个参数分开传值
        :return: 返回一个元素列表
        """
        try:
            if len(self.driver.find_elements(*loc)):
                return self.driver.find_elements(*loc)
        except Exception as e:
            logging.warning(f"{self} 页面中未能找到 {loc} 元素：", e)

    # 判断元素文本
    def is_text_in_element(self, loc, text):
        try:
            WebDriverWait(self.driver, 2).until(EC.text_to_be_present_in_element(loc, text))
            return True
        except (TimeoutException, NoSuchElementException) as e:
            return False

    def is_page_has_text(self, text):
        """
        判断当前页面是否存在指定的文字
        :param text:字符串类型，要判断是否存在的文字
        :return:布尔值，True代表存在，False代表不存在
        """
        nowtime = time.time()
        while self.driver.page_source.find(text) < 0:
            time.sleep(1)
            if time.time() - nowtime >= 5000:
                return False
        return True

    # 判断元素的value属性
    def is_value_element(self, loc, text):
        try:
            WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element_value(loc, text))
            return True
        except (TimeoutException, NoSuchElementException) as e:
            return False

    # 判断元素是否被定位到
    def is_exists(self, loc):
        try:
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(loc))
            return True
        except (TimeoutException, NoSuchElementException) as e:
            return False

    # 判断元素是否已经不存在,不存在了返回True,还存在就返回False
    def element_is_disappeared(self, loc, timeout=30):
        is_disappeared = WebDriverWait(self.driver, timeout, 1, ElementNotVisibleException).until_not(
            lambda x: x.find_element(*loc).is_displayed())
        return is_disappeared

    # 判断元素是否可见
    def element_is_dispalyed(self, loc, timeout=5):
        return WebDriverWait(self.driver, timeout, 1, ElementNotVisibleException).until(
            lambda x: x.find_element(*loc)).is_displayed()

    # 封装一个send_keys
    def clear_and_sendkeys(self, loc, text):
        self.find_element(loc).clear().send_keys(text)

    # 封装一个click
    def click(self, loc):
        self.find_element(loc).click()

    # 封装一个text
    def get_text(self, loc):
        return self.find_element(loc).text

    # 屏幕滑动方法
    def swipe_down(self):
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 500)

    def swipe_up(self):
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)

    def swipe_left(self):
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, 500)

    def swipe_rigth(self):
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width * 4 / 5, height / 2, width / 5, height / 2, 500)

    def switch_to_last_handle(self):
        """
        在打开的窗口里选择最后一个
        :return:None
        """
        all_handles = self.driver.window_handles
        self.driver.switch_to.window(all_handles[-1])

    def switch_to_native(self):
        self.driver.switch_to.context(NATIVE)

    def switch_to_webview(self):
        contexts = self.driver.contexts
        if WEBVIEW in contexts:
            self.driver.switch_to.context(WEBVIEW)
            if self.driver.title == '搜一搜':  # 如果页面的title是'搜一搜'，需要切换handle
                self.switch_to_last_handle()
        else:
            time.sleep(3)
            self.driver.switch_to.context(QYWXVIEW)

    # 切换iframe
    def switch_to_frame(self, _id):
        """
        切换iframe
        :param _id: iframe的id
        """
        self.driver.switch_to.frame(_id)

    def take_screenshot(self, img_name):
        """
        获取当前屏幕的截图
        :param img_name: 截图名称
        """
        logging.warning('{:-^60}'.format(' error_screenshot '))

        try:
            self.switch_to_native()
            day = time.strftime("%Y-%m-%d", time.localtime(time.time()))
            shot_path = SCREENSHOTURL + day
            shot_time = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
            img_type = '.png'
            if not os.path.exists(shot_path):
                os.makedirs(shot_path)
            filename = shot_path + "\\" + shot_time + "_" + img_name + img_type
            self.driver.get_screenshot_as_file(filename)
        except Exception as e:
            logging.warning('截图失败: ', e)
