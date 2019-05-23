#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/17 16:10
# @Author  : Bilon
# @File    : eleconfig.py
from selenium.webdriver.common.by import By

PUBLIC = {
    # 微信
    # '武汉珈研': (By.XPATH, '//android.view.View[@text="武汉珈研"]'),
    '消息列表': (By.ID, 'com.tencent.mm:id/b4o'),
    '订单云平台': (By.ID, 'com.tencent.mm:id/am1'),
    '退出应用' : (By.ID, 'com.tencent.mm:id/k5'),

    # 企业微信
    '工作台' : (By.XPATH, '//android.widget.TextView[@text="工作台"]'),
    '慧订货' : (By.XPATH, '//android.widget.TextView[@text="慧订货"]'),

    '账套列表': (By.TAG_NAME, 'a'),
    '底部首页菜单': (By.XPATH, '//p[text()="首页"]'),
    '底部首页按钮': (By.XPATH, '//button[text()="首页"]'),
    '悬浮图标': (By.ID, 'button'),
    '返回首页': (By.XPATH, '//a[contains(text(),"首页")]'),
    '个人中心': (By.XPATH, '//p[text()="我的"]'),
    '客户拜访': (By.ID, 'customerVisits'),
    '客户列表': (By.XPATH, '//*[@id="customerList"]/div'),
    '弹层': 'layui-layer-iframe1',    # 弹层的id
    '确定按钮': (By.XPATH, '//a[text()="确定"]'),
    '定位地址': (By.ID, 'location-span'),
    '刷新定位': (By.ID, 'refresh'),

    '草稿箱角标': (By.XPATH, '//*[@id="home"]/div[4]/div[2]/a[5]/span'),
    '草稿箱': (By.XPATH, '//p[text()="拜访草稿箱"]'),
    '清空草稿箱': (By.TAG_NAME, 'img'),

    # 拍照
    '新增照片': (By.CLASS_NAME, 'picture1BtnId'),
    '拍照': (By.ID, 'com.android.camera:id/shutter_button'),
    '确认照片': (By.ID, 'com.android.camera:id/done_button'),
    '企业微信二次确认': (By.ID, 'com.tencent.wework:id/e2v'),

    # 本地照片上传
    '选择从文件上传': (By.XPATH, '//android.widget.TextView[@text="文件"]'),   # 微信

    '选择其他方式上传': (By.XPATH, '//android.widget.TextView[@text="其他方式"]'),  # 企业微信
    '企业微信步骤二': (By.XPATH, '//android.widget.ImageButton[@content-desc="显示根目录"]'),
    '获取照片列表': (By.ID, 'com.android.documentsui:id/thumbnail'),

    '关闭按钮': (By.XPATH, '//span[text()="关闭"]'),
    '列表': (By.CLASS_NAME, 'weui-check_label'),

}

ORDER = {

    # 订单相关元素
    '合计数量': (By.ID, 'totalNum'),
    '大单位输入框': (By.ID, 'bigNum'),
    '小单位输入框': (By.ID, 'smallNum'),
    '确认输入': (By.ID, 'confirm-input'),
    '购物车': (By.ID, 'shoppingCart'),
    '添加商品': (By.ID, 'addGoods'),
    '勾选赠品': (By.NAME, 'isGift'),
    '下单': (By.ID, 'placeOrder'),
    '选择客户': (By.XPATH, '//*[@id="form"]/div[1]/div[1]'),
    '客户': (By.ID, 'customerInfo'),
    '侧边客户列表': (By.ID, 'combin-filter'),
    '提交订单': (By.ID, 'placeOrder'),
    '聚合下单': (By.ID, 'order'),
    '拜访完成': (By.ID, 'visitEnd'),
    '删除商品': (By.CLASS_NAME, 'icon-trash-o'),
    '首页下单': (By.XPATH, '//*[@id="home"]/div[3]/div[2]/a[1]'),
    '输入商品数量': (By.XPATH, '/html/body/div[5]/input'),
    '删除确认': (By.XPATH, '//a[text()="确定"]'),
    '下单二次确认': (By.XPATH, '/html/body/div[4]/div[3]/a[2]'),
    '跳转订单列表': (By.XPATH, '/html/body/div[4]/div[2]/a[1]'),
    '拜访完成二次确认': (By.XPATH, '//a[contains(text(),"确定")]'),
}

