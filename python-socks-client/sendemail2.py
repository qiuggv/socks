#encoding: utf-8

from httplib2 import socks
import socket

#设置使用socks5代理
socket.socket = socks.socksocket
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,"132.122.1.152",1080)

#覆盖原来的域名解析方法，从socks5代理获取ip
def getaddrinfo(*args):
    return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]
socket.getaddrinfo=getaddrinfo

#以上设置必须都使用之前设置好

import smtplib
import sys

def main():
        script,mailto,subject,content=sys.argv
        print script
        print mailto	#邮件发给谁
        print subject	#邮件主题
        print content	#邮件内容
        #socket.socket = socks.socksocket
        #socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,"132.122.1.152",1080)


        s = smtplib.SMTP("smtp.163.com")
        #s = smtplib.SMTP("220.181.12.18")
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


#########################
#使用方式：python ./sendemail2.py 274429987@qq.com 公司21会议 请紧急回复
#########################
if __name__ == "__main__":
        main()
