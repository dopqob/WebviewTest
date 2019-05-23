#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/17 19:13
# @Author  : Bilon
# @File    : decorator.py
import logging


def error_shot(func):
    """错误截图装饰器"""
    name = func.__name__

    def wrapper(self, *args, **kwargs):
        try:
            func(self, *args, **kwargs)
        except Exception as e:
            self.take_screenshot(name)  # 封装的截图方法
            logging.error(e)
            raise e
    return wrapper