ACTIVITY = {
    '活动快捷执行': (By.ID, 'activity_quick'),
    '活动': (By.ID, 'activity_title'),
    '费用明细': (By.ID, 'expenses_ids'),
    '可用数量': (By.ID, 'ableNum'),
    '赠送数量': (By.ID, 'apply_num1'),
    '补录赠送数量': (By.ID, 'apply_num'),
    '可用金额': (By.ID, 'ableMoney'),
    '赠送金额': (By.ID, 'apply_amount1'),
    '补录赠送金额': (By.ID, 'apply_amount'),
    '宴席类型': (By.ID, 'banquet_type'),
    '单位名称': (By.ID, 'companyName'),
    '联系人': (By.ID, 'customerNames'),    # 联系人/培育对象
    '电话': (By.ID, 'customerMobile'),
    '地址': (By.ID, 'customerAddress'),
    '人数': (By.ID, 'people'),    # 人数/桌数
    '列表': (By.CLASS_NAME, 'weui-check_label'),    # 活动列表和费用明细列表
    # '提交': (By.CLASS_NAME, 'weui-footer'),
    '提交': (By.XPATH, '//a[text()="提交"]'),
    '选择营销活动': (By.CLASS_NAME, 'weui-input'),    # 营销推广活动选择
    '确定': (By.XPATH, '//a[text()="确定"]'),
    '继续上传': (By.XPATH, '//a[contains(text(),"继续上传")]'),
    '关闭弹层': (By.XPATH, '/html/body/div[2]'),
    '营销推广': (By.XPATH, '//p[text()="营销推广"]'),
    '营销补录': (By.XPATH, '//p[text()="营销补录"]'),
    '营销提交': (By.XPATH, '//button[text()="提交"]'),
}

CUSTOMER = {
    '新增客户': (By.XPATH, '//p[text()="新增客户"]'),
    '客户名': (By.ID, 'customer_name'),
    '联系人': (By.ID, 'contact'),
    '电话': (By.ID, 'mobile'),
    '客户类型': (By.ID, 'default_customer_type'),
    '客户等级': (By.ID, 'subType'),
    '省市区': (By.ID, 'delivery-address'),
    '详细地址': (By.ID, 'address'),
    '添加图片': (By.ID, 'uploaderInput'),
    '新增': (By.ID, 'add'),
    '完成': (By.XPATH, '//a[text()="完成"]'),
    '确定': (By.XPATH, '//a[text()="确定"]'),
    # addcustomer_entrance : '//*[@id="home"]/div[3]/div[2]/a[2]'  # 新增客户功能入口
    '列表': (By.CLASS_NAME, 'weui-check_label'),

    # 常规拜访
    '常规拜访': (By.ID, 'photo'),
    '拜访完成': (By.ID, 'visitEnd'),
    '提交': (By.XPATH, '//button[text()="提交"]'),
    '备注': (By.ID, 'question_desc'),
    '拜访补录': (By.ID, 'photoBL'),
}

AUDIT = {
    '订单审核': (By.XPATH, '//p[text()="订单审核"]'),
    '客户审核': (By.XPATH, '//p[text()="客户审核"]'),
    '拜访审核': (By.XPATH, '//p[text()="拜访审核"]'),
    '活动审核': (By.XPATH, '//p[text()="活动审核"]'),
    '同意': (By.XPATH, '//div[text()="同意"]'),
    '拒绝': (By.XPATH, '//div[text()="拒绝"]'),
    '确认': (By.XPATH, '//span[text()="确认"]'),
    '通过': (By.XPATH, '//span[text()="通过"]'),
    '取消': (By.XPATH, '//span[text()="取消"]'),
    '订单拒绝理由': (By.NAME, 'refuseReson'),
    '拜访拒绝理由': (By.XPATH, '//*[@id="refuse-reason"]/select'),
    '备注': (By.ID, 'comment'),
    '返回首页': (By.CLASS_NAME, 'return_index'),
}

REFUND = {
    '申请退货': (By.XPATH, '//p[text()="申请退货"]'),
    '退货按钮': (By.ID, 'refund'),
    '自由退货': (By.XPATH, '/html/body/div[1]/a/img'),
    '日期筛选': (By.ID, 'date'),
    '下一步': (By.ID, 'placeOrder'),
    '退货仓库': (By.ID, 'warehouseName'),
    '确定': (By.XPATH, '//a[text()="确定"]'),
    '提交订单': (By.XPATH, '//button[text()="提交订单"]'),
    '否': (By.XPATH, '//a[text()="否"]'),
    '查看订单': (By.XPATH, '//a[text()="查看订单"]'),
}

OUTPUT = {
    '订单状态': (By.ID, 'status'),
    '日期筛选': (By.ID, 'date'),
    '单个出库': (By.ID, 'allOut'),
    '批量出库': (By.ID, 'batchOutStock'),
    '订单列表': (By.CLASS_NAME, 'list-layer'),
    '出库单': (By.XPATH, '//p[text()="出库单"]'),
    '确定': (By.XPATH, '//a[text()="确定"]'),
    '二次确认': (By.XPATH, '//span[text()="确认"]'),
}
