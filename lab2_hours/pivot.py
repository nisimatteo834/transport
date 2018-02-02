# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 22:51:06 2018

@author: Matteo
"""

import pandas as pd
import numpy as np
import itertools
from time import gmtime, strftime

if __name__ == '__main__':
    #folder = 'C:\\Users\\Matteo\\Desktop\\lab1es2\\transport'
    folder = '.'
    #dc = pd.read_csv(folder+'/spostamenti.csv',keep_default_na=False)
    dc = pd.read_excel(folder+'/spostamenti.xlsx')
    dc = dc.rename(columns =({'PROV_PAR':'COUNT'}))

    
#%%Acting on data for pivot
    fascia_eta = ["1","2","3","4"]    
    sesso = ["1","2"]    
    scopo_list = ["1","2","3","4","5","6","7","8"]#,"9","10","11"]
    #%%
    
    #df = dc.copy()
    #pvt = pd.pivot_table(df,index=["COD_ZONA_PAR","COD_ZONA_ARR"],values=["COUNT"],aggfunc=np.sum)

#%%    
    l = 0
    start = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    for i  in range(1,len(sesso)+1):
        df = dc.copy()
        sub_sex = set(itertools.combinations(sesso,i))        
        sub_sex = [list(row) for row in sub_sex]    
        for sex in sub_sex:
            for j in range(1,len(fascia_eta)+1):
                sub_fascia = set(itertools.combinations(fascia_eta,j))
                sub_fascia = [list(row) for row in sub_fascia]
                for fascia in sub_fascia:        
                    for k in range(1,len(scopo_list)+1):
                        sub_scopo = set(itertools.combinations(scopo_list,k))
                        sub_scopo = [list(row) for row in sub_scopo]
                        for scopo in sub_scopo:
                            l = l+1
                            print (sex,fascia,scopo)
                            dg = df.copy()
                            dg = dg.loc[df['SESSO'].isin(sex)]
                            dg = dg.loc[df['FASCIA_ETA'].isin(fascia)]
                            dg = dg.loc[df['SCOPO'].isin(scopo)]
                            pvt = pd.pivot_table(dg,index=["COD_ZONA_PAR","COD_ZONA_ARR"],values=["COUNT"],aggfunc=np.sum)
                            #print (pvt)
                            
    end = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    print (start,end,l)

                        
                    
                
    
    
    
    