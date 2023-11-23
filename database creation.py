import mysql.connector as mql
mycon=mql.connect(host='localhost',user='root',passwd='1234')
cursor=mycon.cursor()
mycon.autocommit=True
s1="create database IF NOT EXISTS MDCL_RCD"
cursor.execute(s1)
