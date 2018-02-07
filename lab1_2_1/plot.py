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
    matplotlib.rcParams.update({'font.size': 35})


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

        fig = pyplot.figure(1, figsize=(20, 10))
        x = np.linspace(1, 30, 720)
        pyplot.plot(x, list(bookings.values()), label='Bookings')
        pyplot.xlim(0.5, 30.5)
        pyplot.xlabel('Day of the Month')
        pyplot.ylabel('#Bookings')
        pyplot.title('Filtered Bookings per Hour of the Day in September 2017 in ' + city)
        pyplot.legend()
        fig.savefig(folder + '/booking1_' + city + '.png')

        # %%Bookings not filtered

        # Interesting to notice
        # if we put as a filter that the car has     to move we go from a max of 900 cases to less than 20

        bookings_nf = folder + '/booking_nf_' + city + '.dat'
        f = open(bookings_nf, 'r')
        booking_lines = f.readlines()
        y = []
        y_nf = []
        bookings_nf = {}
        difference = {}
        previous = int(booking_lines[0].split(' ')[2]) - 1

        for l in booking_lines:
            key = l.split(' ')[2]
            value = int(l.split(' ')[1])
            while int(key) - previous != 1:
                bookings_nf[str(previous + 1)] = 0
                y_nf.append(str(0))
                previous += 1

            bookings_nf[key] = value
            y_nf.append(l.split(' ')[1])
            previous = int(key)

        for l in bookings_nf:
            if l in bookings:
                y.append(bookings_nf.get(l) - bookings.get(l))
                difference[l] = bookings_nf.get(l) - bookings.get(l)
            else:
                y.append(bookings_nf.get(l))
                difference[l] = bookings_nf.get(l)

        differences[city] = y
        not_filtered[city] = y_nf
        fig = pyplot.figure(2, figsize=(20, 10))
        x = np.linspace(1, 30, 720)
        nf = pyplot.plot(x, list(bookings_nf.values()),
                         label='Not filtered')
        f = pyplot.plot(x, list(bookings.values()), label='Filtered')

        # pyplot.plot(x,list(difference.values()))
        # pyplot.plot(x,y_nf)

        pyplot.xlim(0.5, 30.5)
        pyplot.xlabel('Day of the Month')
        pyplot.ylabel('Bookings')
        pyplot.title('Comparison not_Filtered-Filtered in ' + city)
        pyplot.legend()
        fig.savefig(folder + '/comparison_booking_' + city
                    + '.png')

        fig = pyplot.figure(3, figsize=(20, 10))
        x = np.linspace(1, 30, 720)
        diff = pyplot.plot(x, list(difference.values()),
                           label='Difference')
        pyplot.xlim(0.5, 30.5)
        pyplot.xlabel('Day of the Month')
        pyplot.ylabel('Difference')
        pyplot.title('Difference not_Filtered-Filtered in ' + city)
        pyplot.legend()
        fig.savefig(folder + '/difference_booking_' + city
                    + '.png')

        # %% Parkings filtered

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

        f.close()

        fig = pyplot.figure(4, figsize=(20, 10))
        x = np.linspace(1, 30, 720)
        pyplot.plot(x, list(parkings.values()), label='Parkings')
        pyplot.xlim(0.5, 30.5)
        pyplot.xlabel('Day of the Month')
        pyplot.ylabel('#Parkings')
        pyplot.title('Parkings per Hour of the Day in September 2017 in ' + city)
        pyplot.legend()
        fig.savefig(folder + '/parkings_' + city + '.png')

        pyplot.show()

#    percentage = {}
#    x = np.linspace(1, 30, 720)
#    fig = pyplot.figure(5, figsize=(20, 10))
#    cities = ['TO']
#    for city in cities:
#        percentage[city] = []
#        for i in range(len(differences[city])):
#            
#            if (int(not_filtered[city][i])!=0):
#                percentage[city].append(int(differences[city][i])/ int(not_filtered[city][i]))
#            else:
#                percentage[city].append(0)
#
#        pyplot.plot(x, percentage[city], label=city)


			