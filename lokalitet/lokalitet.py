import numpy as np
import csv
import pandas as pd
import math
import pycountry


def avstand(land1,land2):
    #my_data = np.genfromtxt('capdist.csv', delimiter=',')
    df=pd.read_csv('capdist.csv', sep=',',header=None)
    df = df.values
    #avstand = 0
    for i in range(len(df)):
        if(df[i][1]==land1 and df[i][3]==land2):
            return df[i][4]
            
    return 0
   
    
#avstand = avstand('NOR','USA')


def TM_vare_import_og_eksport(df,land1,land2,item):
    
    
    import_Tonn_Array = np.array([])
    eksport_Tonn_Array = np.array([])
    for i in range(len(df)):
        if(df[i][1]==land1 and df[i][3]==land2 and df[i][5]==item and df[i][7]=='Import Quantity'):
            for k in range(1,56,2):
                import_Tonn_Array = np.append(import_Tonn_Array,df[i][-(k+1)])
        
    for i in range(len(df)):
        if(df[i][1]==land1 and df[i][3]==land2 and df[i][5]==item and df[i][7]=='Export Quantity'):
            for k in range(1,56,2):
                eksport_Tonn_Array = np.append(eksport_Tonn_Array,df[i][-(k+1)])
            #eksport_Tonn_Array = df[i][-2]
    for i in range(len(import_Tonn_Array)):
        if math.isnan(import_Tonn_Array[i]):
            import_Tonn_Array[i]=0
        if math.isnan(eksport_Tonn_Array[i]):
            eksport_Tonn_Array[i]=0
    eksport_Tonn_Array = np.flip(eksport_Tonn_Array,0)
    import_Tonn_Array = np.flip(import_Tonn_Array,0)
    return import_Tonn_Array,eksport_Tonn_Array


TM=pd.read_csv('TM.csv', sep=',',header=None,encoding='latin-1')
TM = TM.values

import_tonn,eksport_tonn = TM_vare_import_og_eksport(TM,'Canada','Republic of Korea','Cereals, breakfast') 






