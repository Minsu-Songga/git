#-*- coding:utf-8 -*-
import pymysql

db = pymysql.Connect(host='3.34.2.177', user='mstpjt', password='1111', port = 56941, database='mstDB')
cursor = db.cursor()


query = "INSERT INTO mstDB (CAMERA_NUM, SORTATION, sec, No) VALUES (%s,%s,%s,%s)"
data  = (3,3, 300, 3)
cursor.execute(query, data)
db.commit()



# ref : https://luran.me/300