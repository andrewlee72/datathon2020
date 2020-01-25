import csv
import numpy
from scipy.stats.stats import pearsonr

namescsvf = open('ACS2017_v01_Codebook.xlsx - ACS_2017.csv')
namesreader = csv.reader(namescsvf)
namesd = []
for row in namesreader:
    namesd.append(row)
namesd = numpy.array(namesd)
names = {}
for i in range(len(namesd)):
    names[namesd[i][1].lower()] = namesd[i][5]
extranames = ['sumlevel', 'stfips', 'county', 'tract', 'blkgrp', 'tothhlang']
for i in extranames:
    names[i] = i

datacsvf = open('ACS20175Harris_BG_v01.csv')
datareader = csv.reader(datacsvf)
data = []
for row in datareader:
    data.append(row)
heads = data[0][2:]
data = numpy.array(data[1:])
data = data.transpose()[2:]
data[data == ''] = 0
data = data.astype(numpy.float)
things = []
for i in range(len(data)):
    for j in range(i+1, len(data)):
        things.append((pearsonr(data[i], data[j])[0]**2, names[heads[i].lower()], names[heads[j].lower()]))
things = sorted(things, reverse=True)
for i in things:
    print(i)
