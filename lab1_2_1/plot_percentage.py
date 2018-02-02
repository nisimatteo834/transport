# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 12:31:41 2018

@author: Matteo
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:37:27 2018

@author: Matteo
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-
from matplotlib import pyplot
import json
import numpy as np
import os

if __name__ == '__main__':

    cities = ['MA', 'TO', 'NY']
    differences = {}
    not_filtered = {}
    bookings_d = {}
    


        # %% Bookings filtered

    fig = pyplot.figure(1, figsize=(10,5))

    for city in cities:
        folder = os.path.dirname(os.path.abspath("__file__"))
        bookings = folder + '/booking_' + city + '.dat'

        f = open(bookings, 'r')
        booking_lines = f.readlines()
        bookings_d[city] = {}
        previous = int(booking_lines[0].split(' ')[2]) - 1
        y = []
        for l in booking_lines:
            key = int(l.split(' ')[2])
            value = int(l.split(' ')[1])

            while int(key) - previous != 1:
                bookings_d[city][previous + 1] = 0
                y.append(str(0))
                previous += 1

            bookings_d[city][key] = value
            y.append(l.split(' ')[1])
            previous = int(key)

        f.close()

#        fig = pyplot.figure(1, figsize=(10,5))
        x = np.linspace(1, 30, 720)
        pyplot.plot(x, list(bookings_d[city].values()), label=city)
        pyplot.xlim(0.5, 30.5)
        pyplot.xlabel('Day of the Month')
        pyplot.ylabel('#Bookings')
        pyplot.title('Filtered Bookings per Hour of the Day in September 2017')# in ' + city)
        pyplot.legend()
        fig.savefig(folder + '/booking_perc.png')
        
        #%%
    fig = pyplot.figure(2, figsize=(10,5))
    pyplot.title('Parkings per Hour of the Day in September 2017')
    pyplot.xlabel('Day of the Month')
    pyplot.ylabel('#Parkings')


    parkings_d = {}
    for city in cities:
        parkings = folder + '/parking_' + city + '.dat'
        f = open(parkings, 'r')
        parking_lines = f.readlines()
        x = []
        y = []
        parkings_d[city] = {}
        previous = int(parking_lines[0].split(' ')[2]) - 1

        for l in parking_lines:
            key = int(l.split(' ')[2])
            value = int(l.split(' ')[1])
            while int(key) - previous != 1:
                parkings_d[city][previous + 1] = 0
                y.append(str(0))
                previous += 1

            parkings_d[city][key] = value
            y.append(l.split(' ')[1])
            previous = int(key)
        f.close()


        x = np.linspace(1, 30, 720)
        pyplot.plot(x, list(parkings_d[city].values()), label=city)
        pyplot.xlim(0.5, 30.5)
        pyplot.legend()
        fig.savefig(folder + '/parkings_perc.png')
    
    
    #%% computing percentage
    percentage_b = {}
    percentage_p = {}
    total = {}
    fig = pyplot.figure(3, figsize=(20,10))
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
        x = np.linspace(1, 30, 720)
        pyplot.plot(x, list(percentage_b[city].values()), label=city)
        pyplot.xlim(0.5, 30.5)
        pyplot.legend(prop={'size':20})
        fig.savefig(folder + '/percentage.png')
        
    
    
    
    
