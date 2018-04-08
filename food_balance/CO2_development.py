import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
from sklearn import datasets, linear_model
from sklearn.cluster import KMeans


country_col = 0
year_0_col = 1
n_years = 50


# get data from file, and devide into 3 arrays. One with name, one with type of food and one with each column being a countries spesific food types protein quantity per captia per year
def get_CO2_from_file(file_name):
    try:
        f = open(file_name,'r')
    except IOError:
        print("could not open file")
    reader = csv.reader(f, delimiter=",")
    data = {}
    last_country = " "
    for row in reader:
        quantity = [float(row[column]) for column in range(year_0_col,len(row) - year_0_col)]
        country = row[country_col]
        data[country] = quantity
    f.close()
    return data

def development_trend_plot(data):
    fig, ax = plt.subplots()
    for country in data:
        x = []
        y = []
        #y_coef = []
        for i in range(0,len(data[country])):
            y.append(data[country][i])
            x.append( 1961 +i)
            #y_coef.append(coef[0] + coef[1]*i)
        ax.plot(x, y,label = country)
    #ax.plot(x, y_coef,label = country)
    ax.set_xlabel('year')
    ax.set_ylabel('total CO2 per capita per day')
    ax.grid(True)
    ax.legend()
    plt.title("Total CO2")
    plt.show()

def histogram_spread_in_y(data, year_array):
    fig, ax = plt.subplots()
    y_data = []
    label_data = []
    for year in year_array:
        y_year = []
        for country in data:
            y = data[country][year]
            y_year.append(y)
        y_data.append(y_year)
        label_data.append(year)
    bins = [0,1000,2000,3000,4000,5000,6000,7000]
    plt.hist(y_data,bins = bins, label = label_data)
    plt.legend(loc='upper right')
    ax.set_xlabel('year')
    ax.set_ylabel('total CO2 per capita per day')
    ax.grid(True)
    plt.title("Total CO2")
    plt.show()

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



file_name = "data/total_CO2.csv"
CO2_countries = get_CO2_from_file(file_name)

#test_country_array = ["Norway"]
test_country_array = ["Chad","Norway","Sweden","Afghanistan","Senegal","Zimbabwe"]

data_dic = {}
for country in CO2_countries:
    data_dic[country] = CO2_countries[country]


development_trend_plot(data_dic)

year = list(range(40))
year = [0,10,20,30,40]
histogram_spread_in_y(data_dic,year)
