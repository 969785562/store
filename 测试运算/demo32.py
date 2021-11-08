"""
@author:96978
@file:demo32.py
@time:2021/11/08
"""


import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header



sendname = '969785562@qq.com'  # 本人邮箱账号
password = 'xysoisvpavovbdfd'
user2 = '969785562@qq.com'
part=MIMEMultipart('mixed')
part_text=MIMEText('157卢子岩测试报告')
part.attach(part_text)
part['Subject'] = Header('python', 'utf-8')
part['From'] = sendname
part['To'] = user2
# with open('D:\Pythonproject\pythonproject1\pycode1\计算器.html','r',encoding='utf-8') as f:
# 	content = f.read()
#设置html格式参数
part1 = MIMEText(open('D:\Pythonproject\pythonproject1\pycode1\计算器.html','r',encoding='utf-8').read(),'html','utf-8')
part1.add_header('Content-Disposition', 'attachment', filename='运算测试.html')
part.attach(part1)
try:
	server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
	server.login(sendname, password)  # 括号中对应的是发件人邮箱账号、邮箱密码
	server.sendmail(sendname, [user2,], part.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
	print('发送成功')
	server.quit()  # 关闭连接
except smtplib.SMTPException as e:
	print('发送失败', e)



