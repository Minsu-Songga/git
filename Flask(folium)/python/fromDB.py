import pymysql

# DB connect 
mysqldb = pymysql.connect( 
    user='mstpjt',
    password='1111',
    host='13.124.112.205',
    port = 55996,
    db='mstDB')

# Dict형식의 CURSOR  
cursor = mysqldb.cursor(pymysql.cursors.DictCursor)

# SQL 작성 
sql = "select * from mstDB"

 # SQL 실행
cursor.execute(query=sql)

mstDB_dic = cursor.fetchall()



print(mstDB_dic[0]['CAMERA_NUM'])
print(mstDB_dic[0]['SORTATION'])
print(mstDB_dic[0]['sec'])
sec = mstDB_dic[0]['sec']
min = sec/60
print('min:', min)


