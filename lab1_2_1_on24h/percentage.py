# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 13:31:14 2018

@author: Matteo
"""
import matplotlib
from matplotlib import pyplot
import os


if __name__=='__main__':
    bookings_d = {}
    parkings_d = {}
    cities = ['MA','TO','NY']
    
    for city in cities:
        folder = os.path.dirname(os.path.abspath(__file__))
        #%% Bookings filtered
        bookings = folder + "/booking_"+city+".dat"    
        f=open(bookings,"r")
        booking_lines=f.readlines()
        bookings_d[city] = {}
        previous = -1
        y = []
        for l in booking_lines:
            key = int(l.split(' ')[1])
            value = int(l.split(' ')[2])        
    
            while (int(key) - previous) != 1:
                bookings_d[city][previous+1] = 0
                previous += 1
                
            bookings_d[city][key] = value
            previous = int(key)
            
                    
        
        f.close()       

        
        #%% Parkings filtered
        parkings = folder + "/parking_"+city+".dat"    
        f=open(parkings,"r")
        parking_lines=f.readlines()
        x=[]
        y=[]
        previous = -1
        parkings_d[city] = {}
        
        for l in parking_lines:
            key = int(l.split(' ')[1])
            value = int(l.split(' ')[2])   
            while (int(key) - previous) != 1:
                parkings_d[city][previous+1] = 0
                previous += 1
                
            parkings_d[city][key] = value
            previous = key
            
        f.close()
    
#%% computing percentage
    percentage_b = {}
    percentage_p = {}
    total = {}
    fig = pyplot.figure(3, figsize=(20,10))
    matplotlib.rcParams.update({'font.size': 35})

    pyplot.title('Percentage of Bookings per Hour of the Day in September 2017')
    pyplot.xlabel('Day of the Month')
    pyplot.ylabel('Utilization Factor')
    for city in cities:
        percentage_b[city] = {}
        percentage_p[city] = {}
        total[city] = {}
        for hour in bookings_d[city]:
            try:
                total[city][hour] = bookings_d[city][hour] + parkings_d[city][hour]
            except KeyError as e:
                print ('Missing Values')
                total[city][hour] = -1
                           
            
            try:
                percentage_b[city][hour] = float(bookings_d[city][hour])/total[city][hour]
            except ZeroDivisionError as zerodiv:
                percentage_b[city][hour] = 0
        x = np.linspace(0, 23, 24)
        pyplot.plot(x, list(percentage_b[city].values()), label=city,linewidth=3.5)
        pyplot.legend()
        fig.savefig(folder + '/percentage.png')
    
      
        
        
    
        