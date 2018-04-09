import numpy as np
import csv
import pandas as pd
import math
import pycountry
from scipy.stats import norm
import time

start = time.time()

avs=pd.read_csv('capdist.csv', sep=',',header=None)
avs = avs.values
df=pd.read_csv('TMtest.txt', sep=',',header=None,encoding='latin-1')
df = df.values

def avstand(land1,land2,avs):
    for i in range(len(avs)):
        if(avs[i][1]==land1 and avs[i][3]==land2):
            return avs[i][4]
            
    return 0
   
    

def alpha3ToCountryName(alpha):
	try:
		country = pycountry.countries.get(alpha3=alpha)
	except KeyError:
		#print("Could not recognise code - default value returned")
		country = pycountry.countries.get(alpha3="ATA")
	countryName = country.name
	return countryName

def countryNameToAlpha3(cName):
	try:
		country = pycountry.countries.get(name=cName)
	except KeyError:
		#print("Could not recognise code - default value returned")
		country = pycountry.countries.get(name="Antarctica")
	alpha = country.alpha3
	return alpha


def TM_vare_import_og_eksport(land1,land2,item,df):
    
    import_Tonn_Array = np.array([])
    eksport_Tonn_Array = np.array([])
    for i in range(len(df)):
        if df[i][1]==land1 and df[i][3]==land2 and df[i][5]==item and df[i][7]=='Import Quantity':
            for k in range(1,56,2):
                import_Tonn_Array = np.append(import_Tonn_Array,df[i][-(k+1)])
        
        if df[i][1]==land1 and df[i][3]==land2 and df[i][5]==item and df[i][7]=='Export Quantity':
            for k in range(1,56,2):
                eksport_Tonn_Array = np.append(eksport_Tonn_Array,df[i][-(k+1)])
            #if df[i+1][1]!=land1:
                #break
    if len(import_Tonn_Array)==0:
       import_Tonn_Array = np.zeros(28)
       
       print('error, making import zero vector')
  
    if len(eksport_Tonn_Array)==0:  
        eksport_Tonn_Array = np.zeros(28)
        print('error, making export zero vector')
        
    maxLen=28
    for i in range(maxLen):
        if math.isnan(import_Tonn_Array[i]):
            import_Tonn_Array[i]=0
        if math.isnan(eksport_Tonn_Array[i]):
            eksport_Tonn_Array[i]=0
    eksport_Tonn_Array = np.flip(eksport_Tonn_Array,0)
    import_Tonn_Array = np.flip(import_Tonn_Array,0)
    return import_Tonn_Array,eksport_Tonn_Array


def indeksAllYears(country,df):
    indeksForCountry = np.zeros(28)
    
    #eksport_Tonn_Array=np.array([])
    for i in range(len(df)-1): 
        import_Tonn_Array=np.array([])
        if df[i][1]==country:
          country2 = countryNameToAlpha3(df[i][3])
          if(df[i][7]=='Import Quantity'):
              for k in range(1,56,2):
                import_Tonn_Array = np.append(import_Tonn_Array,df[i][-(k+1)])
          if len(import_Tonn_Array)==0:
              import_Tonn_Array = np.zeros(28)
          if df[i+1][1]!=country:
              break
  
          maxLen=28
          for i in range(maxLen):
            if math.isnan(import_Tonn_Array[i]):
                import_Tonn_Array[i]=0
          import_Tonn_Array = np.flip(import_Tonn_Array,0)
          
          
          importNumbersYear = import_Tonn_Array
          
          indeksForCountry = [sum(x) for x in zip(indeksForCountry, importNumbersYear*punish(country,country2))] 
                    

    return indeksForCountry


def indeksOneYear(country,year,df):
    indeksForCountry = 0
    
    #eksport_Tonn_Array=np.array([])
    for i in range(len(df)-1): 
        import_Tonn_Array=np.array([])
        if df[i][1]==country:
          country2 = countryNameToAlpha3(df[i][3])
          item     = df[i][5]
          if(df[i][7]=='Import Quantity'):
              for k in range(1,56,2):
                import_Tonn_Array = np.append(import_Tonn_Array,df[i][-(k+1)])
          #if(df[i][7]=='Export Quantity'):
               # eksport_Tonn_Array = np.append(eksport_Tonn_Array,df[i][-(k+1)])
         
          if len(import_Tonn_Array)==0:
              import_Tonn_Array = np.zeros(28)
              #print('error, making import zero vector')
          if df[i+1][1]!=country:
              break
  
       # if len(eksport_Tonn_Array)==0:  
          #  eksport_Tonn_Array = np.zeros(28)
           # print('error, making export zero vector')
         
            
           
          maxLen=28
          for i in range(maxLen):
            if math.isnan(import_Tonn_Array[i]):
                import_Tonn_Array[i]=0
          import_Tonn_Array = np.flip(import_Tonn_Array,0)
          importNumbersYear = import_Tonn_Array[year]
          indeksForCountry += importNumbersYear*punish(country,country2)
                    

    return indeksForCountry


def punish(country1,country2):
    distance = int(avstand(country1,country2,avs))
    punishmentFactor = norm.cdf(distance,7000,5000)
    return punishmentFactor




start = time.time()
#import_tonn,eksport_tonn = TM_vare_import_og_eksport('Spain','Norway','Avocados',df) 
test = indeksAllYears('Norway',df)
end = time.time()
print(end-start)
