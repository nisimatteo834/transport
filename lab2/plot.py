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
    
    for fld in ['alldays','weekends','weekdays']:
        print ('Working on '+fld)
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
        norm['enjoy_all'] =enjoy_all/enjoy_all.values.sum()
        norm['enjoy_all'].to_excel(writer,sheet_name='enjoy')
        norm['car2go_all'] = car2go_all/car2go_all.values.sum()
        norm['car2go_all'].to_excel(writer,sheet_name='car2go')
        norm['total_all'] = total_all/total_all.values.sum()
        norm['total_all'].to_excel(writer,sheet_name = 'all')
    #%% Getting indexes
        temp = norm['enjoy_all'].stack()
        indexes = temp.index.values
        
    
    #%%Acting on data for pivot
        
        results = {}
        results['car2go'] = {}
        results['car2go']['sex'] = ["1","2"]
        results['car2go']['eta'] = ["1","2","3"]
        results['car2go']['scopo'] = ["1","2","3","6","7","8","11"]
        
        results['total'] = {}
        results['total']['sex'] = ["1","2"]
        results['total']['eta'] = ["1","2","3"]
        results['total']['scopo'] = ["1","2","3","6","7","8","11"]
         
        results['enjoy'] = {}
        results['enjoy']['sex'] = ["1","2"]
        results['enjoy']['eta'] = ["1","2","3"]
        results['enjoy']['scopo'] = ["1","2","3","6","7","8","11"]
        
        
        
        for index in results.keys():
            print ('\tWorking on '+index)
            dg = dc.copy()
            dg = dg.loc[dg['SESSO'].isin(results[index]['sex'])]
            dg = dg.loc[dg['FASCIA_ETA'].isin(results[index]['eta'])]
            dg = dg.loc[dg['SCOPO'].isin(results[index]['scopo'])]
            pvt = pd.pivot_table(dg,index=["COD_ZONA_PAR","COD_ZONA_ARR"],values=["COUNT"],aggfunc=np.sum)
            pvt = pvt.reindex(indexes)
            pvt = pvt.unstack()
            pvt = pvt.fillna(0)
            norm_pvt = pvt/pvt.values.sum()
            norm_pvt.to_excel(writer, sheet_name = 'pvt_'+index)
            distance = np.abs(norm[index+'_all'].values - norm_pvt.values)
            #distance.to_excel(folder+'\\all_days\\final.xlsx')
    
            test4  = norm_pvt.values.sum()
                    
        writer.save()
            
        
        
    
   