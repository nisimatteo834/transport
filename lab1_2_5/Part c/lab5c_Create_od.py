# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 20:29:42 2018

@author: Asus
"""
import numpy as np
import geopandas as gpd
import geojsonio
from shapely.geometry import Point, Polygon
from time import gmtime, strftime
import datetime

if __name__ == '__main__':
    
    fileZones="zones.txt"
    data1 = open(fileZones,"r")
    datazone = data1.readlines()
    data1.close()
    #print(datazone)
    zones=[]    
    for zone in datazone:
        zones.append(int(zone))
    print(zones)
    
    fileName = "trips.txt"
    states = gpd.read_file('geojson_zones.txt')

    
    states['centroid_column'] = states.centroid

    states = states.set_geometry('geometry')

    
    
    file = open(fileName,"r")
    data = file.readlines()
    file.close()
    
    
    #dimention = (1600,1600)
    dimention = (272,272)
    matrix = np.zeros(dimention)
    #print(matrix)
    counter = 0
    start = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    print ('Starting at',start)
    
    for i in data:
        counter +=1
        print(counter)
        result =""
        index1 = 0.5
        index2 = 0.5
        origin, destination = [a.strip() for a in i.split(' | ')]
        #print(origin, destination)
        org = origin.split(',')
        a= tuple(float(x) for x in org)
        o=Point(a)
        #print(o)
        des = destination.split(',')
        b= tuple(float(x) for x in des)
        d=Point(b)
        #print(d)
        for j in range (1,(len(zones)+1)):
            poly1 = states['geometry'][zones[j-1]]
            if(poly1.contains(o)):
                result = str(j-1)
                index1=j-1
        
        for k in range (1,(len(zones)+1)):
            poly2 = states['geometry'][zones[k-1]]
            if(poly2.contains(d)):
                result = result +" to " +str(k-1)
                index2=k-1
        
        if(result != ""):
            print(result)
            
        if(index1 != 0.5 and index2 != 0.5):
            matrix[index1][index2] += 1
            print("add")
            print(matrix[index1][index2])

    end = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    
    cons = (states['centroid_column'][800])    
    if(poly.contains(cons)):
        print("yes")
    
    print(start,end)    
    print(matrix)


	#with open('output.txt', 'wb') as f:
    with open('output2.txt', 'wb') as f:
        np.savetxt(f, matrix.astype(int), delimiter=',')
