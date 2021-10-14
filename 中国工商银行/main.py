"""
@author:96978
@file:main.py
@time:2021/10/13
"""
import defhome
import random
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
		name=input('请输入名字')
		password=int(input('请输入密码'))
		country=input('请输入国家')
		province=input('请输入省份')
		street=input('请输入街道')
		gate=input('请输入门牌号')
		print(defhome.addUser(username,name,password,country,province,street,gate))
	elif num==2:
		username = input('请输入账号')
		money= int(input('请输入存款金额'))
		n=defhome.saveMoney(username, money)
		if n==True:
			print('存款成功')
		else:
			print('用户不存在')
	elif num==3:
		username = input('请输入账号')
		password = int(input('请输入密码'))
		n = defhome.pd(username, password)
		if n == 0:
			money = int(input('请输入取款金额'))
			m=defhome.drawMoney(username,money)
			if m==3:
				print("余额不足")

	elif num==4:
		username = input('请输入账号')
		password = int(input('请输入密码'))
		n = defhome.pd(username, password)
		if n == 0:
			transfername=input('请输入转入账号')
			money=int(input('请输入转出金额'))
			m=defhome.transferMoney(username,transfername,money)
			if m==3:
				print("余额不足")
	elif num==5:
		username=input('请输入账号')
		password=int(input('请输入密码'))
		n=defhome.pd(username,password)
		if n==0:
			str1=defhome.queryUser(username)
			str2=['账号','姓名','密码','国家','省份','街道','门牌号','余额','开户行']
			for i in range(len(str1[0])):
				print('您的',str2[i],'为',str1[0][i])
	elif num==6:
		defhome.dbClose()
		print('Byebye!!!')
		break
	else:
		print('别瞎输')
