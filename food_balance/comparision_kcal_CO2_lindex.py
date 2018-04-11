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

import plotly.plotly as py
n_years = 25 # 1986 - 2013

def sankey_diagram(data_dic):
    data = dict(
        type='sankey',
        node = dict(
          pad = 15,
          thickness = 20,
          line = dict(
            color = "black",
            width = 0.5
          ),
          label = ["A1", "A2", "B1", "B2", "C1", "C2"],
          color = ["blue", "blue", "blue", "blue", "blue", "blue"]
        ),
        link = dict(
          source = [0,1,0,2,3,3],
          target = [2,3,3,4,4,5],
          value = [8,4,2,8,4,2]
      )
    )

    layout =  dict(
        title = "Basic Sankey Diagram",
        font = dict(
          size = 10
        )
    )

    fig = dict(data=[data], layout=layout)
    py.image.save_as(fig, filename='a-simple-plot.png')


def histogram_spread_in_y(data_dic, year_array,file_name,label):
    bins = get_bins(data_dic,10)
    fig, ax = plt.subplots()
    y_data = []
    label_data = []
    edge_array =[]
    resul_array = []
    color = ["blue","red","purple", "darkorange", "green", "brown"]
    i = 0
    for year in year_array:
        y_year = []
        for country in data_dic:
            if(data_dic[country][year] is not None):
                y = data_dic[country][year]
                y_year.append(y)
        y_data.append(y_year)
        label_data.append(year+1986)

        results, edges = np.histogram(y_year,bins = bins, normed=True)
        binWidth = edges[1] - edges[0]
        plt.bar(edges[:-1], results*binWidth, binWidth,label=year+1986,edgecolor=color[i],color='None')
        i = i+1
    #plt.hist(y_data, label = label_data,density = True)
    plt.legend(loc='upper right')
    ax.set_ylabel('andel land i verden')
    plt.title(label)
    if(file_name):
        plt.savefig(file_name)

def get_bins(data_dic,n_bins):
    data = get_mean_data_per_year(data_dic)
    y_min  = 1000000000000000000000000000000
    y_max = -1*y_min
    for country in data_dic:
        for i in range(len(data_dic[country])):
            y = data_dic[country][i]
            if y is not None:
                if(y_min > y):
                    y_min  =y
                if(y_max < y):
                    y_max = y
    width = (y_max-y_min)/(n_bins)
    bins = np.arange(y_min, y_max + width*2,width)

    return bins
def plot_PCA(target_names,X_label,X):
    plt.figure()

    n = 0
    for name in target_names:
        x = []
        y = []
        for i in range(len(X_label)):
            if(X_label[i] == name):
                x.append(X[i,0])
                y.append(X[i,0])

        plt.plot(x, y, 'o', label=name)
        n+=1

    plt.legend(loc='best', shadow=False, scatterpoints=1)
    plt.title('PCA of IRIS dataset')
    plt.show()

def plot_global_development(data_dic,file_name,label):
    data = get_mean_data_per_year(data_dic)
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

def plot_varity_country(data_dic, label,all_countries, file_name,years):
    plt.figure(figsize=(15, 10), dpi=100)
    plt.grid()
    y = np.zeros(len(all_countries))
    for year in years:
        x = []
        y  = []
        for i in range(len(all_countries)):
            country = all_countries[i]
            x.append(i)
            y.append(data_dic[country][year])
        plt.scatter(x,y)
    x =[i for i in range(len(all_countries))]
    plt.xticks(x, all_countries,rotation='vertical')
    plt.title(label)
    if(file_name):
        plt.savefig(file_name,dpi = 100)
    else:
        plt.show()


def plot_country_development(data_dic,country_array,file_name,label,label_on):

    fig, ax = plt.subplots()
    for country in country_array:
        x = []
        y = []
        data = data_dic[country]
        for i in range(len(data)):
            if( data[i] == None):
                continue
            y.append(data[i])
            x.append(i + 1986)
        plt.plot(x, y,label = country)
    if(label_on):
        plt.legend(loc='best', shadow=False, scatterpoints=1)
    plt.title(label)
    ax.set_xlabel("År")
    if(file_name):
        plt.savefig(file_name)
    else:
        plt.show()

