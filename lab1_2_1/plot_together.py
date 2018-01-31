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

    fig = pyplot.figure(1, figsize=(20, 10))

    for city in cities:
        folder = os.path.dirname(os.path.abspath(__file__))

        # %% Bookings filtered

        bookings = folder + '/booking_' + city + '.dat'
        f = open(bookings, 'r')
        booking_lines = f.readlines()
        bookings = {}
        previous = int(booking_lines[0].split(' ')[2]) - 1
        y = []
        for l in booking_lines:
            key = l.split(' ')[2]
            value = int(l.split(' ')[1])

            while int(key) - previous != 1:
                bookings[str(previous + 1)] = 0
                y.append(str(0))
                previous += 1

            bookings[key] = value
            y.append(l.split(' ')[1])
            previous = int(key)

        f.close()

#        fig = pyplot.figure(1, figsize=(20, 10))
        x = np.linspace(1, 30, 720)
        pyplot.plot(x, list(bookings.values()), label=city)
        pyplot.xlim(0.5, 30.5)
        pyplot.xlabel('Day of the Month')
        pyplot.ylabel('#Bookings')
        pyplot.title('Filtered Bookings per Hour of the Day in September 2017')# in ' + city)
        pyplot.legend()
        fig.savefig(folder + '/booking1.png')
        
        #%%
    fig = pyplot.figure(2, figsize=(20, 10))
    pyplot.title('Parkings per Hour of the Day in September 2017')
    pyplot.xlabel('Day of the Month')
    pyplot.ylabel('#Parkings')


    for city in cities:
        parkings = folder + '/parking_' + city + '.dat'
        f = open(parkings, 'r')
        parking_lines = f.readlines()
        x = []
        y = []
        parkings = {}
        previous = int(parking_lines[0].split(' ')[2]) - 1

        for l in parking_lines:
            key = l.split(' ')[2]
            value = int(l.split(' ')[1])
            while int(key) - previous != 1:
                parkings[str(previous + 1)] = 0
                y.append(str(0))
                previous += 1

            parkings[key] = value
            y.append(l.split(' ')[1])
            previous = int(key)

        x = np.linspace(1, 30, 720)
        pyplot.plot(x, list(parkings.values()), label=city)
        pyplot.xlim(0.5, 30.5)
        pyplot.legend()
        fig.savefig(folder + '/parkings.png')
    f.close()
    
    
    
