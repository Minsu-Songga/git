#-*- coding:utf-8 -*-
import pymysql

db = pymysql.Connect(host='13.124.0.40', 
                     user='mstpjt', 
                     password='1111',
                     port = 50118, 
                     database='mstDB')
cursor = db.cursor()



query = "UPDATE mstDB SET  sort = %s, sec = %s , name = %s where camera_num = 1"


data  = (1, 0, 'MINSU')
cursor.execute(query, data)
db.commit()

