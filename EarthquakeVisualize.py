import pandas as pd
import numpy as np
import folium as f
import math
#from html2image import Html2Image
from datetime import datetime as dt

path='EarthquakeData.csv'

data=pd.read_csv(path)

list_time=np.array(data['time'])
list_datetime=list_time
list_latitude=np.array(data['latitude'])
list_longitude=np.array(data['longitude'])
list_depth=np.array(data['depth'])
list_mag=np.array(data['mag'])
list_place=np.array(data['place'])

#print(list_time[1])

#时间处理模块，粒度为天
def conv_time(UTCformat):
    StdTime = dt.strptime(UTCformat, '%Y-%m-%dT%H:%M:%S.%fZ')
    date=StdTime.strftime("%Y-%m-%d")

    return date

#for i in range(list_time.size):
   # list_datetime[i]=conv_time(list_time[i])

#地震事件绘制模块
def draw_event(latitude,longtitude,depth,mag,text):
    
    if depth<=30: #极浅源地震
        colors='#D400EF'
    elif(depth<=60): #浅源地震
        colors='#FF7B00'
    elif(depth<=300): #中源地震
        colors='#00FFBB'
    else: #深源地震
        colors='#12009B'

    if mag==6:
        r=30000
    else:#地震能量经验式计算可视化等效
        r=30000*math.sqrt(math.pow(32,mag-6))

    f.Circle(
    location=(latitude, longtitude),
    radius=r,   # 圆的半径
    color=colors,
    weight=1,
    opacity=1,
    fill=True,
    fill_color='#FFD700',
    fill_opacity=0.2,
    tooltip=text
    ).add_to(world_map)

world_map=f.Map(location=(0,0),
                tiles='https://server.arcgisonline.com/ArcGIS/rest/services/Ocean/World_Ocean_Base/MapServer/tile/{z}/{y}/{x}',
                attr='Esri.OceanBasemap',
                #tiles='https://webrd02.is.autonavi.com/appmaptile?lang=zh_en&size=1&scale=1&style=8&x={x}&y={y}&z={z}',  #将地图更换为国内高德地图源。如加载html为空白请使用这个源，并注释掉前两行代码。
                #attr='高德-中英文对照',
                zoom_start=3)

for i in range(0,10000):

    latitude=list_latitude[i]
    longitude=list_longitude[i]
    depth=list_depth[i]
    mag=list_mag[i]
    text=f"{list_time[i]} --- {list_place[i]} --- M{mag} --- {depth}km"

    draw_event(latitude=latitude,longtitude=longitude,depth=depth,mag=mag,text=text)

world_map.save('test.html')
