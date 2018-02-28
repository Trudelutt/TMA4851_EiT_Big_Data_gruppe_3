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

def alpha3ToCountryName(alpha):
	try:
		country = pycountry.countries.get(alpha_3=alpha)
	except KeyError:
		print("Could not recognise code - default value returned")
		country = pycountry.countries.get(alpha_3="ATA")
	countryName = country.name
	return countryName

def countryNameToAlpha3(cName):
	try:
		country = pycountry.countries.get(name=cName)
	except KeyError:
		print("Could not recognise code - default value returned")
		country = pycountry.countries.get(name="Antarctica")
	alpha = country.alpha_3
	return alpha

#print(alpha3ToCountryName("NOR"))
#print(countryNameToAlpha3("Norway"))


def TM_vare_import_og_eksport(land1,land2,item):
    df=pd.read_csv('TM.csv', sep=',',header=None,encoding='latin-1')
    df = df.values

    
    import_Tonn_Array = np.array([])
    eksport_Tonn_Array = np.array([])
    for i in range(len(df)):
        if(df[i][1]==land1 and df[i][3]==land2 and df[i][5]==item and df[i][7]=='Import Quantity'):
            for k in range(1,56,2):
                import_Tonn_Array = np.append(import_Tonn_Array,df[i][-(k+1)])
        if(df[i][1]==land1 and df[i][3]==land2 and df[i][5]==item and df[i][7]=='Export Quantity'):
            for k in range(1,56,2):
                eksport_Tonn_Array = np.append(eksport_Tonn_Array,df[i][-(k+1)])
    if(not import_Tonn_Array.any):
       import_Tonn_Array = np.zeros(28)
       
       print('error, making zero vector')
  
    if(not eksport_Tonn_Array.any):  
        eksport_Tonn_Array = np.zeros(28)
        print('error, making zero vector')
    maxLen = np.max(len(import_Tonn_Array),len(eksport_Tonn_Array))
    for i in range(maxLen):
        if math.isnan(import_Tonn_Array[i]):
            import_Tonn_Array[i]=0
        if math.isnan(eksport_Tonn_Array[i]):
            eksport_Tonn_Array[i]=0
    eksport_Tonn_Array = np.flip(eksport_Tonn_Array,0)
    import_Tonn_Array = np.flip(import_Tonn_Array,0)
    return df,import_Tonn_Array,eksport_Tonn_Array

print('test')

df,import_tonn,eksport_tonn = TM_vare_import_og_eksport('Spain','Norway','Avocados') 






