import csv
import numpy as np
import math

namescsvf = open('ACS20175Harris_BG_v01 - ACS20175Harris_BG_v01 (1).csv')
namesreader = csv.reader(namescsvf)
namesd = np.array(list(namesreader))

schcsvf = open('SchOut - schout.csv')
schreader = csv.reader(schcsvf)
schd = np.array(list(schreader))


outPut = open('SchLangOut.csv', 'w')
outLang = csv.writer(outPut)

#loops over schools

for i in range(1, len(schd)):
    schLatt = float(schd[i, 23])
    schLong = float(schd[i, 24])
    schSumHisp = 0
    schSumAsPI = 0
    totalWeight = 0
    #loops over Census Points
    for j in range(1, len(namesd)-4):
        latt = float(namesd[j, 126])
        long = float(namesd[j, 127])
        #print(len(namesd[1,:]))
        #print(j)
        weight = math.exp(-(3/4 * (long-schLong)**2 + (latt-schLatt)**2)/.1)
        tempVal = weight * float(namesd[j, 101]) / float(namesd[j, 2])
        schSumHisp = tempVal + schSumHisp
        tempVal = weight * float(namesd[j, 102]) / float(namesd[j, 2])
        schSumAsPI = tempVal + schSumAsPI
        totalWeight += weight
    outPutter = np.array(list(schd[i, 0:25]) + list([schSumHisp/totalWeight, schSumAsPI/totalWeight]))
    print(outPutter)
    outLang.writerow(outPutter)
outPut.close()






