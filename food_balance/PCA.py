import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import pandas as pd
import numpy as np
import sklearn
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.cm as cm
import matplotlib.pylab as pl
import plotly.plotly as py
from plot_functions import *
from sklearn import preprocessing

n_years = 25 # 1986 - 2013

def global_PCA(X):
    # Global PCA
    std_scale = preprocessing.StandardScaler().fit(X)
    X_std = std_scale.transform(X)
    pca = PCA(n_components=1).fit(X_std)
    components = pca.transform(X_std)


    pca_score = pca.explained_variance_ratio_
    eigenvalues = pca.explained_variance_ # w
    covariance = pca.get_covariance()
    V = pca.components_
    print(" PCA score, how much each PCA contain " , pca_score)
    print(" PCA eigen values " , eigenvalues)
    print(" PCA eigen vector " , V)
    print(" PCA covariance \n ", covariance)
    print(" PCA", components)
    return components

def local_PCA():

    last_country = X_label[0]
    row_start = 0;
    row_end = 0;
    components = "empty"
    for i in range(len(X_label)):
        country = X_label[i]
        if country != last_country or i == len(X_label) -1 :
            row_end = i
            if(i == len(X_label) -1):
                row_end = i+1

            print(X_label[row_start:row_end])
            x_country = X[row_start:row_end]
            std_scale = preprocessing.StandardScaler().fit(x_country)
            X_std = std_scale.transform(x_country)
            pca = PCA(n_components=1).fit(X_std)
            component = pca.transform(X_std)
            print("len component", len(component))
            print("len country", len(x_country))
            print(" PCA eigen values " , eigenvalues)

            pca_score = pca.explained_variance_ratio_
            eigenvalues = pca.explained_variance_ # w
            covariance = pca.get_covariance()
            V = pca.components_
            print(" PCA score, how much each PCA contain " , pca_score)
            print(" PCA covariance \n", covariance)
            print(component, year_array[row_start:row_end])
            if(components == "empty"):
                components = component
            else:
                print(component)
                print(components)
                components = np.append(components,component)
                print(components)

            row_start = row_end;
            last_country = country;

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

def get_country_region_from_file(file_name, country_col, region_col):
    try:
        f = open(file_name,'r')
    except IOError:
        print("could not open file")
    reader = csv.reader(f, delimiter=",")
    data = {}
    region_list  ={}
    for row in reader:
        country = row[country_col]
        region = row[region_col]
        data[country] = region
        if region not in region_list:
            region_list[region] = [country]
        else:
            region_list[region].append(country)
    f.close()
    return data, region_list

def get_X_y_from_file(file_name, x1_col, x2_col, x3_col, country_col,year_col):
    try:
        f = open(file_name,'r')
    except IOError:
        print("could not open file")
    reader = csv.reader(f, delimiter=",")
    X = []
    y = []
    year = []
    for row in reader:
        print(row)
        print(row[0])
        if( row[x1_col] == 'ZV3' or row[x1_col] == 'V3' ):
            continue
        X.append([float(row[x1_col]), float(row[x2_col]), float(row[x3_col])])
        y.append(row[country_col])
        year.append(int(row[year_col]))
    f.close()
    return X,y,year

def get_X_y_from_file_2(file_name, x1_col, x2_col, x3_col,x4_col, country_col,year_col):
    try:
        f = open(file_name,'r')
    except IOError:
        print("could not open file")
    reader = csv.reader(f, delimiter="\t")
    X = []
    y = []
    year = []
    for row in reader:
        if( row[x1_col] == 'ZV3' or row[x1_col] == 'V3' ):
            continue
        X.append([float(row[x1_col].replace(',','.')),float(row[x2_col].replace(',','.')),float(row[x3_col].replace(',','.')),float(row[x4_col].replace(',','.'))])
        y.append(row[country_col])
        year.append(int(row[year_col]))
    f.close()
    return X,y,year


