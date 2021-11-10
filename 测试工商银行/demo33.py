"""
@author:96978
@file:demo33.py
@time:2021/11/09
"""
import unittest
import zmail
test = unittest.defaultTestLoader.discover(r'D:\Pythonproject\pythonproject1\pycode1', pattern='day14.py')
runner = unittest.TextTestRunner()
runner.run(test)

server=zmail.server('969785562@qq.com','xysoisvpavovbdfd')
send=['969785562@qq.com',]
mail_content={
	'subject': '中国工商银行测试结果', #主题
	'attachments': 'D:\Pythonproject\pythonproject1\pycode1\data.xls', # 附件内容（最好使用绝对路径，若你电脑没有这个文件会造成错误）
	'headers':'中国工商银行测试结果'
}
server.send_mail(send,mail_content)