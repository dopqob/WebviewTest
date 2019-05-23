#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/17 11:44
# @Author  : Bilon
# @File    : mail.py
import mimetypes
import os
import smtplib
import threading
import time
import logging
from datetime import datetime
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from os.path import getsize


class Email(object):
    mail_cfgs = {'msg_from': '1551658080@qq.com',  # 发送邮箱
                 # 'password': 'latimgqpunpgcbeb',  # 邮箱密码（授权码 30884413）
                 'password': 'wbawewprwmlthffa',  # 邮箱密码（授权码 1551658080）
                 'msg_to': ['30884413@qq.com'],  # 接收邮箱
                 'msg_cc': ['1335150450@qq.com'],  # 抄送邮箱
                 'msg_subject': 'APP测试报告',  # 邮件主题
                 # 'msg_content': 'Hi, boy! Just do it, python!',  # 邮件内容
                 # 'attach_file': r'.\^ccloud$\*\.py',  # 附件
                 'attach_file': '../testreport',  # 附件
                 # 'msg_date': time.ctime()  # 邮件发送时间戳
                 }

    # 初始化相关配置信息
    def __init__(self):
        self.kwargs = self.mail_cfgs
        self.smtp_server = 'smtp.qq.com'    # QQ邮箱
        self.MAX_FILE_SIZE = 10 * 1024 * 1024   # 附件大小10M

    # 获取配置参数
    def __get_cfg(self, key, throw=True):
        cfg = self.kwargs.get(key)
        if throw and (cfg is None or cfg == ''):
            raise Exception("The configuration can't be empty", 'utf-8')
        return cfg

    # 初始化读取到的参数信息
    def __init_cfg(self):
        self.msg_from = self.__get_cfg('msg_from')
        self.password = self.__get_cfg('password')
        self.msg_to = self.__get_cfg('msg_to')
        self.msg_cc = self.__get_cfg('msg_cc', throw=False)
        self.msg_subject = self.__get_cfg('msg_subject')
        # self.msg_content = self.__get_cfg('msg_content')
        # self.msg_date = self.__get_cfg('msg_date')
        self.attach_file = self.__get_cfg('attach_file', throw=False)

    # 登录SMTP服务器
    def login_server(self):
        # server = smtplib.SMTP(self.smtp_server, 25)     # 其他邮箱
        server = smtplib.SMTP_SSL(self.smtp_server, 465)    # QQ邮箱
        server.set_debuglevel(1)
        server.login(self.msg_from, self.password)
        return server

    # 获取最新报告的地址
    def acquire_report_address(self):
        # 获取当前年月日
        # now = datetime.now().strftime('%Y-%m-%d')
        # new_address = self.attach_file + '\\' + now

        # 测试报告文件夹中的所有文件加入到列表
        # test_reports_list = os.listdir(new_address)
        test_reports_list = os.listdir(self.attach_file)
        # 按照升序排序生成新的列表
        new_test_reports_list = sorted(test_reports_list)
        # 获取最新的测试报告
        the_last_report = new_test_reports_list[-1]
        # 最新的测试报告的地址
        the_last_report_address = os.path.join(self.attach_file, the_last_report)
        return the_last_report_address

    # 处理邮件内容
    def get_main_msg(self, new_report):
        """
        调用了两个方法：_format_addr()和get_attach_file()
        _format_addr()来格式化一个邮件地址,注意不能简单地传入name addr@example.com，因为如果包含中文，需要通过Header对象进行编码
        get_attach_file()是用来获取附件的相关信息
        """
        # 读取测试报告中的内容作为邮件的内容
        with open(new_report, 'r', encoding='utf8') as f:
            mail_body = f.read()

        msg = MIMEMultipart()
        # message content
        msg.attach(MIMEText(mail_body, 'html', 'utf-8'))

        msg['From'] = self._format_addr(f'Bilon {self.msg_from}')    # 发件人
        msg['To'] = self._format_addr(self.msg_to)   # 收件人
        msg['Cc'] = self._format_addr(self.msg_cc)   # 抄送人
        msg['Subject'] = Header(self.msg_subject, 'utf-8')
        # msg['Date'] = self.msg_date

        # attachment content
        attach_file = self.get_attach_file(new_report)
        if attach_file is not None:
            msg.attach(attach_file)
        return msg

    # 格式化邮件地址
    @staticmethod
    def _format_addr(s):
        if isinstance(s, list):
            addr_list = []
            for _ in s:
                name, addr = parseaddr(_)
                addr = formataddr((Header(name, 'utf-8').encode(), addr))
                addr_list.append(addr)
            return ','.join(addr_list)
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    # 获取附件的相关信息
    def get_attach_file(self, new_report):
        """
        带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身，所以，可以构造一个MIMEMultipart对象代表邮件本身，
        然后往里面加上一个MIMEText作为邮件正文，再继续往里面加上表示附件的MIMEBase对象即可，
        我们把附件那部分抽取到get_attach_file()方法中
        """
        if new_report is not None and new_report != '':
            try:
                if getsize(new_report) > self.MAX_FILE_SIZE:  # 附件大于10M抛出异常
                    raise Exception('The attachment is too large and the upload failed!!')

                with open(new_report, 'rb') as file:
                    # mimetypes是python自带的标准库，可以根据文件的后缀名直接得到文件的MIME类型
                    ctype, encoding = mimetypes.guess_type(new_report)
                    if ctype is None or encoding is not None:
                        ctype = 'application/octet-stream'
                    maintype, subtype = ctype.split('/', 1)
                    mime = MIMEBase(maintype, subtype)
                    mime.set_payload(file.read())
                    # 设置信息头
                    mime.add_header('Content-Disposition', 'attachment',
                                    filename=os.path.basename(new_report))
                    mime.add_header('Content-ID', '<0>')
                    mime.add_header('X-Attachment-Id', '0')
                    # 设置编码规则
                    encoders.encode_base64(mime)
                    return mime
            except Exception as e:
                logging.error('%s......' % e)
                return None
        else:
            return None

    # 发送邮件
    def send(self):
        try:
            # initialize the configuration file
            self.__init_cfg()
            # log on to the SMTP server and verify authorization
            server = self.login_server()
            # mail content
            new_report = self.acquire_report_address()
            msg = self.get_main_msg(new_report)
            # send mail
            server.sendmail(self.msg_from, self.msg_to + self.msg_cc, msg.as_string())
            # server.sendmail(self.msg_from, self.msg_to, msg.as_string())
            server.quit()
            logging.info("Send succeed!!")
        except smtplib.SMTPException:
            logging.error("Error:Can't send this email!!")


# 循环发送，每5分钟向收件人邮箱发送一封邮件
def circle_send(control):
    time_intvl = 5 * 60
    start_time = int(time.time())
    print(start_time)
    while True:
        end_time = int(time.time())
        cost_time = end_time - start_time
        # print(cost_time)
        if cost_time == time_intvl:
            control.send()
            start_time = end_time
            print('regular send email....%s' % time.ctime(start_time))
        else:
            pass


# 定时发送：每天23:00定时发送邮件
def regular_send(control):
    regular_hour = 23
    regular_min = 00
    regular_sec = 00
    while True:
        current_time = time.localtime(time.time())
        # print(current_time.tm_min)
        if (current_time.tm_hour == regular_hour) \
                and (current_time.tm_min == regular_min) \
                and (current_time.tm_sec == regular_sec):
            control.send()
            print('send a email at 23:00:00 every day....')
        else:
            pass


if __name__ == "__main__":

    manager = Email()
    manager.send()

    # threading.Thread(target=manager.circle_send, args=(manager,)).start()   # 循环发送
    # threading.Thread(target=manager.regular_send, args=(manager,)).start()    # 定时发送
