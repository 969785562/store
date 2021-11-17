"""
@author:96978
@file:InitPage.py
@time:2021/11/17
"""

import xlrd
import xlwt
from xlutils import copy
import time

class  InitPage():

    def xldata(self,num):
        workbook=xlrd.open_workbook(filename=r'D:\Python自动化测试\其他课程\自动化\day03\HKR.xls',encoding_override=True)
        sheet=workbook.sheet_by_index(0)
        rows=sheet.nrows
        list=['username','password','expect','num']
        loginSuccessData=[]
        loginErrorData=[]
        for row in range(1,rows):
            data={}
            for col in range(4):
                data[list[col]]=sheet.cell_value(row,col)
            if data['expect']=='Student Login':
                loginSuccessData.append(data)
            else:
                loginErrorData.append(data)
        if num==1:
            return loginSuccessData
        else:
            return loginErrorData



    def xlw(self,num,str):
        de = xlrd.open_workbook(filename=r'D:\Python自动化测试\其他课程\自动化\day03\HKR.xls',encoding_override=True)
        wb=copy.copy(de)
        worksheet=wb.get_sheet(0)
        worksheet.write(num,4,str)
        worksheet.write(num,5,'卢子岩')
        # print(time.strftime("%Y-%m-%d",time.localtime()))
        time1=time.strftime("%Y-%m-%d",time.localtime())
        worksheet.write(num,6,time1)
        wb.save('D:\Python自动化测试\其他课程\自动化\day03\HKR.xls')
        return 1








