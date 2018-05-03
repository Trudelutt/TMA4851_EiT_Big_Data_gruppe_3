import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
import matplotlib.cm as cm
from plot_functions import *

n_years = 25 # 1986 - 2013

# get data from file, and devide into 3 arrays. One with name, one with type of food and one with each column being a countries spesific food types protein quantity per captia per year
def get_data_from_file(file_name, country_col, year_0_col):
    try:
        f = open(file_name,'r')
    except IOError:
        print("could not open file")
    reader = csv.reader(f, delimiter=",")
    data = {}
    last_country = " "
    for row in reader:
        quantity = [float(row[column]) for column in range(year_0_col,year_0_col + n_years)]
        country = row[country_col]
        data[country] = quantity
    f.close()
    return data



file_name = "data/locality_index.csv"
data_dic = get_data_from_file(file_name, 0, 1)

target_names  =[]
last_country  = ""
for country in data_dic:
    if(last_country!= country):
        target_names.append(country)
        last_country = country

country_array = ["Norway","Sweden","Argentina","Zimbabwe"]
year_0 = 1986
file_name = "image/lindex_selected_countries.eps"
plot_country_development(data_dic,country_array,file_name,"lokalitetsindeks",1,year_0)

file_name = "image/lindex_error_bar.eps"
plot_global_error_bar(data_dic,file_name,"FIS-indeks",0,year_0)

years = list(range(25))
file_name = "image/lindex_varr.png"
plot_varity_country(data_dic, "FIS-indeks per år",target_names, file_name,years)

file_name = "image/lindex_global.eps"
plot_global_development(data_dic,file_name,"FIS-indeks",year_0)
#plt.show()

#year = [0,5,10,15,14,24]
#histogram_spread_in_y(data_dic, year,None,"Histogram av lokalitetsindeks")
