"""
@author:96978
@file:defhome.py
@time:2021/10/13
"""
import pymysql
db=pymysql.connect(
	host='localhost',
	user='root',
	password='root',
	database='bank'
)
cursor = db.cursor()


# 判断账号是否存在，账号与密码是否一致
def pd(username,password):
	# cursor = db.cursor()
	sql1="select username from user"
	cursor.execute(sql1)
	a = cursor.fetchall()
	list1 = []
	for x in range(len(a)):
		list1.append(a[x][0])
	if username in list1:
		sql2 = "select password from user where username='%s'" %username
		cursor.execute(sql2)
		b = cursor.fetchall()
		if password==b[0][0]:
			return 0
		else:
			print('密码错误')
			return 1
	else:
		print('账号不存在')
	return 2


# 添加用户
def addUser(username,name,password,country,province,street,gate):
	# cursor = db.cursor()
	sql1 = "select username from user"
	cursor.execute(sql1)
	a = cursor.fetchall()
	list1 = []
	for x in range(len(a)):
		list1.append(a[x][0])
	if username in list1:
		print('账号已存在')
		return 2
	else:
		if len(list1)==100:
			print('用户库已满')
			return 3
		else:
			sql="INSERT INTO user VALUES ('%s','%s','%s','%s','%s','%s','%s','0','中国工商银行的昌平支行')"%(username,name,password,country,province,street,gate)
			cursor.execute(sql)
			db.commit()
			return 1


# 查询用户信息
def queryUser(username):
	# cursor=db.cursor()
	sql="select * from user where username='%s'"%username
	cursor.execute(sql)
	a=cursor.fetchall()
	return a


#存钱
def saveMoney(username,money):
	sql1 = "select username from user"
	cursor.execute(sql1)
	a = cursor.fetchall()
	list1 = []
	for x in range(len(a)):
		list1.append(a[x][0])
	if username in list1:
		sql3 = "select money from user where username='%s'" % username
		cursor.execute(sql3)
		dbmoney = cursor.fetchall()
		# print(dbmoney[0][0])
		money+=dbmoney[0][0]
		sql2 = "UPDATE user SET money='%s' WHERE username='%s'"%(money,username)
		cursor.execute(sql2)
		db.commit()
		return True
	else:
		return False

# 取钱
def drawMoney(username,money):
	sql = "select money from user where username='%s'" % username
	cursor.execute(sql)
	dbmoney = cursor.fetchall()
	if money<=dbmoney[0][0]:
		money=dbmoney[0][0]-money
		sql2 = "UPDATE user SET money='%s' WHERE username='%s'" % (money, username)
		cursor.execute(sql2)
		db.commit()
		print('取款成功，您的余额为:',money)
		return True
	else:
		return 3


# 转账
def transferMoney(username,transfername,money):
	sql1 = "select username from user"
	cursor.execute(sql1)
	a = cursor.fetchall()
	list1 = []
	for x in range(len(a)):
		list1.append(a[x][0])
	if transfername in list1:
		sql = "select money from user where username='%s'" % username
		cursor.execute(sql)
		dbmoney = cursor.fetchall()
		sql1 = "select money from user where username='%s'" % transfername
		cursor.execute(sql1)
		dbmoney2 = cursor.fetchall()
		# print(dbmoney,dbmoney2)
		if money <= dbmoney[0][0]:
			money1 = dbmoney[0][0] - money
			money2= dbmoney2[0][0] + money
			sql2 = "UPDATE user SET money='%s' WHERE username='%s'" % (money1, username)
			sql3 = "UPDATE user SET money='%s' WHERE username='%s'" % (money2, transfername)
			cursor.execute(sql2)
			cursor.execute(sql3)
			db.commit()
			print('转账成功')
			return True
		else:
			return 3


def dbClose():
	cursor.close()
	db.close()
	return 1