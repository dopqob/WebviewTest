#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 9:32
# @Author  : Bilon
# @File    : driver.py
import yaml
import logging.config
from appium import webdriver
from config.sysconfig import *


CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()

with open('../config/caps.yaml', 'r', encoding='utf-8') as f:
    data = yaml.load(f)


def driver():
    """启动微信"""

    desired_caps = {}
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['chromeOptions'] = data['chromeOptions']

    # 出现StackOverflowError UIAutomatorTestRunner时加上此配置
    desired_caps['disableAndroidWatchers'] = data['disableAndroidWatchers']

    desired_caps['platformName'] = data['platformName']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['noReset'] = data['noReset']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']

    # logging.info(' -----> Open Wechat and prepare to run testcase')

    mydriver = webdriver.Remote('http://' + HOST + '/wd/hub', desired_caps)
    mydriver.implicitly_wait(20)
    return mydriver


def qywx_driver():
    """启动企业微信"""

    desired_caps = {}
    desired_caps['appPackage'] = data['appPackage_qywx']
    desired_caps['appActivity'] = data['appActivity_qywx']
    desired_caps['chromeOptions'] = data['chromeOptions_qywx']

    # 出现StackOverflowError UIAutomatorTestRunner时加上此配置
    desired_caps['disableAndroidWatchers'] = data['disableAndroidWatchers']

    desired_caps['platformName'] = data['platformName']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['noReset'] = data['noReset']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']

    # logging.info(' ----> Open 企业微信 and prepare to run testcase')

    mydriver = webdriver.Remote('http://' + HOST + '/wd/hub', desired_caps)
    mydriver.implicitly_wait(20)
    return mydriver


if __name__ == '__main__':
    driver()
    # qywx_driver()
