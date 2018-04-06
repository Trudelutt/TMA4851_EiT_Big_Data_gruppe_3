import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
from sklearn import datasets, linear_model
from sklearn.cluster import KMeans


country_col = 0
food_t_col = 1
year_0_col = 3
n_years = 50
# years: 1961-1971-1981-1991- 2001- 2011

# get data from file, and devide into 3 arrays. One with name, one with type of food and one with each column being a countries spesific food types protein quantity per captia per year
def get_food_supply_quantity_from_file(file_name):
    try:
        f = open(file_name,'r')
    except IOError:
        print("could not open file")
    reader = csv.reader(f, delimiter=",")
    data = {}
    last_country = " "
    for row in reader:
        quantity = [float(row[column]) for column in range(year_0_col,len(row) - year_0_col)]
        item = row[food_t_col]
        country = row[country_col]
        if( country in data):
            data[country][item] = quantity;
            #print(country," type ",item, diet_countries[country][item])
        else:
            data[country] = {}
            data[country][item] = quantity;


    f.close()
    return data

def get_CO2_foodtypes_from_file(file_name):
    try:
        f = open(file_name,'r')
    except IOError:
        print("could not open file")
    reader = csv.reader(f, delimiter=",")
    data = {}
    last_country = " "
    for row in reader:
        if row[1] != "kg CO2/kg food type":
            quantity = float(row[1])
            item = row[2]
            data[item] = quantity
    f.close()
    return data

def get_total_CO2_country( CO2_food_type, food_quantity):
    total = [0 for x in range(0,n_years)]
    for item in food_quantity:
        if(item in CO2_food_type):
            for j in range(0,len(food_quantity[item])):
                total[j] += food_quantity[item][j]*CO2_food_type[item]
    return total


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
        y_country = []
        for country in data:
            y = data[country][year]
            y_country.append(y)
        y_data.append(y_country)
        label_data.append(year)
    plt.hist(y_data, label = label_data)
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



file_name = "data/food_supply_quantity.csv"
food_quantity_countries = get_food_supply_quantity_from_file(file_name)
file_name = "data/CO2_per_food_type.csv"
CO2_food_type =  get_CO2_foodtypes_from_file(file_name)
#test_country_array = ["Norway"]
test_country_array = ["Chad","Norway","Sweden","Afghanistan","Senegal","Zimbabwe"]
data_dic = {}
coef_dic = {}
'''years_array = []
for i in range(0,n_years):
    years_array.append([i])
years = np.array(years_array)'''

for country in food_quantity_countries:
    food_quantity = food_quantity_countries[country]
    data = get_total_CO2_country(CO2_food_type, food_quantity)
    data_dic[country] = data
    #coef = linear_regression(years, data)
    #coef_dic[country] = coef

development_trend_plot(data_dic)
#kmeans(coef_dic)
year = list(range(40))
histogram_spread_in_y(data_dic,year)
