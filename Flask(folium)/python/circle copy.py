import folium
import webbrowser
import pandas as pd
from time import sleep
import pymysql

web = 1

while True:
    # DB connect 
    mysqldb = pymysql.connect( 
    user='mstpjt',
    password='1111',
    host='3.36.119.185',
    port = 54099,
    db='mstDB')
    # Dict of CURSOR  
    cursor = mysqldb.cursor(pymysql.cursors.DictCursor)
    
    # SQL write 
    sql = "select * from mstDB"

     # SQL operate
    cursor.execute(query=sql)
    mstDB_dic = cursor.fetchall()
    sec = mstDB_dic[0]['sec']
    min = sec/60


    camera = mstDB_dic[0]['CAMERA_NUM']
    #print(type(camera))

    sortation = mstDB_dic[0]['SORTATION']
    #print('type(sortation):',type(sortation))

    time = min   
    print(camera)
    print(sortation)
    print(min)

    map_view = folium.Map(location=[37.54380696363407, 126.67682839947783], zoom_start=30)
    
    if camera == 1:
        x = 37.54381054028666
        y = 126.67757270121972
    elif  camera == 2:
        x =37.542755762723104
        y = 126.67658872977056
    elif camera == 3:
        x =37.54379981033517
        y = 126.67574577873687
    elif camera == 4:
        x =37.54443645185251
        y = 126.67668405002358    
    
    if sortation == 1:
        vel = 91.8
    elif sortation == 2:
        vel = 86.4
    elif sortation == 3:
        vel = 40

    dis = float(vel*time)    
    dia = float(dis/2)
    
    # marker of camera
    folium.Marker([37.54381054028666, 126.67757270121972], popup='camera1').add_to(map_view)
    folium.Marker([37.542755762723104, 126.67658872977056], popup='camera2').add_to(map_view)
    folium.Marker([37.54379981033517, 126.67574577873687], popup='camera3').add_to(map_view)
    folium.Marker([37.54443645185251, 126.67668405002358], popup='camera4').add_to(map_view)
    
    circle1 = folium.CircleMarker([x,y], popup='circle', color='#3186cc' ,fill_color='#132b5e', radius=dia).add_to(map_view)
    
    map_view.save('templates/save1.html')
    data = open('templates/save1.html', 'r').readlines()
    data[3] = '\t<meta http-equiv="refresh" content="10" />\n'
    out = open('templates/save1.html', 'w')
    out.writelines(data)
    out.close() 
    

    if web == 1:
        webbrowser.open("/home/minsu/Desktop/Flask/templates/save1.html")
        web = 0  
    
    if dia == 50:
        camera = mstDB_dic[0]['CAMERA_NUM']
        sortation = mstDB_dic[0]['SORTATION']
        time = min
    sleep(10)

#map_view.save('templates\save.html')
#webbrowser.open("templates\save.html")
