"""
@author:96978
@file:operation.py
@time:2021/11/19
"""
import time

from appium.webdriver.common.touch_action import TouchAction


class operation:


	def __init__(self,driver):
		self.driver=driver


	def start(self):
		time.sleep(8)
		el1 = self.driver.find_element_by_xpath(
			"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[3]")
		el1.click()
		time.sleep(10)
		el1 = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
		el1.click()




	def homepage(self):
		time.sleep(10)
		el8 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup")
		el8.click()
		time.sleep(10)
		TouchAction(self.driver).tap(x=738, y=1561).perform()
	def homepageSuccess(self):
		el1 = self.driver.find_element_by_id("com.sina.weibo:id/detail_activity_header_title_text").text
		return el1


	def video(self):
		time.sleep(15)
		el1 = self.driver.find_element_by_accessibility_id("视频")
		el1.click()
		time.sleep(15)
		el2 = self.driver.find_element_by_id("com.sina.weibo:id/story_new_footer_like")
		el2.click()
		time.sleep(15)
		el3 = self.driver.find_element_by_xpath(
			"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View")
		el3.click()
		time.sleep(15)
		el4 = self.driver.find_element_by_id("com.sina.weibo:id/story_new_footer_comment")
		el4.click()
		time.sleep(15)
		el5 = self.driver.find_element_by_xpath(
			"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView")
		el5.click()
		time.sleep(15)
		el6 = self.driver.find_element_by_id("com.sina.weibo:id/titleText")
		el6.click()
		time.sleep(15)
	def videoSuccess(self):
		el6 = self.driver.find_element_by_id("com.sina.weibo:id/titleText").text
		return el6


	def search(self):
		time.sleep(15)
		el3 = self.driver.find_element_by_accessibility_id("发现")
		el3.click()
		time.sleep(15)
		el4 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.EditText")
		el4.click()
		time.sleep(15)
		el5 = self.driver.find_element_by_id("com.sina.weibo:id/tv_search_keyword")
		el5.click()
		time.sleep(12)
		el5.send_keys("杨幂")
		time.sleep(15)
		el6 = self.driver.find_element_by_xpath(
			"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout")
		el6.click()
		time.sleep(15)
		el7 = self.driver.find_element_by_xpath(
			"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.view.ViewGroup[1]/android.widget.TextView")
		el7.click()
		time.sleep(15)


	def searchSuccess(self):
		el8 = self.driver.find_element_by_id("com.sina.weibo:id/detail_activity_header_title_text").text
		return el8

	def news(self):
		time.sleep(18)
		el1 = self.driver.find_element_by_accessibility_id("消息")
		el1.click()
		time.sleep(15)
		el2 = self.driver.find_element_by_id("com.sina.weibo:id/et_login_view_phone")
		el2.click()
		time.sleep(15)
		el2.send_keys("13253241216")
		time.sleep(12)
		el3 = self.driver.find_element_by_id("com.sina.weibo:id/tv_login_view_resent")
		el3.click()

	def newsSuccess(self):
		time.sleep(12)
		el2 = self.driver.find_element_by_id("com.sina.weibo:id/tv_login_sms_title").text
		return el2









