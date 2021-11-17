"""
@author:96978
@file:day2.py
@time:2021/11/17
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


class Logintest:
	def __init__(self,driver):
		self.driver=driver

	def login(self,username,password):
		self.driver.find_element(By.XPATH,value='//*[@id="loginname"]').send_keys(username)
		self.driver.find_element(By.XPATH,value='//*[@id="password"]').send_keys(password)
		self.driver.find_element(By.XPATH,value='//*[@id="submit"]').click()


	def getLoginSuccess(self):
		return self.driver.title

	def getLoginError(self):
		return self.driver.find_element(By.XPATH,value='//*[@id="msg_uname"]').text


















