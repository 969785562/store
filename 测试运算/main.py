"""
@author:96978
@file:main.py
@time:2021/11/05
"""
from HTMLTestRunner import HTMLTestRunner
import unittest

test = unittest.defaultTestLoader.discover(r'D:\Pythonproject\pythonproject1\pycode1', pattern='Test*.py')

runner = HTMLTestRunner.HTMLTestRunner(
	title='计算器测试报告',
	description='计算器测试报告',  # 副标题
	verbosity=1,
	stream=open(file='计算器.html', mode='w+', encoding='utf-8')

)

runner.run(test)

