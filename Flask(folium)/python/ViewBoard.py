import pymysql

db = pymysql.connect(host="52.78.123.53", user="mstpjt", passwd="1111", port = 55756, db="mstDB", charset="utf8")
cur = db.cursor()

sql = "SELECT * from board"
cur.execute(sql)

data_list = cur.fetchall()

print(data_list[0])
print(data_list[1])
print(data_list[2])