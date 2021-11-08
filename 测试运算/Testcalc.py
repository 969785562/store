"""
@author:96978
@file:Testcalc.py
@time:2021/11/05
"""
from unittest import TestCase

from ddt import ddt,data,unpack

from demo31 import Calc
@ddt
class Testcalc(TestCase):


	@data([5,6,11],[1,3,4],[-1,-2,-3])
	@unpack
	def testadd(self,a,b,c):
		calc=Calc()
		sum = calc.add(a,b)
		self.assertEqual(c,sum)

	@data([5, 6, -1], [1, 3, -2], [-1, -2, 1])
	@unpack
	def testsub(self,a,b,c):

		calc = Calc()
		sub = calc.sub(a, b)
		self.assertEqual(c, sub)

	@data([5, 6, 30], [1, 3, 3], [-1, -2, 2])
	@unpack
	def testmulti(self,a,b,c):

		calc = Calc()
		multi = calc.multi(a, b)
		self.assertEqual(c, multi)

	@data([22, 2, 11], [-4, 2, -2], [-2, -2, 1])
	@unpack
	def testdivide(self,a,b,c):

		calc = Calc()
		divide = calc.divide(a, b)
		self.assertEqual(c, divide)