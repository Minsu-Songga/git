import folium
import webbrowser
import pandas as pd
from time import sleep
import pymysql

web = 1
cnt = 0
while True:
    # DB connect 
    mysqldb = pymysql.connect( 
    user='mstpjt',
    password='1111',
    host='54.180.32.86',
    port = 54923,
    db='mstDB')
    # Dict of CURSOR  
    cursor = mysqldb.cursor(pymysql.cursors.DictCursor)
    
    # SQL write 
    sql = "select * from mstDB"

     # SQL operate
    cursor.execute(query=sql)
    mstDB_dic = cursor.fetchall()
    print('mstDB_dic:',mstDB_dic)


    # camera = mstDB_dic[0]['camera_num']
    # sortation = mstDB_dic[0]['sort']
    # sec = mstDB_dic[0]['sec']
    # min = sec/60
    # time = min



    map_view = folium.Map(location=[37.54380696363407, 126.67682839947783], zoom_start=30)
    
    if mstDB_dic[0]['camera_num'] == 1:
        x = 37.54381054028666
        y = 126.67757270121972
        
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
        dis = float(vel*time)    
        dia = float(dis/2)
        
        if mstDB_dic[0]['name'] == 'MINSU':
            circle1 = folium.CircleMarker([x,y], popup='camera1', color='#e81a2e' ,fill_color='#e81a2e', radius=dia).add_to(map_view)
        elif mstDB_dic[0]['name'] == 'TAEMIN':
            circle1 = folium.CircleMarker([x,y], popup='camera1', color='#f2ee07' ,fill_color='#f2ee07', radius=dia).add_to(map_view)
        else:
            circle1 = folium.CircleMarker([x,y], popup='camera1', color='#2399e8' ,fill_color='#2399e8', radius=dia).add_to(map_view)

        cnt +=1
        if cnt ==5:
            del circle1
    
    if  mstDB_dic[1]['camera_num'] == 2:
        x =37.542755762723104
        y = 126.67658872977056

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
        dis = float(vel*time)    
        dia = float(dis/2)

        if mstDB_dic[1]['name'] == 'MINSU':
            circle2 = folium.CircleMarker([x,y], popup='camera2', color='#e81a2e' ,fill_color='#e81a2e', radius=dia).add_to(map_view)
        elif mstDB_dic[1]['name'] == 'TAEMIN':
            circle2 = folium.CircleMarker([x,y], popup='camera2', color='#f2ee07' ,fill_color='#f2ee07', radius=dia).add_to(map_view)
        else:
            circle2 = folium.CircleMarker([x,y], popup='camera2', color='#2399e8' ,fill_color='#2399e8', radius=dia).add_to(map_view)

        cnt +=1
        if cnt ==5:
            del circle2
    
    if mstDB_dic[2]['camera_num'] == 3:
        x =37.54379981033517
        y = 126.67574577873687

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
        dis = float(vel*time)    
        dia = float(dis/2)

        if mstDB_dic[2]['name'] == 'MINSU':
            circle3 = folium.CircleMarker([x,y], popup='camera3', color='#e81a2e' ,fill_color='#e81a2e', radius=dia).add_to(map_view)
        elif mstDB_dic[2]['name'] == 'TAEMIN':
            circle3 = folium.CircleMarker([x,y], popup='camera3', color='#f2ee07' ,fill_color='#f2ee07', radius=dia).add_to(map_view)
        else:
            circle3 = folium.CircleMarker([x,y], popup='camera3', color='#2399e8' ,fill_color='#2399e8', radius=dia).add_to(map_view)

 
        cnt +=1
        if cnt ==5:
            del circle3
    
    

    
    # marker of camera
    folium.Marker([37.54381054028666, 126.67757270121972], popup='camera1').add_to(map_view)
    folium.Marker([37.542755762723104, 126.67658872977056], popup='camera2').add_to(map_view)
    folium.Marker([37.54379981033517, 126.67574577873687], popup='camera3').add_to(map_view)
    folium.Marker([37.54443645185251, 126.67668405002358], popup='camera4').add_to(map_view)


    map_view.save('templates/save.html')
    data = open('templates/save.html', 'r').readlines()
    data[3] = '\t<meta http-equiv="refresh" content="10" />\n'
    out = open('templates/save.html', 'w')
    out.writelines(data)
    out.close() 
    

    if web == 1:
        # webbrowser.open("/home/minsu/Desktop/Flask/templates/save.html")
        web = 0  
    
    if dia == 50:
        camera = mstDB_dic[0]['camera_num']
        sortation = mstDB_dic[0]['sort']
        time = min
    sleep(10)

#map_view.save('templates\save.html')
#webbrowser.open("templates\save.html")
