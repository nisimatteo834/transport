# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 00:09:10 2018

@author: Asus
"""
import pandas as pd
import numpy as np
import itertools
from time import gmtime, strftime
import datetime

if __name__ == '__main__':
    #folder = 'C:\\Users\\Matteo\\Desktop\\lab1es2\\transport'
    folder = '.'
    #dc = pd.read_csv(folder+'/spostamenti.csv',keep_default_na=False)
    dc = pd.read_excel(folder+'/spostamenti.xlsx')
    dc = dc.rename(columns =({'PROV_PAR':'COUNT'}))
    
    #enjoy = pd.read_excel(folder+'/carsharing_alldays.xlsx','enjoy')
    #car2go = pd.read_excel(folder+'/carsharing_alldays.xlsx','car3go')
    #total = pd.read_excel(folder+'/carsharing_alldays.xlsx','Total')
    enjoy = pd.read_excel(folder+'/carsharing_alldays.xlsx','Sheet3')
    car2go = pd.read_excel(folder+'/carsharing_alldays.xlsx','Sheet4')
    total = pd.read_excel(folder+'/carsharing_alldays.xlsx','Sheet5')
#%%Normalizing
    #summ = enjoy.values.sum()
    norm_enjoy =enjoy/enjoy.values.sum()
    test1  = norm_enjoy.values.sum()      
    norm_car2go = car2go/car2go.values.sum()
    test2  = norm_car2go.values.sum()
    norm_total = total/total.values.sum()
    test3  = norm_total.values.sum()
#%% Getting indexes
    temp = norm_enjoy.stack()
    indexes = temp.index.values
    

#%%Acting on data for pivot
    fascia_eta = ["1","2","3","4"]    
    sesso =["1","2"]    
    scopo_list = ["8"] #["1","2","3","4","5","6","7","8","9","10","11"]
#%% Pivot Table

    dg = dc.copy()
    dg = dg.loc[dc['SESSO'].isin(sesso)]
    dg = dg.loc[dc['FASCIA_ETA'].isin(fascia_eta)]
    dg = dg.loc[dc['SCOPO'].isin(scopo_list)]
    pvt = pd.pivot_table(dg,index=["COD_ZONA_PAR","COD_ZONA_ARR"],values=["COUNT"],aggfunc=np.sum)
    pvt = pvt.reindex(indexes)
    pvt = pvt.unstack()
    pvt = pvt.fillna(0)
#%% Calculating Distance    
    l = 0
    best_enjoy= []
    best_car2go= []
    best_total= []
    
    sum_enjoy=1.0
    sum_car2go=1.0
    sum_total=1.0

    start = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    print ('Starting at',start)
    
    norm_pvt = pvt/pvt.values.sum()
    test4  = norm_pvt.values.sum()
    distance_enjoy = np.abs(norm_enjoy.values - norm_pvt.values)
    distance_car2go = np.abs(norm_car2go.values - norm_pvt.values)
    distance_total = np.abs(norm_total.values - norm_pvt.values)
                                
                                
    best_enjoy.clear()
    sum_enjoy = distance_enjoy.sum()
    best_enjoy.append(sesso)
    best_enjoy.append(fascia_eta)
    best_enjoy.append(scopo_list)
                                
    best_car2go.clear()
    sum_car2go = distance_car2go.sum()
    best_car2go.append(sesso)
    best_car2go.append(fascia_eta)
    best_car2go.append(scopo_list)
                                
    best_total.clear()
    sum_total = distance_total.sum()
    best_total.append(sesso)
    best_total.append(fascia_eta)
    best_total.append(scopo_list)
                                
    #%%                        
    end = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    print ('Best Total',best_total,sum_total)
    print ('Best Car2Go',best_car2go,sum_car2go)
    print ('Best Enjoy',best_enjoy,sum_enjoy)
    print (start,end,l)

                        
                    
                
    
    
    
    