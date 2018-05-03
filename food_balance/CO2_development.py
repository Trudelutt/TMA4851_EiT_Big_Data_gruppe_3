import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
from sklearn import datasets, linear_model
from sklearn.cluster import KMeans
from plot_functions import *

n_years = 47

def linear_regression(x, y):
    regr = linear_model.LinearRegression()
    coef_dic = {};
    regr.fit(x, y)
    intercept = regr.intercept_
    coef = regr.coef_[0]
    return [intercept, coef]

def kmeans(coef_dic):
    X = []
    country_label = []

    for country in coef_dic:
        X.append(coef_dic[country])
        country_label.append(country)
    X = np.array(X)
    kmeans = KMeans(n_clusters=5)
    kmeans.fit(X)
    y_kmeans = kmeans.predict(X)

    fig, ax = plt.subplots()
    colour_array = ['red', 'green', 'blue','yellow','pink','purple']
    for i in range(len(country_label)):
        x = X[i,0]
        y = X[i,1]
        ax.scatter(x, y,label = country_label[i],color=colour_array[y_kmeans[i]] , s = 40)
    #ax.plot(x, y_coef,label = country)
    ax.set_xlabel('intercept')
    ax.set_ylabel('coef')
    ax.grid(True)
    ax.legend()
    plt.title("Clustering based on linear regression")
    plt.show()


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
        quantity = [float(row[column]) for column in range(year_0_col,n_years)]
        country = row[country_col]
        data[country] = quantity
    f.close()
    return data

# get data from file, and devide into 3 arrays. One with name, one with type of food and one with each column being a countries spesific food types protein quantity per captia per year


file_name = "data/total_CO2.csv"
data_dic = get_data_from_file(file_name, 0, 1)



target_names  =[]
last_country  = ""
for country in data_dic:
    if(last_country!= country):
        target_names.append(country)
        last_country = country

country_array = ["Norway","Sweden","Argentina","Zimbabwe"]
year_0  = 1960
file_name = "image/CO_selected_countries.eps"
plot_country_development(data_dic,country_array,file_name,"total CO2-ekvivalent fra 66 matvarer per innbygger",1,year_0)

file_name = "image/CO2_error_bars.eps"
plot_global_error_bar(data_dic,file_name,"total CO2-ekvivalent fra 66 matvarer per innbygger",0,year_0)

file_name = "image/CO2_varr.png"
years = list(range(25))
plot_varity_country(data_dic, "total CO2-ekvivalent fra 66 matvarer per innbygger per år",target_names,file_name,years)
year = [0,5,10,15,14,24]

file_name = "image/CO2_global.eps"
plot_global_development(data_dic,file_name,"total CO2-ekvivalent fra 66 matvarer per innbygger",year_0)

#plt.show()
