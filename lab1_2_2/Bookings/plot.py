# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 11:07:34 2018

@author: Matteo
"""

from matplotlib import pyplot
import matplotlib
import numpy as np
import os


if __name__=='__main__':
    i = 1
    y = {}
    cumulative = {}

    for city in ['to','ny','ma']:
        y[city] = []
        cumulative[city] = []
        folder = os.path.dirname(os.path.abspath(__file__))
        data = folder + '/'+ city + '_ng.dat'
        f = open(data,'r')
        data_lines = f.readlines()
        for l in data_lines:
            minutes = float(l.split(' ')[2])
            
            if minutes < 180 and minutes > 2:
                y[city].append(minutes)
        fig = pyplot.figure(i,figsize = (20,10))
        matplotlib.rcParams.update({'font.size': 35})

        i=i+1

        bins = np.arange(np.floor(min(y[city])),np.ceil(max(y[city])))
        values,base = np.histogram(y[city],bins=bins,density=1)
        norm1 = values/np.linalg.norm(values)
        
        cumulative[city] = np.cumsum(values)
        pyplot.plot(base[:-1],cumulative[city],c='blue',linewidth=2.0)
        pyplot.xlabel('Minutes')
        
        if city == 'to':
            pyplot.title('CDF bookings in Torino in September 2017')
            fig.savefig(folder + '/'+city+'_booking_ng.png')
        elif city == 'ny':
            pyplot.title('CDF bookings in NYC in September 2017')
            fig.savefig(folder + '/'+city+'_booking_ng.png')
        elif city == 'ma':
            pyplot.title('CDF bookings in Madrid in September 2017')
            fig.savefig(folder + '/'+city+'_booking_ng.png')
    
    fig = pyplot.figure(i,figsize = (20,10))
    matplotlib.rcParams.update({'font.size': 35})
    pyplot.title('CDF of bookings in the three cities')

    for city in ['to','ny','ma']:
        pyplot.plot(cumulative[city],label=city,linewidth=3.5)
        pyplot.legend(prop={'size': 20})
        fig.savefig(folder + '/total_bookig_ng_p.png')
        

             
        