# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 14:15:01 2018

@author: Matteo
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 22:51:06 2018

@author: Matteo
"""

import pandas as pd
import numpy as np
import itertools
from time import gmtime, strftime
import datetime
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

if __name__ == '__main__':
    results = {}
    results['alldays'] = {}
    results['alldays']['car2go'] = {}
    results['alldays']['car2go']['sex'] = ["1","2"]
    results['alldays']['car2go']['eta'] = ["1","2","3"]
    results['alldays']['car2go']['scopo'] = ["1","2","3","6","7","8","11"]
    
    results['alldays']['total'] = {}
    results['alldays']['total']['sex'] = ["1","2"]
    results['alldays']['total']['eta'] = ["1","2","3"]
    results['alldays']['total']['scopo'] = ["1","2","3","6","7","8","11"]
     
    results['alldays']['enjoy'] = {}
    results['alldays']['enjoy']['sex'] = ["1","2"]
    results['alldays']['enjoy']['eta'] = ["1","2","3"]
    results['alldays']['enjoy']['scopo'] = ["1","2","3","6","8","11"]
    
    #for weekends
    results['weekends'] = {}
    results['weekends']['car2go'] = {}
    results['weekends']['car2go']['sex'] = ["1","2"]
    results['weekends']['car2go']['eta'] = ["1","2"]
    results['weekends']['car2go']['scopo'] = ["1","2","3","7","8","11"]
    
    results['weekends']['total'] = {}
    results['weekends']['total']['sex'] = ["1","2"]
    results['weekends']['total']['eta'] = ["1","2","3"]
    results['weekends']['total']['scopo'] = ["1","2","3","6","7","8","11"]
     
    results['weekends']['enjoy'] = {}
    results['weekends']['enjoy']['sex'] = ["1","2"]
    results['weekends']['enjoy']['eta'] = ["1","2","3"]
    results['weekends']['enjoy']['scopo'] = ["1","2","3","8","6"]
    
    #for workingdays
    results['weekdays'] = {}
    results['weekdays']['car2go'] = {}
    results['weekdays']['car2go']['sex'] = ["1","2"]
    results['weekdays']['car2go']['eta'] = ["1","2","3"]
    results['weekdays']['car2go']['scopo'] = ["1","2","3","6","7","8","11"]
    
    results['weekdays']['total'] = {}
    results['weekdays']['total']['sex'] = ["1","2"]
    results['weekdays']['total']['eta'] = ["1","2","3"]
    results['weekdays']['total']['scopo'] = ["1","2","3","6","7","8"]
     
    results['weekdays']['enjoy'] = {}
    results['weekdays']['enjoy']['sex'] = ["1","2"]
    results['weekdays']['enjoy']['eta'] = ["2","1"]
    results['weekdays']['enjoy']['scopo'] = ["1","2","3","8"]
    
    #%%morning
    results['morning'] = {}
    results['morning']['car2go'] = {}
    results['morning']['car2go']['sex'] = ["1","2"]
    results['morning']['car2go']['eta'] = ["1","2","3"]
    results['morning']['car2go']['scopo'] = ["1","2","3","6","7","11"]
    
    results['morning']['total'] = {}
    results['morning']['total']['sex'] = ["1","2"]
    results['morning']['total']['eta'] = ["1","2","3"]
    results['morning']['total']['scopo'] = ["1","2","3","6","7","11"]
     
    results['morning']['enjoy'] = {}
    results['morning']['enjoy']['sex'] = ["1","2"]
    results['morning']['enjoy']['eta'] = ["2","3"]
    results['morning']['enjoy']['scopo'] = ["1","2","3","6","11"]
    
    #%% afternoon
    results['afternoon'] = {}
    results['afternoon']['car2go'] = {}
    results['afternoon']['car2go']['sex'] = ["1","2"]
    results['afternoon']['car2go']['eta'] = ["1","2"]
    results['afternoon']['car2go']['scopo'] = ["1","2","3","8","11"]
    
    results['afternoon']['total'] = {}
    results['afternoon']['total']['sex'] = ["1","2"]
    results['afternoon']['total']['eta'] = ["1","2"]
    results['afternoon']['total']['scopo'] = ["1","2","3","8","11"]
     
    results['afternoon']['enjoy'] = {}
    results['afternoon']['enjoy']['sex'] = ["1","2"]
    results['afternoon']['enjoy']['eta'] = ["1","2","3"]
    results['afternoon']['enjoy']['scopo'] = ["1","2","3","6","8","11"]
    
    

    
    for fld in ['alldays','weekends','weekdays','afternoon','morning']:
        #print ('Working on '+fld)
        folder = 'C:\\Users\\Matteo\\Desktop\\lab1es2\\transport\lab2'
        #folder = '.'
        #dc = pd.read_csv(folder+'/spostamenti.csv',keep_default_na=False)
        dc = pd.read_excel(folder+'/spostamenti.xlsx')
        dc = dc.rename(columns =({'PROV_PAR':'COUNT'}))
        
        enjoy_all = pd.read_excel(folder+'\\'+fld+'\\carsharing_'+fld+'.xlsx','Sheet3')
        car2go_all = pd.read_excel(folder+'\\'+fld+'\\carsharing_'+fld+'.xlsx','Sheet4')
        total_all = pd.read_excel(folder+'\\'+fld+'\\carsharing_'+fld+'.xlsx','Sheet5')
    #%%Normalizing
        
        writer = pd.ExcelWriter('final_'+ fld+'.xlsx')
        
        norm = {}
        norm['enjoy_'+fld] =enjoy_all/enjoy_all.values.sum()
        norm['enjoy_'+fld].to_excel(writer,sheet_name='enjoy')
        norm['car2go_'+fld] = car2go_all/car2go_all.values.sum()
        norm['car2go_'+fld].to_excel(writer,sheet_name='car2go')
        norm['total_'+fld] = total_all/total_all.values.sum()
        norm['total_'+fld].to_excel(writer,sheet_name = 'all')
    #%% Getting indexes
        temp = norm['enjoy_'+fld].stack()
        indexes = temp.index.values
        
    
    #%%Data from previous analysis
        
    #for all days
        
        
        for index in results[fld].keys():
            #print ('\tWorking on '+index)
            dg = dc.copy()
            dg = dg.loc[dg['SESSO'].isin(results[fld][index]['sex'])]
            dg = dg.loc[dg['FASCIA_ETA'].isin(results[fld][index]['eta'])]
            dg = dg.loc[dg['SCOPO'].isin(results[fld][index]['scopo'])]
            pvt = pd.pivot_table(dg,index=["COD_ZONA_PAR","COD_ZONA_ARR"],values=["COUNT"],aggfunc=np.sum)
            pvt = pvt.reindex(indexes)
            pvt = pvt.unstack()
            pvt = pvt.fillna(0)
            norm_pvt = pvt/pvt.values.sum()
            norm_pvt.to_excel(writer, sheet_name = 'pvt_'+index)
            distance = np.abs(norm[index+'_'+fld].values - norm_pvt.values)
            print (fld,index,distance.sum())
            #distance.to_excel(folder+'\\all_days\\final.xlsx')
    
            test4  = norm_pvt.values.sum()
                    
        writer.save()
            
        
        
    
   