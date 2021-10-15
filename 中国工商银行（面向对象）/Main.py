"""
@author:96978
@file:Main.py
@time:2021/10/15
"""

import Defhome
import random
user=Defhome.User()
address=Defhome.Address()
bank=Defhome.Bank()

print('''
	******************************
	*         中国工商银行         *
	*         账户管理系统         *
	*             v1.0           *
	******************************
	* 1.开户                      *
	* 2.存钱                      *
	* 3.取钱                      *
	* 4.转账                      *
	* 5.查询                      *
	* 6.Bye!                     *
	******************************
''')

while True:
	num=int(input('请输入序号'))
	if num==1:
		username=random.randint(10000000,100000000)
		print('您的账号为:',username)
		user.setUsername(username)
		user.setName(input('请输入姓名'))
		user.setPassword(int(input('请输入密码')))
		address.setCountry(input('请输入国家'))
		address.setProvince(input('请输入省份'))
		address.setStreet(input('请输入街道'))
		address.setGate(input('请输入门牌号'))
		bank.setBank('中国工商银行昌平支行')
		user.addUser()
		address.addAddress(username)
		bank.addBank(username)

	elif num==2:
		username = input('请输入账号')
		user.setUsername(username)
		if user.pdUsername()==0:
			bank.setMoney(int(input('请输入存款金额')))
			if bank.saveMoney(username)==True:
				print('存款成功')
		else:
			print('用户不存在')
	elif num==3:
		username = input('请输入账号')
		user.setUsername(username)
		user.setPassword(int(input('请输入密码')))
		n = user.pd()
		if n == 0:
			bank.setMoney(int(input('请输入取款金额')))
			m=bank.drawMoney(username)


	elif num==4:
		username = input('请输入账号')
		user.setUsername(username)
		user.setPassword(int(input('请输入密码')))
		n = user.pd()
		if n == 0:
			transfername=input('请输入转入账号')
			bank.setMoney(int(input('请输入转出金额')))
			m=bank.transferMoney(username,transfername)

	elif num==5:
		user.setUsername(input('请输入账号'))
		user.setPassword(int(input('请输入密码')))
		n=user.pd()
		if n==0:
			str1=user.queryUser()
			str2=['账号','姓名','密码','国家','省份','街道','门牌号','余额','开户行']
			for i in range(len(str1[0])):
				print('您的',str2[i],'为',str1[0][i])
	elif num==6:
		Defhome.dbClose()
		print('Byebye!!!')
		break
	else:
		print('别瞎输')
