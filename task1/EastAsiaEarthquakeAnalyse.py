from __future__ import division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path='EarthquakeData.csv'

data=pd.read_csv(path)

list_latitude=np.array(data['latitude'])
list_longitude=np.array(data['longitude'])
list_depth=np.array(data['depth'])
list_mag=np.array(data['mag'])

def judgeEastAsia(latitude,longitude):
    if latitude >= 4 and latitude <= 53 and longitude >= 73 and longitude <= 150:
        return True

strong_exshallow=0
strong_shallow=0
strong_mid=0
strong_deep=0
tremor_exshallow=0
tremor_shallow=0
tremor_mid=0
tremor_deep=0
weak_exshallow=0
weak_shallow=0
weak_mid=0
weak_deep=0

sum_weak=0
sum_tremor=0
sum_strong=0
sum=0

for i in range(list_latitude.size):
    if judgeEastAsia(list_latitude[i],list_longitude[i]):
        #sum+=1
        depth=list_depth[i]
        mag=list_mag[i]

        if mag<6.0:#中强地震
            sum_weak+=1
            if depth<=30: #极浅源地震
                weak_exshallow+=1
            elif(depth<=60): #浅源地震
                weak_shallow+=1
            elif(depth<=300): #中源地震
                weak_mid+=1
            else: #深源地震
                weak_deep+=1
        elif mag<7.0:#强地震
            sum_tremor+=1
            if depth<=30:
                tremor_exshallow+=1
            elif(depth<=60):
                tremor_shallow+=1
            elif(depth<=300):
                tremor_mid+=1
            else:
                tremor_deep+=1
        else:#强烈地震
            sum_strong+=1
            if depth<=30:
                strong_exshallow+=1
            elif(depth<=60):
                strong_shallow+=1
            elif(depth<=300):
                strong_mid+=1
            else:
                strong_deep+=1

#print(sum)
#print(sum_strong)
#print(strong_exshallow)
#print(strong_shallow)
#print(strong_mid)
#print(strong_deep)



labels=['M4.5-6.0','M6.0-7.0','M7.0+']
data_exshallow=np.array([weak_exshallow/sum_weak,tremor_exshallow/sum_tremor,strong_exshallow/sum_strong])*100
data_shallow=np.array([weak_shallow/sum_weak,tremor_shallow/sum_tremor,strong_shallow/sum_strong])*100
data_mid=np.array([weak_mid/sum_weak,tremor_mid/sum_tremor,strong_mid/sum_strong])*100
data_deep=np.array([weak_deep/sum_weak,tremor_deep/sum_tremor,strong_deep/sum_strong])*100

#print(data_exshallow)
#print(data_shallow)
#print(data_mid)
#print(data_deep)

plt.rcParams['font.family'] = ['SimHei']
bar_width=0.35

fig,ax=plt.subplots()

ax.bar(labels,data_exshallow,bar_width,color='#FF0000',label='极浅源地震（<=30km）')
ax.bar(labels,data_shallow,bar_width,bottom=data_exshallow,color='#FFB700',label='浅源地震(30-60km)')
ax.bar(labels,data_mid,bar_width,bottom=data_exshallow+data_shallow,color='#00C8FF',label='中源地震(60-300km)')
ax.bar(labels,data_deep,bar_width,bottom=data_exshallow+data_shallow+data_mid,color='#2F00FF',label='深源地震(>300km)')

ax.set_ylabel('占比(%)')
ax.set_title('2014-2024东亚范围地震震源深度分析')


ax.legend()

plt.show()