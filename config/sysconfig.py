#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/17 15:05
# @Author  : Bilon
# @File    : sysconfig.py

# 运行主机：端口号
HOST = '127.0.0.1:4723'

# 截图路保存径，绝对路径，也可以用相对路径
SCREENSHOTURL = '..\\screenshot\\'

# 时间样式
ISOTIMEFORMAT = '%Y-%m-%d %H_%M_%S'

# 测试报告生成路径
REPORTURL = '..\\testreport\\'

# 邮件
SMTP_SERVER = 'smtp.qq.com'
FROM_ADDR = '1551658080@qq.com'
PASSWORD = 'wbawewprwmlthffa'
TO_ADDR = ['30884413@qq.com', 'dongpiquo@gmail.com']

# 以下针对微信webview应用
# 默认context
NATIVE = 'NATIVE_APP'

# Webview context
WEBVIEW = 'WEBVIEW_com.tencent.mm:tools'

# 企业微信Webview context
QYWXVIEW = 'WEBVIEW_com.tencent.wework'
