"""
@author:96978
@file:day14.py
@time:2021/11/09
"""

from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from 工商银行完整版 import bank_saveMoney
from 工商银行完整版 import bank_takeMoney
from 工商银行完整版 import bank_selectUser
from 工商银行完整版 import bank_transformMoney

import xlrd
from xlutils import copy


de=xlrd.open_workbook(filename='D:\Pythonproject\pythonproject1\pycode1\data.xls',encoding_override=True)


sheet=de.sheet_by_index(0)
cols=sheet.ncols
rows=sheet.nrows
list=[]
for i in range(1,rows):
	list1=[]
	for j in range(cols-1):
		va=sheet.cell_value(i,j)
		list1.append(va)
	list.append(list1)


sheet1=de.sheet_by_index(1)
cols1=sheet1.ncols
rows1=sheet1.nrows
list2=[]
for i in range(1,rows1):
	list1=[]
	for j in range(cols1-1):
		va=sheet1.cell_value(i,j)
		list1.append(va)
	list2.append(list1)


sheet2=de.sheet_by_index(2)
cols2=sheet2.ncols
rows2=sheet2.nrows
list3=[]
for i in range(1,rows2):
	list1=[]
	for j in range(cols2-1):
		va=sheet2.cell_value(i,j)
		list1.append(va)
	list3.append(list1)


sheet3=de.sheet_by_index(3)
cols3=sheet3.ncols
rows3=sheet3.nrows
list4=[]
for i in range(1,rows3):
	list1=[]
	for j in range(cols3-1):
		va=sheet3.cell_value(i,j)
		list1.append(va)
	list4.append(list1)



@ddt
class testCase(TestCase):
	@data(*list)
	@unpack
	def testSaveMoney(self,ac,money,a,row):
		re=bank_saveMoney(ac,money)
		#断言
		de1 = xlrd.open_workbook(filename='D:\Pythonproject\pythonproject1\pycode1\data.xls', encoding_override=True)
		workbook=copy.copy(de1)
		worksheet=workbook.get_sheet(0)
		if re==a :
			worksheet.write(row,4,'通过')
			workbook.save('data.xls')
		else:
			worksheet.write(row,4,'未通过')
			workbook.save('data.xls')

	@data(*list2)
	@unpack
	def testTakeMoney(self, ac,password,money, a, row):
		re = bank_takeMoney(ac, password,money)
		# 断言
		de1 = xlrd.open_workbook(filename='D:\Pythonproject\pythonproject1\pycode1\data.xls',
								 encoding_override=True)
		workbook = copy.copy(de1)
		worksheet = workbook.get_sheet(1)
		if re == a:
			worksheet.write(row, 5, '通过')
			workbook.save('data.xls')
		else:
			worksheet.write(row, 5, '未通过')
			workbook.save('data.xls')

	@data(*list3)
	@unpack
	def testSelectUser(self, ac,password, a, row):
		re = bank_selectUser(ac, password)
		# 断言
		de1 = xlrd.open_workbook(filename='D:\Pythonproject\pythonproject1\pycode1\data.xls',
								 encoding_override=True)
		workbook = copy.copy(de1)
		worksheet = workbook.get_sheet(2)
		if re == a:
			worksheet.write(row, 4, '通过')
			workbook.save('data.xls')
		else:
			worksheet.write(row, 4, '未通过')
			workbook.save('data.xls')



	@data(*list4)
	@unpack
	def testTransformMoney(self, outac,inac,password,money,a, row):
		re = bank_transformMoney(outac,inac,password,money)
		# 断言
		de1 = xlrd.open_workbook(filename='D:\Pythonproject\pythonproject1\pycode1\data.xls',
								 encoding_override=True)
		workbook = copy.copy(de1)
		worksheet = workbook.get_sheet(3)
		if re == a:
			worksheet.write(row, 6, '通过')
			workbook.save('data.xls')
		else:
			worksheet.write(row, 6, '未通过')
			workbook.save('data.xls')





