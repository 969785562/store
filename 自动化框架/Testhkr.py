"""
@author:96978
@file:Testhkr.py
@time:2021/11/17
"""
from ddt import ddt
from ddt import data
from unittest import TestCase
from selenium import webdriver
from InitPage import InitPage
from day2 import Logintest
import time

@ddt()
class Testhkr(TestCase):

	Initpage=InitPage()


	def setUp(self) -> None:
		self.driver = webdriver.Chrome()
		self.driver.get('http://localhost:8080/HKR')
		self.driver.maximize_window()

	def tearDown(self) -> None:
		self.driver.quit()





	@data(*Initpage.xldata(1))
	def testloginSuccess(self,testdata):
		username=testdata['username']
		password=testdata['password']
		expect=testdata['expect']
		num=testdata['num']
		login=Logintest(self.driver)
		login.login(username,password)
		result=login.getLoginSuccess()
		time.sleep(3)
		Initpage = InitPage()
		if expect == result:
			print(Initpage.xlw(num,'通过'))
		else:
			print(Initpage.xlw(num,'未通过'))
	# 	断言
		self.assertEqual(expect,result)





	@data(*Initpage.xldata(2))
	def testloginError(self,testdata):
		username = testdata['username']
		password = testdata['password']
		expect = testdata['expect']
		num = testdata['num']

		login = Logintest(self.driver)

		login.login(username,password)
		result=login.getLoginError()

		time.sleep(3)
		Initpage = InitPage()
		if expect == result:
			print(Initpage.xlw(num,'通过'))
		else:
			print(Initpage.xlw(num,'未通过'))

		self.assertEqual(expect,result)

