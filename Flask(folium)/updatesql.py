#-*- coding:utf-8 -*-
import pymysql

db = pymysql.Connect(host='3.37.87.224', 
                     user='mstpjt', 
                     password='1111',
                     port = 58994, 
                     database='mstDB')
cursor = db.cursor()



query = "UPDATE mstDB SET  sort = %s, sec = %s , name = %s where camera_num = 3"


data  = (2, 200, 'TAEMIN')
cursor.execute(query, data)
db.commit()

