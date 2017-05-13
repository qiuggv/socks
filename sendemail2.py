#encoding: utf-8

from httplib2 import socks
import socket
import smtplib
import sys

def main():
	script,mailto,subject,content=sys.argv
	print script
	print mailto
	print subject
	print content
	socket.socket = socks.socksocket
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,"132.122.1.152",1080)
	
	
	s = smtplib.SMTP("smtp.163.com")
	s.login("13160846099@163.com", "qiuxy@telecom.")
	msg = '''\
From: 13160846099@163.com
To: '''+mailto+'''
Subject: '''+subject+'''
Content-Type: text/html; charset=us-ascii

'''+content+'''</font>'''
	#toMail = ["13160846099@163.com"]		
	#s.sendmail("13160846099@163.com", toMail, msg)
	s.sendmail("13160846099@163.com", mailto, msg)
	s.quit()


if __name__ == "__main__":
	main()
