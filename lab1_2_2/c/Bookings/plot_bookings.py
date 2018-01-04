# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:34:55 2018

@author: Matteo
"""


from matplotlib import pyplot
import numpy as np
import os


if __name__=='__main__':
    i = 1
    y = {}
    cumulative = {}

    for city in ['to','ny','ma']:
        y[city] = {}
        y[city][1] = []
        y[city][2] = []
        y[city][3] = []
        y[city][4] = []
        cumulative[city]= {}
        cumulative[city][1] = []
        cumulative[city][2] = []
        cumulative[city][3] = []
        cumulative[city][4] = []
        

        cumulative[city] = {}
        folder = os.path.dirname(os.path.abspath(__file__))
        data = folder + '/'+ city + '_ng.dat'
        f = open(data,'r')
        data_lines = f.readlines()
        for l in data_lines:
            minutes = float(l.split(' ')[2])
            day = int(l.split(' ')[1])
            
            if minutes < 180 and minutes > 2:
                if day <=7:
                    y[city][1].append(minutes)
                    
                if day > 7 and day<15:
                    y[city][2].append(minutes)
                    
                if day > 14 and day <22:
                    y[city][3].append(minutes)
                    
                if day > 21 and day < 29:
                    y[city][4].append(minutes)
#%%
        fig = pyplot.figure(i,figsize = (10,5))
        for j in [1,2,3,4]:
            i=i+1
            bins = np.arange(np.floor(min(y[city][j])),np.ceil(max(y[city][j])))
            values,base = np.histogram(y[city][j],bins=bins,density=1)
            #norm1 = values/np.linalg.norm(values)            
            cumulative[city][j] = np.cumsum(values)            

            pyplot.plot(base[:-1],cumulative[city][j],label="Week"+str(j))
            pyplot.xlabel('Minutes')
            
        if city == 'to':
            pyplot.title('CDF bookings in Torino in September 2017 divided by weeks')
            fig.savefig(folder + '/'+city+'_booking_ng.png')
        elif city == 'ny':
            pyplot.title('CDF bookings in NYC in September 2017 divided by weeks')
            fig.savefig(folder + '/'+city+'_booking_ng.png')
        elif city == 'ma':
            pyplot.title('CDF bookings in Madrid in September 2017 divided by weeks')
            fig.savefig(folder + '/'+city+'_booking_ng.png')
        pyplot.legend()
        pyplot.show()
            
#%%
    
