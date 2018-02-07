# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 23:18:07 2018

@author: Matteo
"""
import matplotlib
from matplotlib import pyplot
import json
import numpy as np
import os


if __name__=='__main__':
    
    cities = ['MA','TO','NY']
    plot = {}
    plot['MA'] = 'bo'
    plot['TO'] = 'r^'
    plot['NY'] = 'g*'
    
    fig = pyplot.figure(1,figsize = (20,10))
    matplotlib.rcParams.update({'font.size': 35})
    x = np.linspace(0,23,24)
    pyplot.xticks(x)
    pyplot.xlabel('Hour of the day')
    pyplot.ylabel('#Bookings')
    pyplot.title('Bookings per Hour in September 2017 per each city')    


    for city in cities:
        folder = os.path.dirname(os.path.abspath(__file__))
        #%% Bookings filtered
        bookings = folder + "/booking_"+city+".dat"    
        f=open(bookings,"r")
        booking_lines=f.readlines()
        bookings = {}
        previous = -1
        y = []
        for l in booking_lines:
            key = l.split(' ')[1]
            value = int(l.split(' ')[2])        
    
            while (int(key) - previous) != 1:
                bookings[str(previous+1)] = 0
                y.append(str(0))
                previous += 1
                
            bookings[key] = value
            y.append(l.split(' ')[2])
            previous = int(key)
                               
        
        f.close()
        pyplot.plot(x,list(bookings.values()),label=city,linewidth=3.5)
        pyplot.xticks(x)
        pyplot.xlabel('Hour of the day')
        pyplot.ylabel('#Bookings')
        pyplot.title('Bookings per Hours in September 2017')
    pyplot.legend()
    fig.savefig(folder + '/Images/booking_discrete_on_one.png')
    #pyplot.close(fig)
    
       
        

