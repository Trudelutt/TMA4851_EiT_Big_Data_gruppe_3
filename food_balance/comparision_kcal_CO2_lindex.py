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

import pylab

n_years = 25 # 1986 - 2013

def histogram_spread_in_y(data, year_array,file_name,label):
    fig, ax = plt.subplots()
    y_data = []
    label_data = []
    for year in year_array:
        y_year = []
        for country in data:
            if(data[country][year] is not None):
                y = data[country][year]
                y_year.append(y)
        y_data.append(y_year)
        label_data.append(year+1986)
    plt.hist(y_data, label = label_data,density = True)
    plt.legend(loc='upper right')
    ax.set_ylabel('andel land i verden')
    ax.grid(True)
    plt.title(label)
    if(file_name):
        plt.savefig(file_name)
    else:
        plt.show()

def plot_PCA(target_names,X_label,X):
    plt.figure()

    n = 0
    for name in target_names:
        x = []
        y = []
        for i in range(len(X_label)):
            if(X_label[i] == name):
                x.append(Y_sklearn[i,0])
                y.append(Y_sklearn[i,0])

        plt.plot(x, y, 'o', label=name)
        n+=1

    plt.legend(loc='best', shadow=False, scatterpoints=1)
    plt.title('PCA of IRIS dataset')
    plt.show()

def plot_global_development(pca_dic,file_name,label):
    data = get_global_PCA(pca_dic)
    x = []
    y = []
    fig, ax = plt.subplots()
    for i in range(len(data)):
        y.append(data[i])
        x.append(i + 1986)
    plt.plot(x, y)
    plt.title(label)
    ax.set_xlabel('År')
    ax.set_ylabel('Standardisert data')
    if(file_name):
        plt.savefig(file_name)
    else:
        plt.show()

def plot_varity_country(pca_dic, label,X_label, file_name,years):
    fig, ax = plt.subplots()
    plt.figure(figsize=(15, 10), dpi=100)
    plt.grid()
    for year in years:
        for i in range(len(X_label)):
            country = X_label[i]
            x = i
            y = pca_dic[country][year]
            plt.scatter(x,y)
    x =[i for i in range(len(X_label))]
    plt.xticks(x, X_label,rotation='vertical')
    plt.title(label)
    if(file_name):

        plt.savefig(file_name,dpi = 100)
    else:
        plt.show()


def plot_country_development(pca_dic,country_array,file_name,label):

    fig, ax = plt.subplots()
    for country in country_array:
        x = []
        y = []
        data = pca_dic[country]
        for i in range(len(data)):
            if( data[i] == None):
                continue
            y.append(data[i])
            x.append(i + 1986)
        plt.plot(x, y,label = country)
    #plt.legend(loc='best', shadow=False, scatterpoints=1)
    plt.title(label)
    ax.set_xlabel("År")
    if(file_name):
        plt.savefig(file_name)
    else:
        plt.show()

def get_global_PCA(pca_dic):
    n_country_per_year = np.zeros(25)
    avg = np.zeros(25)
    for country in pca_dic :
        for i in range(len(pca_dic[country])):
            if(pca_dic[country][i] is  None ):
                continue
            else:
                avg[i] += pca_dic[country][i]
                n_country_per_year[i] += 1

    for i in range(avg.shape[0]):
        avg[i] = avg[i]/ n_country_per_year[i]

    return avg

def get_max_min_per_year(pca_dic):
    ma = np.ones(25)*(-10000000000)
    mi = np.ones(25)*100000000000
    for country in pca_dic :
        for i in range(len(pca_dic[country])):
            if(pca_dic[country][i] is  None ):
                continue
            else:
                if( ma[i] < pca_dic[country][i]):
                     ma[i] = pca_dic[country][i]
                if( mi[i] > pca_dic[country][i]):
                     mi[i] = pca_dic[country][i]
    return ma, mi


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

def get_X_y_from_file(file_name, x1_col, x2_col, x3_col, country_col,year_col):
    try:
        f = open(file_name,'r')
    except IOError:
        print("could not open file")
    reader = csv.reader(f, delimiter=";")
    X = []
    y = []
    year = []
    for row in reader:
        if( row[x1_col] == 'ZV3'):
            continue
        X.append([float(row[x1_col]), float(row[x2_col]), float(row[x3_col])])
        y.append(row[country_col])
        year.append(int(row[year_col]))
    f.close()
    return X,y,year

def write_CO2_to_file(data, file_name):
    f = open(file_name, 'w')
    output = []
    for i in range(len(data)):
        output.append(data[i])
    with f:
        writer = csv.writer(f)
        writer.writerows(output)
    print("Writing complete")

def make_X_file():
    file_name = "data/total_CO2.csv"
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
            X.append([CO2[country][i],kcal[country][i],lindex[country][i]])
            X_label.append(country)
        target_names.append(country)
        country_row[country] = num
        num += 1