def make_X_file(new_file_name):
    file_name = "data/total_CO2_v2.csv"
    CO2 = get_data_from_file(file_name, 0, 26)

    file_name = "data/kcal_food_data_2.csv"
    kcal = get_data_from_file(file_name, 0, 28)

    file_name = "data/locality_index.csv"
    lindex = get_data_from_file(file_name, 0, 1)

    X = []
    country_row = {}
    target_names = []
    X_label = []
    num = 0
    for country  in CO2:
        if country not in lindex:
            continue
        if country not in kcal:
            continue
        if country == "Bahamas":
            continue
        for i in range(n_years):
            X.append([country,i+1986,CO2[country][i],kcal[country][i],lindex[country][i]])
            X_label.append(country)
        target_names.append(country)
        country_row[country] = num
        num += 1

    write_CO2_to_file(X, new_file_name)



file_name = "data/country_region.csv"
country_region, region_list = get_country_region_from_file(file_name, 0, 1)

file_name = "data/FINAL_DATA.csv"
#X,X_label,year_array = get_X_y_from_file(file_name,2,8,9,0,1 )
#X,X_label,year_array = get_X_y_from_file(file_name,2,3,5,0,1 )
X,X_label,year_array = get_X_y_from_file_2(file_name, 2, 3, 5,6, 0,1)

target_names = []
last_country = ""
for country in X_label:
    if country != last_country:
        target_names.append(country)
        last_country = country

country_plot_order = []
for region in region_list:
    for country in region_list[region]:
        country_plot_order.append(country)



pca_dic = {}
z1_dic = {}
z2_dic = {}
z3_dic = {}
for i in range(len(X_label)):
    country = X_label[i]
    if country not in pca_dic:
        pca_dic[country] = [None] * n_years
        z1_dic[country] = [None] * n_years
        z2_dic[country] = [None] * n_years
        z3_dic[country] = [None] * n_years
    year = year_array[i]
    z1_dic[country][year - 1986] = X[i][0]
    z2_dic[country][year - 1986] = X[i][1]
    z3_dic[country][year - 1986] = X[i][2]/1000.0
    pca_dic[country][year - 1986] = X[i][3]


year_0 = 1986
fis_label = "FIS"
CO2_label = "utslippsindeks"
kcal_label = "energiindeks"
env_label = "klimaindeks"

years = list(range(25))
file_name = "image/variation_env_fac_country.png"
plot_varity_country(pca_dic, env_label,target_names, file_name,years)
file_name = "image/variation_CO2_country.png"
plot_varity_country(z1_dic,CO2_label,target_names, file_name,years)
file_name = "image/variation_KCAL_country.png"
plot_varity_country(z2_dic, kcal_label,target_names, file_name,years)
file_name = "image/variation_lindex_country.png"
plot_varity_country(z3_dic, fis_label,target_names, file_name,years)


file_name = "image/global_trend_env_fac_error_bar.eps"
plot_global_error_bar(pca_dic,file_name,env_label,0,year_0)
file_name = "image/global_trend_CO2_error_bar.eps"
plot_global_error_bar(z1_dic,file_name,CO2_label,0,year_0)
file_name = "image/global_trend_KCAL_error_bar.eps"
plot_global_error_bar(z2_dic,file_name,kcal_label,0,year_0)
file_name = "image/global_trend_lindex_error_bar.eps"
plot_global_error_bar(z3_dic,file_name,fis_label,1,year_0)



country_array = ["Norway","Sweden","Argentina","Zimbabwe"]
file_name = "image/selected_env_fac.png"
plot_country_development(pca_dic,country_array,file_name,env_label,1,year_0)
file_name = "image/selected_lindex_fac.png"
plot_country_development(z3_dic,country_array,file_name,fis_label,1,year_0)




file_name = "image/global_trend_env_fac.png"
plot_global_development(pca_dic,file_name,env_label,year_0)
file_name = "image/global_trend_CO2.png"
plot_global_development(z1_dic,file_name,CO2_label,year_0)
file_name = "image/global_trend_KCAL.png"
plot_global_development(z2_dic,file_name,kcal_label,year_0)
file_name = "image/global_trend_lindex.png"
plot_global_development(z3_dic,file_name,fis_label,year_0)