def get_mean_data_per_year(data_dic):
    n_country_per_year = np.zeros(25)
    avg = np.zeros(25)
    for country in pca_dic :
        for i in range(len(data_dic[country])):
            if(data_dic[country][i] is  None ):
                continue
            else:
                avg[i] += data_dic[country][i]
                n_country_per_year[i] += 1

    for i in range(avg.shape[0]):
        avg[i] = avg[i]/ n_country_per_year[i]

    return avg

def get_max_min_per_year(data_dic):
    ma = np.ones(25)*(-10000000000)
    mi = np.ones(25)*100000000000
    for country in data_dic :
        for i in range(len(data_dic[country])):
            if(data_dic[country][i] is  None ):
                continue
            else:
                if( ma[i] < data_dic[country][i]):
                     ma[i] = data_dic[country][i]
                if( mi[i] > data_dic[country][i]):
                     mi[i] = data_dic[country][i]
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

def plot_global_error_bar(data_dic,file_name,label,locality_index):
    fig, ax = plt.subplots()
    all_points_x = []
    all_points_y = []
    for country in data_dic:
        for i in range(len(data_dic[country])):
            if(data_dic[country][i] is  None ):
                continue
            all_points_x.append(i+1961)
            all_points_y.append(data_dic[country][i])

    data = get_mean_data_per_year(data_dic)
    ma, mi = get_max_min_per_year(data_dic)
    y_err = np.zeros((2,len(ma)))
    for i in range(len(ma)):
        y_err[0,i] = data[i] - mi[i]
        y_err[1,i] = ma[i] - data[i]
    x = []
    y = []
    for i in range(len(data)):
        y.append(data[i])
        x.append(i + 1961)
    plt.scatter(all_points_x, all_points_y, s = 5)
    ax.errorbar(x, y, yerr=y_err, fmt='o',c = "red")
    #ax.errorbar(x, y,yerr = y_err)
    plt.title(label)
    ax.set_xlabel('År')
    if(file_name):
        plt.savefig(file_name)



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
    print(year)
    pca_dic[country][year - 1986] = components[i][0]
    z1_dic[country][year - 1986] = X[i][0]
    z2_dic[country][year - 1986] = X[i][1]
    z3_dic[country][year - 1986] = X[i][2]

'''
file_name = "image/global_trend_env_fac_error_bar.png"
plot_global_error_bar(pca_dic,file_name,"Global utvikling av miljøindeks",0)
file_name = "image/global_trend_CO2_error_bar.png"
plot_global_error_bar(z1_dic,file_name,"Global utvikling av 'total CO2'",0)
file_name = "image/global_trend_KCAL_error_bar.png"
plot_global_error_bar(z2_dic,file_name,"Global utvikling av KCAL per capita per dag",0)
file_name = "image/global_trend_lindex_error_bar.png"
plot_global_error_bar(z3_dic,file_name,"Global utvikling av lokalitetsindeks",1)


file_name = "image/selected_env_fac.png"
country_array = ["Norway","Sweden","Chile","Zimbabwe"]
plot_country_development(pca_dic,country_array,file_name,"Utvikling av miljøfaktoren for utvalgte land",1)

file_name = "image/all_env_fac.png"
plot_country_development(pca_dic,target_names,file_name,"Utvikling av miljøfaktoren for alle land",0)
file_name = "image/all_CO2.png"
plot_country_development(z1_dic,target_names,file_name,"Utvikling av 'total CO2' for alle land",0)
file_name = "image/all_kcal.png"
plot_country_development(z2_dic,target_names,file_name,"Utvikling av total KCAL per inbygger per dag for alle land",0)
file_name = "image/all_lindex.png"
plot_country_development(z3_dic,target_names,file_name,"Utvikling av lokalitetsindeks for alle land",0)
'''
'''
years = list(range(25))
file_name = "image/variation_env_fac_country.png"
plot_varity_country(pca_dic, "Variasjon i miljøfaktor for hvert land",target_names, file_name,years)
file_name = "image/variation_CO2_country.png"
plot_varity_country(z1_dic, "Variasjon i 'total CO2' for hvert land ",target_names, file_name,years)
file_name = "image/variation_KCAL_country.png"
plot_varity_country(z2_dic, "Variasjon i 'KCAL ' for hvert land ",target_names, file_name,years)
file_name = "image/variation_lindex_country.png"
plot_varity_country(z3_dic, "Variasjon i lokalitetsindeks for hvert land ",target_names, file_name,years)
'''
'''
year = [0,24]
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


plt.show()
