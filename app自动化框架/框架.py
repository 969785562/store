"""
@author:96978
@file:框架.py
@time:2021/11/17
"""
import time

from HTMLTestRunner import HTMLTestRunner
import unittest
import os
import zmail
tests=unittest.defaultTestLoader.discover(os.getcwd(),pattern='Test*.py')
file=open(file='weibo.html',mode='w+',encoding='utf-8')
runner=HTMLTestRunner.HTMLTestRunner(
	title='app自动化测试报告',
	description='app测试报告',
	verbosity=1,
	stream=file
)
runner.run(tests)
file.close()
server=zmail.server('969785562@qq.com','vmzeyigtqpbfbdca')
send=['969785562@qq.com',]
att=['D:\Pythonproject\pythonproject1\weibo\weibo.html',]
with open('D:\Pythonproject\pythonproject1\weibo\weibo.html','r',encoding='utf-8') as f:
	content= f.read()
mail_content={
	'subject': 'app自动化测试报告', #主题
	'content_text':'微博测试邮件',
	'attachments': att, # 附件内容（最好使用绝对路径，若你电脑没有这个文件会造成错误）
	# 'content_html':content,
	'headers':'app自动化测试报告'
}
server.send_mail(send,mail_content)

