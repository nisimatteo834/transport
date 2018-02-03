# -*- coding: utf-8 -*-
from __future__ import print_function

"""
Created on Fri Feb  2 12:39:14 2018

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

if __name__ == '__main__':
    folder = 'C:\\Users\\Matteo\\Desktop\\lab1es2\\transport\\lab2'
    #folder = '.'
    #dc = pd.read_csv(folder+'/spostamenti.csv',keep_default_na=False)
    dc = pd.read_excel(folder+'/spostamenti.xlsx')
    dc = dc.rename(columns =({'PROV_PAR':'COUNT'}))
    
    towrite = folder+'\\allincsv\\results2.csv'
    file = open(towrite, 'w+')
    file.write('SESSO,FASCIA,SCOPO,ENOJY,CAR2GO,TOTAL\n')


    for fld in ['alldays','weekends','weekdays','afternoon','morning']:
    
        enjoy = pd.read_excel(folder+'/'+fld+'/carsharing_'+fld+'.xlsx','Sheet3')
        car2go = pd.read_excel(folder+'/'+fld+'/carsharing_'+fld+'.xlsx','Sheet4')
        total = pd.read_excel(folder+'/'+fld+'/carsharing_'+fld+'.xlsx','Sheet5')
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
        sum_enjoy=1.0
        sum_car2go=1.0
        sum_total=1.0
    
        start = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        #print ('Starting at',start)
        
        for i  in range(1,2):#len(sesso)+1):
            df = dc.copy()
            sub_sex = set(itertools.combinations(sesso,i))        
            sub_sex = [list(row) for row in sub_sex]    
            for sex in sub_sex:
                for j in range(1,2):#len(fascia_eta)+1):
                    sub_fascia = set(itertools.combinations(fascia_eta,j))
                    sub_fascia = [list(row) for row in sub_fascia]
                    for fascia in sub_fascia:        
                        for k in range(1,2):#len(scopo_list)+1):
                            sub_scopo = set(itertools.combinations(scopo_list,k))
                            sub_scopo = [list(row) for row in sub_scopo]
                            for scopo in sub_scopo:
                                dg = df.copy()
                                dg = dg.loc[df['SESSO'].isin(sex)]
                                dg = dg.loc[df['FASCIA_ETA'].isin(fascia)]
                                dg = dg.loc[df['SCOPO'].isin(scopo)]
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
                                    file.write(str(fld)+','+str(sex)+','+str(fascia)+','+str(scopo)+','+str(distance_enjoy.sum())+','+str(distance_car2go.sum())+','+str(distance_total.sum())+'\n')
                                    print(str(fld)+','+str(sex)+','+str(fascia)+','+str(scopo)+','+str(distance_enjoy.sum())+','+str(distance_car2go.sum())+','+str(distance_total.sum())+'\n')
          
    
                                # else:
                                #     print ('NO')
                                #     print (sex,fascia,scopo)
                                #     print (size)

                                
    #%%                        


                        
                    
                
    
    
    
    