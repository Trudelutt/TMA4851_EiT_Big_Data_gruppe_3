import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
import matplotlib.cm as cm

n_years = 25 # 1986 - 2013


def histogram_spread_in_y(data_dic, year_array,file_name,label):
    bins = get_bins(data_dic,10)
    print(bins)
    fig, ax = plt.subplots()
    y_data = []
    label_data = []
    edge_array =[]
    resul_array = []
    color = ["purple","red","blue", "darkorange", "green", "magenta", "maroon", "brown"]
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
        plt.bar(edges[:-1], results*binWidth, binWidth,label=year+19861,edgecolor=color[i],color='None')
        i = i+1
    #plt.hist(y_data, label = label_data,density = True)
    plt.legend(loc='upper right')
    ax.set_ylabel('andel land i verden')
    ax.grid(True)
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
            if(y_min > y):
                y_min  =y
            if(y_max < y):
                y_max = y
    width = (y_max-y_min)/(n_bins)
    bins = np.arange(y_min, y_max + width*2,width)

    return bins

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
    if(file_name):
        plt.savefig(file_name)


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



def plot_country_development(data_dic,country_array,file_name,label):

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
    plt.legend(loc='best', shadow=False, scatterpoints=1)
    plt.title(label)
    ax.set_xlabel("År")
    if(file_name):
        plt.savefig(file_name)


def get_mean_data_per_year(data_dic):
    n_country_per_year = np.zeros(25)
    avg = np.zeros(25)
    for country in data_dic :
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



file_name = "data/locality_index.csv"
data_dic = get_data_from_file(file_name, 0, 1)

target_names  =[]
last_country  = ""
for country in data_dic:
    if(last_country!= country):
        target_names.append(country)
        last_country = country

country_array = ["Norway","Sweden","Chile","Zimbabwe"]

file_name = "image/selected_lindex_plot.png"
plot_country_development(data_dic,country_array,None,"Utvikling av lokalitetsindeksen for utvalgte land")

plot_global_error_bar(data_dic,None,"Global utvikling av lokalitetsindeks",0)
years = list(range(25))
plot_varity_country(data_dic, "Variasjon i lokalitetsindeks for hvert land",target_names, None,years)
year = [0,5,10,15,14,24]

histogram_spread_in_y(data_dic, year,None,"Histogram av lokalitetsindeks")

file_name = "image/global_trend_env_fac.png"
plot_global_development(data_dic,None,"Global utvikling av lokalitetsindeks")

plt.show()
