import xlrd
import csv
import os
import random
import matplotlib.pyplot as plt
from collections import defaultdict

fr=open('file.txt','r',encoding='UTF-8')
for file in fr:
    file = file.strip('\n')
    table=xlrd.open_workbook(file+'.xlsx')
    sheet=table.sheets()[0]
    rows=sheet.nrows
    rider=defaultdict(list)
    rider_lo=defaultdict(list)
    rider_la=defaultdict(list)
    rider_time=defaultdict(list)
    longitude=[]
    latitude=[]

    for row in range(1,rows):
        rowvalue=sheet.row_values(row)
        Lo_gps=rowvalue[4]
        La_gps=rowvalue[3]
        longitude.append(Lo_gps)
        latitude.append(La_gps)
        time_gps=rowvalue[2]
        val=[Lo_gps,La_gps,time_gps]
        rider[str(rowvalue[0])].append(val)
        rider_lo[str(rowvalue[0])].append(Lo_gps)
        rider_la[str(rowvalue[0])].append(La_gps)
        rider_time[str(rowvalue[0])].append(time_gps)

    i=0
    if not os.path.exists(file):
        os.makedirs(file)
    for key_rider in rider.keys():
        if i>3:
            break
        print(rider_lo[key_rider])
        csvF=open('./'+file+'/'+'loc&gps'+str(key_rider)+'.csv','w+',newline="")
        csvwriter=csv.writer(csvF)
        csvwriter.writerow(['longitude','latitude'])
        csvwriter.writerow(rider_lo[key_rider])
        csvwriter.writerow(rider_la[key_rider])
        csvwriter.writerow(rider_time[key_rider])
        csvF.close()
        plt.scatter(rider_lo[key_rider],rider_la[key_rider])
        plt.plot(rider_lo[key_rider],rider_la[key_rider])
        i+=1
    plt.title(file)
    plt.xlabel("Rider_Longitude")
    plt.ylabel("Rider_Latitud")
    plt.savefig('./'+file+'/'+file+'.png')
    #plt.show()
    plt.close()

    
