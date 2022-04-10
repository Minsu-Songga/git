#-*- coding:utf-8 -*-
import pymysql

db = pymysql.Connect(host='13.209.69.215', user='mstpjt', password='1111', port = 55716, database='mstDB')
cursor = db.cursor()



query = "UPDATE mstDB SET  sort = %s, sec = %s , name = %s where camera_num = 1"


data  = (3, 1, 'MINSU')
cursor.execute(query, data)
db.commit()

