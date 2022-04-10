import pymysql



db = pymysql.Connect(

  host="13.124.112.205",

  user="mstpjt",

  password="1111",

  port = 55996,

  database="mstDB"

)



cursor = db.cursor()

# delete_all  = "DELETE FROM mstDB WHERE CAMERA_NUM = '5'"

delete_all  = "DELETE FROM mstDB "

cursor.execute(delete_all )

db.commit()

print(cursor.rowcount, "record(s) deleted")