# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 18:39:15 2018

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

if __name__ == '__main__':
    folder = 'C:\\Users\\Matteo\\Desktop\\lab1es2\\transport'
    #folder = '.'
    #dc = pd.read_csv(folder+'/spostamenti.csv',keep_default_na=False)
    dc = pd.read_excel(folder+'/spostamenti.xlsx')
    dc = dc.rename(columns =({'PROV_PAR':'COUNT'}))
    
    #enjoy = pd.read_excel(folder+'/carsharing.xlsx','enjoy')
    #car2go = pd.read_excel(folder+'/carsharing.xlsx','car3go')
    #total = pd.read_excel(folder+'/carsharing.xlsx','Total')
    enjoy = pd.read_excel(folder+'/carsharing.xlsx','Sheet3')
    car2go = pd.read_excel(folder+'/carsharing.xlsx','Sheet4')
    total = pd.read_excel(folder+'/carsharing.xlsx','Sheet5')
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
    sesso = ["1","2"]    
    scopo_list = ["1","2","3","4","5","6","7","8","9","11","10"]
    #%%
    
    #df = dc.copy()
    #pvt = pd.pivot_table(df,index=["COD_ZONA_PAR","COD_ZONA_ARR"],values=["COUNT"],aggfunc=np.sum)

#%% 
    l = 0
    best_enjoy= []
    best_car2go= []
    best_total= []
    
    sum_enjoy=1.0
    sum_car2go=1.0
    sum_total=1.0

    start = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    print ('Starting at',start)
    print('SESSO_FASCIA_SCOPO,ENOJY,CAR2GO,TOTAL')
    for i  in range(1,2):#,len(sesso)+1):
        df = dc.copy()
        sub_sex = set(itertools.combinations(sesso,i))        
        sub_sex = [list(row) for row in sub_sex]    
        for sex in sub_sex:
            for j in range(1,2):#len(fascia_eta)+1):
                sub_fascia = set(itertools.combinations(fascia_eta,j))
                sub_fascia = [list(row) for row in sub_fascia]
                for fascia in sub_fascia:        
#                    for k in range(1,2):#len(scopo_list)+1):
#                        sub_scopo = set(itertools.combinations(scopo_list,k))
#                        sub_scopo = [list(row) for row in sub_scopo]
#                        for scopo in sub_scopo:
                    l = l+1
                    #print (sex,fascia,scopo)
                    dg = df.copy()
                    dg = dg.loc[df['SESSO'].isin(sex)]
                    dg = dg.loc[df['FASCIA_ETA'].isin(fascia)]
                    dg = dg.loc[df['SCOPO'].isin(scopo_list)]
                    pvt = pd.pivot_table(dg,index=["COD_ZONA_PAR","COD_ZONA_ARR"],values=["COUNT"],aggfunc=np.sum)
                    pvt = pvt.reindex(indexes)
                    pvt = pvt.unstack()
                    pvt = pvt.fillna(0)      
                                            
                    size=pvt.shape
                    
                    if(size==(23,23)):
                        norm_pvt = pvt/pvt.values.sum()
                        test4  = norm_pvt.values.sum()
                        distance_enjoy = np.abs(norm_enjoy.values - norm_pvt.values)
                        distance_car2go = np.abs(norm_car2go.values - norm_pvt.values)
                        distance_total = np.abs(norm_total.values - norm_pvt.values)
                        print (sex[0]+' '+fascia[0]+','+str(distance_enjoy.sum())+','+str(distance_car2go.sum())+','+str(distance_total.sum()))
                               

                        
                        if(distance_enjoy.sum() < sum_enjoy):
                            best_enjoy.clear()
                            sum_enjoy = distance_enjoy.sum()
                            best_enjoy.append(sex)
                            best_enjoy.append(fascia)
                            #best_enjoy.append(sub_scopo)
                        
                        if(distance_car2go.sum() < sum_car2go):
                            best_car2go.clear()
                            sum_car2go = distance_car2go.sum()
                            best_car2go.append(sex)
                            best_car2go.append(fascia)
                            #best_car2go.append(scopo)
                        
                        if(distance_total.sum() < sum_total):
                            best_total.clear()
                            sum_total = distance_total.sum()
                            best_total.append(sex)
                            best_total.append(fascia)
                            #best_total.append(scopo)
                            # else:
                            #     print ('NO')
                            #     print (sex,fascia,scopo)
                            #     print (size)

                                
    #%%                        
    end = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    print ('Best Total',best_total)
    print ('Best Car2Go',best_car2go)
    print ('Best Enjoy',best_enjoy)
    print (start,end,l)

                        
                    
                
    
    
    
    