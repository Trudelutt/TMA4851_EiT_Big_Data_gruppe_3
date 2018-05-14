import csv
import numpy as np
import matplotlib.pyplot as plt
from plot_functions import *

n_years = 53
# years: 1961-1971-1981-1991- 2001- 2011

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
        quantity = [float(row[column]) for column in range(year_0_col,len(row))]
        country = row[country_col]
        data[country] = quantity
    f.close()
    return data


# get data from file, and devide into 3 arrays. One with name, one with type of food and one with each column being a countries spesific food types protein quantity per captia per year


file_name = "data/kcal_food_data_2.csv"
data_dic = get_data_from_file(file_name, 0, 3)
label_name = "Energiindeks"

target_names  =[]
last_country  = ""
for country in data_dic:
    if(last_country!= country):
        target_names.append(country)
        last_country = country

country_array = ["Norway","Sweden","Argentina","Zimbabwe"]
year_0 = 1960
file_name = "image/kcal_selected_kcal_plot.eps"
plot_country_development(data_dic,country_array,file_name,label_name,1,year_0)

file_name = "image/kcal_error_bar.eps"
plot_global_error_bar(data_dic,file_name,label_name,0,year_0)

years = list(range(25))
file_name = "image/kcal_varr.png"
plot_varity_country(data_dic, label_name,target_names, file_name,years)
year = [0,5,10,15,14,24]

file_name = "image/kcal_global.eps"
plot_global_development(data_dic,file_name,label_name,year_0)

##histogram_spread_in_y(data_dic, year,None,"Histogram av kcal")