def plot_global_error_bar(pca_dic,file_name,label):
    data = get_global_PCA(pca_dic)
    ma, mi = get_max_min_per_year(pca_dic)
    y_err = np.zeros((2,len(ma)))
    for i in range(len(ma)):
        y_err[0,i] = -mi[i]
        y_err[1,i] = ma[i]
    x = []
    y = []
    for i in range(len(data)):
        y.append(data[i])
        x.append(i + 1986)
    fig, ax = plt.subplots()
    ax.errorbar(x, y, yerr=y_err, fmt='o')
    plt.title(label)
    ax.set_xlabel('År')
    ax.set_ylabel('Standardisert data')
    if(file_name):
        plt.savefig(file_name)
    else:
        plt.show()



file_name = "data/environment_factor_cleaned.csv"
X,X_label,year_array = get_X_y_from_file(file_name,7,8,9,0,1 )

target_names = []
last_country = ""
for country in X_label:
    if country != last_country:
        target_names.append(country)
        last_country = country
#standarize data#X = StandardScaler().fit_transform(X)

# PCA
pca = PCA(n_components=1)
components = pca.fit(X).transform(X)

pca_score = pca.explained_variance_ratio_
eigenvalues = pca.explained_variance_ # w
covariance = pca.get_covariance()
V = pca.components_


print(" PCA score, how much each PCA contain " , pca_score)
print(" PCA eigen values " , eigenvalues)
print(" PCA eigen vector " , V)
print(" PCA covariance ", covariance)
print(" PCA", components)

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
    pca_dic[country][year - 1986] = components[i][0]
    z1_dic[country][year - 1986] = X[i][0]
    z2_dic[country][year - 1986] = X[i][1]
    z3_dic[country][year - 1986] = X[i][2]



'''file_name = "image/global_trend_env_fac_error_bar.png"
plot_global_error_bar(pca_dic,file_name,"Global utvikling av miljøindeks")
file_name = "image/global_trend_CO2_error_bar.png"
plot_global_error_bar(z1_dic,file_name,"Global utvikling av 'total CO2'")
file_name = "image/global_trend_KCAL_error_bar.png"
plot_global_error_bar(z2_dic,file_name,"Global utvikling av KCAL per capita per dag")
file_name = "image/global_trend_lindex_error_bar.png"
plot_global_error_bar(z3_dic,file_name,"Global utvikling av lokalitetsindeks")'''

'''file_name = "image/all_env_fac.png"
plot_country_development(pca_dic,target_names,file_name,"Utvikling av miljøfaktoren for alle land")
file_name = "image/all_CO2.png"
plot_country_development(z1_dic,target_names,file_name,"Utvikling av 'total CO2' for alle land")
file_name = "image/all_kcal.png"
plot_country_development(z2_dic,target_names,file_name,"Utvikling av total KCAL per inbygger per dag for alle land")
file_name = "image/all_lindex.png"
plot_country_development(z3_dic,target_names,file_name,"Utvikling av lokalitetsindeks for alle land")
'''
'''
years = list(range(25))
file_name = "image/variation_env_fac_country.png"
plot_varity_country(pca_dic, "Variation i miljøfaktor for hvert land",target_names, file_name,years)
file_name = "image/variation_CO2_country.png"
plot_varity_country(z1_dic, "Variation in 'total CO2' for each country",target_names, file_name,years)
file_name = "image/variation_KCAL_country.png"
plot_varity_country(z2_dic, "Variation in 'KCAL per capita per day' for each country",target_names, file_name,years)
file_name = "image/variation_lindex_country.png"
plot_varity_country(z3_dic, "Variation in 'KCAL per capita per day' for each country",target_names, file_name,years)
'''

year = [0,5,10,15,14,24]
file_name = "image/histogram_env_fac.png"
histogram_spread_in_y(pca_dic, year,file_name,"Histogram av miljøfaktor")
file_name = "image/histogram_CO2.png"
histogram_spread_in_y(z1_dic, year,file_name,"Histogram av CO2")
file_name = "image/histogram_KCAL.png"
histogram_spread_in_y(z2_dic, year,file_name,"Histogram av KCAL")
file_name = "image/histogram_lindex.png"
histogram_spread_in_y(z3_dic, year,file_name,"Histogram av lokalitetsindeks")

'''
file_name = "image/global_trend_env_fac.png"
plot_global_development(pca_dic,file_name,"Global utvikling av miljøindeks")
file_name = "image/global_trend_CO2.png"
plot_global_development(z1_dic,file_name,"Global utviklinga av 'total CO2'")
file_name = "image/global_trend_KCAL.png"
plot_global_development(z2_dic,file_name,"Global utvikling av KCAL per capita per day")
file_name = "image/global_trend_lindex.png"
plot_global_development(z3_dic,file_name,"Global utvikling av lokalitetsindeks")
plt.show()'''
