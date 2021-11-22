"""
@author:96978
@file:Testweibo.py
@time:2021/11/19
"""
import time

from appium import webdriver
from unittest import TestCase
from operation import operation


class TestWeibo(TestCase):

	def setUp(self) -> None:
		url = '127.0.0.1:4723/wd/hub'
		path = {
				"deviceName": "emulator-5554",
				"platformName": "Android",
				"platformVersion": "7.1.2",
				"appPackage": "com.sina.weibo",
				"appActivity": "com.sina.weibo.SplashActivity"
			}
		self.driver= webdriver.Remote(url,path)
		operation(self.driver).start()

	def testHomepage(self):
		homepage=operation(self.driver)
		homepage.homepage()
		result=homepage.homepageSuccess()
		print(result)
		time.sleep(2)
		self.assertEqual('微博正文',result)

	def testVideo(self):
		video=operation(self.driver)
		video.video()
		result=video.videoSuccess()
		print(result)
		time.sleep(2)
		self.assertEqual('转发微博',result)

	def testSearch(self):
		search=operation(self.driver)
		search.search()
		result=search.searchSuccess()
		print(result)
		time.sleep(2)
		self.assertEqual('微博正文',result)

	def testNews(self):
		news=operation(self.driver)
		news.news()
		result=news.newsSuccess()
		print(result)
		time.sleep(2)
		self.assertEqual('短信验证码登录',result)


