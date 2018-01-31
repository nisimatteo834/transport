# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:34:55 2018

@author: Matteo
"""


from matplotlib import pyplot
from scipy.stats import norm
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
        y[city]['tot']=[]
        cumulative[city]= {}
        cumulative[city][1] = []
        cumulative[city][2] = []
        cumulative[city][3] = []
        cumulative[city][4] = []
        cumulative[city]['tot'] = []
        week4 = {}
        week4[24] = []
        week4[25] = []
        week4[26] = []
        week4[27] = []
        week4[28] = []
        week4[29] = []
        week4[30] = []
        

        cumulative[city] = {}
        folder = os.path.dirname(os.path.abspath(__file__))
        data = folder + '/'+ city + '_ng_p.dat'
        f = open(data,'r')
        data_lines = f.readlines()
        for l in data_lines:
            minutes = float(l.split(' ')[2])
            day = int(l.split(' ')[1])
            
            if minutes < 180 and minutes > 2:
                y[city]['tot'].append(minutes);

                if day >2 <=9:
                    y[city][1].append(minutes)
                    
                if day > 9 and day<17:
                    y[city][2].append(minutes)
                    
                if day > 16 and day <24:
                    y[city][3].append(minutes)
                    
                if day > 23:
                    y[city][4].append(minutes)
                    week4[day].append(minutes)
#%%
        fig = pyplot.figure(i,figsize = (20,10))
        i=i+1
        
        bins = np.arange(np.floor(min(y[city]['tot'])),np.ceil(max(y[city]['tot'])))
        values,base = np.histogram(y[city]['tot'],bins=bins,density=1)
        cumulative[city]['tot'] = np.cumsum(values)
        pyplot.plot(base[:-1],cumulative[city]['tot'],'b*',label="Month")
        
        for j in [1,2,3,4]:
            bins = np.arange(np.floor(min(y[city][j])),np.ceil(max(y[city][j])))
            values,base = np.histogram(y[city][j],bins=bins,density=1)
            #norm1 = values/np.linalg.norm(values)            
            cumulative[city][j] = np.cumsum(values)
          

            pyplot.plot(base[:-1],cumulative[city][j],label="Week"+str(j))
            pyplot.xlabel('Minutes')
        
        pyplot.legend(prop={'size':15})

        if city == 'to':
            pyplot.title('CDF parkings in Torino in September 2017 divided by weeks')
            fig.savefig(folder + '/'+city+'_parkings_ng.png')
        elif city == 'ny':
            pyplot.title('CDF parkings in NYC in September 2017 divided by weeks')
            fig.savefig(folder + '/'+city+'_parkings_ng.png')
        elif city == 'ma':
            pyplot.title('CDF parkings in Madrid in September 2017 divided by weeks')
            fig.savefig(folder + '/'+city+'_parkings_ng.png')
        pyplot.close(fig)
            
#%%
        fig = pyplot.figure(i,figsize = (20,10))
        i=i+1
        bins = np.arange(np.floor(min(y[city][4])),np.ceil(max(y[city][4])))
        values,base = np.histogram(y[city][4],bins=bins,density=1)
        cum = np.cumsum(values)
        pyplot.plot(base[:-1],cumulative[city][4],label="Week4",linewidth=3.0)
         
        week = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
        for j in range(24,31): 
            bins = np.arange(np.floor(min(week4[j])),np.ceil(max(week4[j])))
            values,base = np.histogram(week4[j],bins=bins,density=1)
            cum = np.cumsum(values)
            pyplot.plot(base[:-1],cum,label=week[j-24]+' '+str(j))
        
        pyplot.legend(prop={'size':15})
        if city == 'to':
            pyplot.title('CDF bookings in Torino in September 2017 divided by day of week')
            fig.savefig(folder + '/'+city+'_parking_4w.png')
        elif city == 'ny':
            pyplot.title('CDF bookings in NYC in September 2017 divided by day of week')
            fig.savefig(folder + '/'+city+'_parking_4w.png')
        elif city == 'ma':
            pyplot.title('CDF bookings in Madrid in September 2017 divided by day of week')
            fig.savefig(folder + '/'+city+'_parking_4w.png')
        pyplot.close(fig)
        


pyplot.show()
