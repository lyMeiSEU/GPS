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
    Lo=defaultdict(list)
    La=defaultdict(list)

    for row in range(1,rows):
        rowvalue=sheet.row_values(row)
        LoN=[rowvalue[9],rowvalue[3]]
        LaN=[rowvalue[10],rowvalue[2]]
        Lo[str(rowvalue[0])].append(LoN)
        La[str(rowvalue[0])].append(LaN)
        detected_time=rowvalue[4]
        val=[LoN,detected_time,LaN]
        rider[str(rowvalue[0])].append(val)


    if not os.path.exists(file):
        os.makedirs(file)
    for key_rider in rider.keys():
        print(rider[key_rider])
        csvF=open('./'+file+'/'+'loc&gps'+str(key_rider)+'.csv','w+',newline="")
        csvwriter=csv.writer(csvF)
        csvwriter.writerow(rider[key_rider])
        csvF.close()
        for i in range(0,len(Lo[key_rider])-1):
            plt.plot(Lo[key_rider][i],La[key_rider][i])
            plt.scatter(Lo[key_rider][i],La[key_rider][i])
        plt.title(file)
        plt.xlabel(str(key_rider)+' logitude_diff')
        plt.ylabel(str(key_rider)+' latitude_diff')
        plt.savefig('./'+file+'/'+file+str(key_rider)+'.png')
        plt.show()
plt.close()

    
