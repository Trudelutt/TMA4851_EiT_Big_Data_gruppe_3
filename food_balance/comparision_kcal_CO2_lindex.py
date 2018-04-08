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
import plotly

n_years = 25 # 1986 - 2013

def histogram_spread_in_y(data, year_array,file_name):
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
    ax.set_xlabel('miljøfaktor')
    ax.set_ylabel('andel land i verden')
    ax.grid(True)
    plt.title("Histogram av miljøfaktor")
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


def plot_country_development(pca_dic,country_array,file_name):

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
    plt.title("Development pca component")
    ax.set_xlabel('year')
    ax.set_ylabel('environment index')
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

file_name = "data/environment_factor_cleaned.csv"
X,X_label,year_array = get_X_y_from_file(file_name,7,8,9,0,1 )

target_names = {}
for country in X_label:
    if country not in target_names:
        target_names[country] = 0
        if(country =="Chad"):
            print("Chad")
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

comp_array = np.array(components)
print(components)
print(np.average(comp_array))

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

#plot_global_development(pca_dic)
country_array = ["Chad","Norway","Sweden","Afghanistan","Senegal","Zimbabwe"]
file_name = "image/total_env_fac.png"
image = plot_country_development(pca_dic,target_names,file_name)

year = [0,5,10,15,14,24]
file_name = "image/histogram_env_fac.png"
histogram_spread_in_y(pca_dic, year,file_name)

file_name = "image/global_trend_env_fac.png"
plot_global_development(pca_dic,file_name,"Global utvikling av miljøindeks")

file_name = "image/global_trend_CO2.png"
plot_global_development(z1_dic,file_name,"Global utviklinga av 'total CO2'")
file_name = "image/global_trend_KCAL.png"
plot_global_development(z2_dic,file_name,"Global utvikling av KCAL per capita per day")
file_name = "image/global_trend_lindex.png"
plot_global_development(z3_dic,file_name,"Global utvikling av lokalitetsindeks")
plt.show()
