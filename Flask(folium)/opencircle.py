import folium
import webbrowser
import pandas as pd
from time import sleep
import pymysql
import cv2
import numpy as np
import os

path = 'C:/Users/SEC/Desktop/Flask'
web = 1
cnt = 0
while True:
    # DB connect 
    mysqldb = pymysql.connect( 
    user='mstpjt',
    password='1111',
    host='13.124.0.40',
    port = 54966,
    db='mstDB')
    # Dict of CURSOR  
    cursor = mysqldb.cursor(pymysql.cursors.DictCursor)
    
    # SQL write 
    sql = "select * from mstDB"

     # SQL operate
    cursor.execute(query=sql)
    mstDB_dic = cursor.fetchall()
    print('mstDB_dic:',mstDB_dic)



    img = cv2.imread('5flow.jpg')
    
    if mstDB_dic[0]['camera_num'] == 1:
        x = 636
        y = 350
        
        sort = mstDB_dic[0]['sort']
        sec= mstDB_dic[0]['sec']
        min= sec/60
        time = min
        if sort == 1:
            vel = 91.8
        elif sort == 2:
            vel = 86.4
        elif sort == 3:
            vel = 40
        dis = int(vel*time)    
        dia = int(dis/2)
        
        if mstDB_dic[0]['name'] == 'MINSU':
            cv2.circle(img, (x, y), dia, (255,0,0), 2)
        elif mstDB_dic[0]['name'] == 'TAEMIN':
            cv2.circle(img, (x, y), dia, (0,255,0), 2)
        else:
            cv2.circle(img, (x, y), dia, (0,0,255), 2)
        # cv2.imshow('circle', img)
        cv2.imwrite(os.path.join(path , '5flow-2.jpg'), img)
        # cv2.waitKey(0)
        cnt +=1
        if cnt ==100:
            del cv2.circle

    
    
    if  mstDB_dic[1]['camera_num'] == 2:
        x = 730
        y = 420

        sort = mstDB_dic[1]['sort']
        sec= mstDB_dic[1]['sec']
        min= sec/60
        time = min
        if sort == 1:
            vel = 91.8
        elif sort == 2:
            vel = 86.4
        elif sort == 3:
            vel = 40
        dis = int(vel*time)    
        dia = int(dis/2)

        if mstDB_dic[1]['name'] == 'MINSU':
            cv2.circle(img, (x, y), dia, (255,0,0), 2)
        elif mstDB_dic[1]['name'] == 'TAEMIN':
            cv2.circle(img, (x, y), dia, (0,255,0), 2)
        else:
            cv2.circle(img, (x, y), dia, (0,0,255), 2)
        # cv2.imshow('circle', img)
        cv2.imwrite(os.path.join(path , '5flow-2.jpg'), img)
        # cv2.waitKey(0)
        cnt +=1
        if cnt ==100:
            del cv2.circle
    
    if mstDB_dic[2]['camera_num'] == 3:
        x =1062
        y = 673

        sort = mstDB_dic[2]['sort']
        sec= mstDB_dic[2]['sec']
        min= sec/60
        time = min
        if sort == 1:
            vel = 91.8
        elif sort == 2:
            vel = 86.4
        elif sort == 3:
            vel = 40
        dis = int(vel*time)    
        dia = int(dis/2)

        if mstDB_dic[2]['name'] == 'MINSU':
            cv2.circle(img, (x, y), dia, (255,0,0), 2)
        elif mstDB_dic[2]['name'] == 'TAEMIN':
            cv2.circle(img, (x, y), dia, (0,255,0), 2)
        else:
            cv2.circle(img, (x, y), dia, (0,0,255), 2)
        # cv2.imshow('circle', img)
        cv2.imwrite(os.path.join(path , '5flow-2.jpg'), img)
        # cv2.waitKey(0)
        cnt +=1
        if cnt ==100:
            del cv2.circle
 


    sleep(10)


