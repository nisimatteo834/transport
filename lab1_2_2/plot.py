# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 11:07:34 2018

@author: Matteo
"""

from matplotlib import pyplot
import json
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
        data = folder + '/'+ city + '_ng_p.dat'
        f = open(data,'r')
        data_lines = f.readlines()
        for l in data_lines:
            minutes = float(l.split(' ')[2])
            
            if minutes < 180 and minutes > 2:
                y[city].append(minutes)
        fig = pyplot.figure(i,figsize = (20,10))
        i=i+1
        values,base = np.histogram(y[city],bins=40,normed=1)
        norm1 = values/np.linalg.norm(values)
        
        cumulative[city] = np.cumsum(values)
        pyplot.plot(base[:-1],cumulative[city],c='blue')
        pyplot.xlabel('Minutes')
        
        if city == 'to':
            pyplot.title('CDF bookings in Torino in September 2017')
            fig.savefig(folder + '/booking_'+city+'_ng_p.png')
        elif city == 'ny':
            pyplot.title('CDF bookings in NYC in September 2017')
            fig.savefig(folder + '/booking_'+city+'_ng_p.png')
        elif city == 'ma':
            pyplot.title('CDF bookings in Madrid in September 2017')
            fig.savefig(folder + '/booking_'+city+'_ng_p.png')
    
    fig = pyplot.figure(i,figsize = (20,10))
    for city in ['to','ny','ma']:
        pyplot.plot(cumulative[city],label=city)
        pyplot.legend()
        fig.savefig(folder + '/total_ng_p.png')
        

             
        