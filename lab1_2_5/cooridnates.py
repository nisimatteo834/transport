# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 11:24:47 2018

@author: Matteo
"""
import sys
from math import sin, cos, sqrt, atan2, radians
import numpy as np


print (sys.path)

file = open('zones.txt','w+')

stringa = '{\"type\": \"FeatureCollection\",\"features\": ['

coordinates = [[
              7.513275146484376,
              44.96917023288551
            ],
            [
              7.77557373046875,
              44.96917023288551
            ],
            [
              7.77557373046875,
              45.15008475740563
            ],
            [
              7.513275146484376,
              45.15008475740563
            ]]
            
R = 6373.0
lon1 = radians(coordinates[0][0])
lon2 = radians(coordinates[1][0])
lat1 = radians(coordinates[0][1])
lat2 = radians(coordinates[1][1])

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

hor_distance = R * c

lon1 = radians(coordinates[0][0])
lon2 = radians(coordinates[3][0])
lat1 = radians(coordinates[0][1])
lat2 = radians(coordinates[3][1])

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))
ver_distance = R * c


number_hor = hor_distance/0.5
number_ver = ver_distance/0.5
size = int(np.floor(min(number_hor,number_ver)))
dist_inlat = (coordinates[3][1]-coordinates[0][1])/number_ver
dist_inlong = (coordinates[1][0]-coordinates[0][0])/number_hor  

zones_of_500 = []
square = []
square.append(coordinates[0])
square.append([square[0][0]+dist_inlong,square[0][1]])
square.append([square[1][0],square[1][1]+dist_inlat])
square.append([square[0][0],square[0][1]+dist_inlat])
square.append(square[0])
zones_of_500.append(square)

for i in range(0,size):
    if (i!=0):
        row_up = zones_of_500[size*(i-1)]
        square = []
        square.append([row_up[0][0],row_up[0][1]+dist_inlat])
        square.append([row_up[1][0],row_up[1][1]+dist_inlat])
        square.append(row_up[1])
        square.append(row_up[0])
        square.append(square[0])
        zones_of_500.append(square)
    for j in range(1,size):
        square = []
        square.append(zones_of_500[40*i+j-1][1])
        square.append([square[0][0]+dist_inlong,square[0][1]])
        square.append([square[1][0],square[1][1]+dist_inlat])
        square.append([square[0][0],square[0][1]+dist_inlat])
        square.append(square[0])
        zones_of_500.append(square)

zones = "["    
for i in range(int(len(zones_of_500))):
    zones += "["
    zones += str(zones_of_500[i])
    zones += "]"

    if i<len(zones_of_500)-1:
        zones += ","
zones += "]"

file.write(zones)    


for i in range(len(zones_of_500)):
    stringa += '{\"type\": \"Feature\",\"properties\": {},\"geometry\": {\"type\": \"Polygon\",\"coordinates\":[';
    stringa += str(zones_of_500[i])
    stringa += ']}}'
    if i<len(zones_of_500)-1: stringa+=','
    
stringa += ']}'
#
#polys = []
#for x in zones_of_500:
#    poly = Polygon( ((x[0], x[0]), (x[0], x[1]), (x[1], x[1]), (x[0], x[0])) )
#    polys.append(poly)    

        
geojson = open('geojson.txt','w+')
geojson.write(stringa)

print (zones)

centroids = []
centroid = open('centroid.csv','w+')
centroid.write('number,long,lat\n')
for i in range(len(zones_of_500)):
    lat = (zones_of_500[i][1][1]-dist_inlong/2)
    lat = lat + dist_inlat/2;
    long = (zones_of_500[i][1][0]-dist_inlong/2)
    stringa = (str(i)+','+str(long)+','+str(lat)+'\n')
    centroids.append((long,lat))
    print (stringa)
    centroid.write(stringa)

    