"""
@author:96978
@file:Defhome.py
@time:2021/10/15
"""
import pymysql
db=pymysql.connect(
	host='localhost',
	user='root',
	password='root',
	database='bank'
)
cursor = db.cursor()



class User:
	__username=''
	__name=''
	__password=0

	def setUsername(self,username):
		self.__username=username
	def getUsername(self):
		return self.__username
	def setName(self,name):
		self.__name=name
	def getName(self):
		return self.__name
	def setPassword(self,password):
		self.__password=password
	def getPassword(self):
		return self.__password

	# 判断账号是否在数据库中
	def pdUsername(self):
		sql1 = "select username from user"
		cursor.execute(sql1)
		a = cursor.fetchall()
		list1 = []
		for x in range(len(a)):
			list1.append(a[x][0])
		if self.__username in list1:
			return 0
		else:
			if len(list1)==100:
				return 2
			else:
				return 1
	# 判断账号和密码是否保持一致
	def pdPassword(self):
		sql2 = "select password from user where username='%s'" % (self.__username)
		cursor.execute(sql2)
		b = cursor.fetchall()
		if self.__password==b[0][0]:
			return 0
		else:
			return 1

	#判断结果
	def pd(self):
		if User.pdUsername(self)==0:
			if User.pdPassword(self)==0:
				print('登录成功')
				return 0
			else:
				print('密码错误')
				return 1
		else:
			print('账号不存在')
			return 2

	def addUser(self):
		if User.pdUsername(self)==0:
			print('账号已存在')
			return 2
		elif User.pdUsername(self)==2:
			print('用户库已满')
			return 3
		else:
			sql = "INSERT INTO User(username,name,password) VALUES ('%s','%s','%s')" % (self.__username, self.__name, self.__password)
			cursor.execute(sql)
			db.commit()
			return 1

	def queryUser(self):
		sql = "select * from user where username='%s'" % self.__username
		cursor.execute(sql)
		a = cursor.fetchall()
		return a

class Address:
	__country=''
	__province=''
	__street=''
	__gate=''

	def setCountry(self,country):
		self.__country=country
	def getCountry(self):
		return self.__country
	def setProvince(self,province):
		self.__province=province
	def getProvince(self):
		return self.__province
	def setStreet(self,street):
		self.__street=street
	def getStreet(self):
		return self.__street
	def setGate(self,gate):
		self.__gate=gate
	def getGate(self):
		return self.__gate

	def addAddress(self,username):
		sql = "UPDATE User SET country='%s',province='%s',street='%s',gate='%s' WHERE username='%s'" % (self.__country, self.__province, self.__street,self.__gate,username)
		cursor.execute(sql)
		db.commit()
		return 0


class Bank:
	__money=0
	__bankname=''

	def setMoney(self,money):
		self.__money=money
	def getMoney(self):
		return self.__money
	def setBank(self,bankname):
		self.__bankname=bankname
	def getBank(self):
		return self.__bankname

	def addBank(self,username):
		sql = "UPDATE User SET money='%s',bank='%s' WHERE username='%s'" % (
		self.__money, self.__bankname,username)
		cursor.execute(sql)
		db.commit()
		return 0

	def saveMoney(self,username):
		sql3 = "select money from user where username='%s'" % username
		cursor.execute(sql3)
		dbmoney = cursor.fetchall()
		self.__money+=dbmoney[0][0]
		sql2 = "UPDATE user SET money='%s' WHERE username='%s'"%(self.__money,username)
		cursor.execute(sql2)
		db.commit()
		return True


	def drawMoney(self,username):
		sql = "select money from user where username='%s'" % username
		cursor.execute(sql)
		dbmoney = cursor.fetchall()
		if self.__money<= dbmoney[0][0]:
			self.__money = dbmoney[0][0] - self.__money
			sql2 = "UPDATE user SET money='%s' WHERE username='%s'" % (self.__money, username)
			cursor.execute(sql2)
			db.commit()
			print('取款成功，您的余额为:',self.__money)
			return True
		else:
			print('余额不足')
			return 3

	def transferMoney(self,username, transfername):
		sql = "select money from user where username='%s'" % username
		cursor.execute(sql)
		dbmoney = cursor.fetchall()
		sql1 = "select money from user where username='%s'" % transfername
		cursor.execute(sql1)
		dbmoney2 = cursor.fetchall()
		# print(dbmoney,dbmoney2)
		if self.__money <= dbmoney[0][0]:
			money1 = dbmoney[0][0] - self.__money
			money2 = dbmoney2[0][0] + self.__money
			sql2 = "UPDATE user SET money='%s' WHERE username='%s'" % (money1, username)
			sql3 = "UPDATE user SET money='%s' WHERE username='%s'" % (money2, transfername)
			cursor.execute(sql2)
			cursor.execute(sql3)
			db.commit()
			print('转账成功')
			return True
		else:
			print('余额不足')
			return 3

def dbClose():
	cursor.close()
	db.close()
	return 1



