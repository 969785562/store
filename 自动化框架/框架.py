"""
@author:96978
@file:框架.py
@time:2021/11/17
"""

from HTMLTestRunner import HTMLTestRunner
import unittest
import os
import zmail
tests=unittest.defaultTestLoader.discover(os.getcwd(),pattern='Test*.py')

runner=HTMLTestRunner.HTMLTestRunner(
	title='HKR自动化测试报告',
	description='HKR测试报告',
	verbosity=1,
	stream=open(file='HKR.html',mode='w+',encoding='utf-8')

)

runner.run(tests)


server=zmail.server('969785562@qq.com','xysoisvpavovbdfd')
send=['969785562@qq.com',]
att=['D:\Pythonproject\pythonproject1\pycode4\HKR.html','D:\Python自动化测试\其他课程\自动化\day03\HKR.xls']
with open('D:\Pythonproject\pythonproject1\pycode4\HKR.html','r',encoding='utf-8') as f:
	content= f.read()
mail_content={
	'subject': 'HKR自动化测试报告', #主题
	'attachments': att, # 附件内容（最好使用绝对路径，若你电脑没有这个文件会造成错误）
	# 'content_html':content,
	'headers':'HKR自动化测试报告'
}
server.send_mail(send,mail_content)

