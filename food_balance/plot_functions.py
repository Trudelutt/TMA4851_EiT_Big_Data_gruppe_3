
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
import matplotlib.cm as cm
import matplotlib.pylab as pl
import plotly.plotly as py
import csv



def histogram_spread_in_y(data_dic, year_array,file_name,label,year_0):
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
        label_data.append(year+year_0)

        results, edges = np.histogram(y_year,bins = bins, normed=True)
        binWidth = edges[1] - edges[0]
        plt.bar(edges[:-1], results*binWidth, binWidth,label=year+year_0,edgecolor=color[i],color='None')
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

def plot_global_development(data_dic,file_name,y_label,year_0):
    data = get_mean_data_per_year(data_dic)
    x = []
    y = []
    fig, ax = plt.subplots()
    for i in range(len(data)):
        y.append(data[i])
        x.append(i + year_0)
    plt.plot(x, y)
    ax.set_xlabel('År')
    ax.set_ylabel(y_label)
    if(file_name):
        #plt.savefig(file_name, dpi=None, facecolor='w', edgecolor='w', orientation='portrait', papertype=None, format=None,transparent=False, bbox_inches='tight', pad_inches=0.1, frameon=None)
        plt.savefig(file_name)

def plot_varity_country(data_dic, y_label,all_countries, file_name,years):
    country_plot_order =  remove_invalid_countries_from_list(data_dic, country_plot_order_origin)
    plt.figure(figsize=(15, 10), dpi=100)
    cmap = plt.get_cmap('viridis')
    colors = cmap(np.linspace(0, 1, len(region_list)))
    region_color = {"Europe":pl.cm.Blues(np.linspace(0,1,len(years))), "Oceania":pl.cm.Greens(np.linspace(0,1,len(years))), "Africa":pl.cm.Reds(np.linspace(0,1,len(years))), "Asia":pl.cm.Purples(np.linspace(0,1,len(years))), "Americas":pl.cm.Greys(np.linspace(0,1,len(years)))}
    plt.grid()
    for i in range(len(country_plot_order)):
        x = []
        y  = []
        country = country_plot_order[i]
        region = country_region[country]
        colors = region_color[region]
        for year in years:
            x.append(i)
            y.append(data_dic[country][year])
        plt.scatter(x,y,c = colors)

    x =[i for i in range(len(country_plot_order))]
    plt.xticks(x, country_plot_order,rotation='vertical')
    plt.ylabel(y_label)
    if(file_name):
        plt.savefig(file_name, dpi=None, facecolor='w', edgecolor='w', orientation='portrait', papertype=None, format=None,transparent=False, bbox_inches='tight', pad_inches=0.1, frameon=None)
        #plt.savefig(file_name)


def remove_invalid_countries_from_list(data_dic, country_plot_order):
    country_plot_order_2 = []
    for country in country_plot_order:
        if country in data_dic:
            country_plot_order_2.append(country)
    return country_plot_order_2


def plot_country_development(data_dic,country_array,file_name,y_label,label_on,year_0):

    fig, ax = plt.subplots()
    for country in country_array:
        x = []
        y = []
        data = data_dic[country]
        for i in range(len(data)):
            if( data[i] == None):
                continue
            y.append(data[i])
            x.append(i + year_0)
        plt.plot(x, y,label = country)
    if(label_on):
        plt.legend(loc='best', shadow=False, scatterpoints=1)
    ax.set_ylabel(y_label)
    ax.set_xlabel("År")
    if(file_name):
        plt.savefig(file_name)


def get_mean_data_per_year(data_dic):
    n_country_per_year = np.zeros(len(data_dic["Norway"]))
    avg = np.zeros(len(data_dic["Norway"]))
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
    ma = np.ones(len(data_dic["Norway"]))*(-10000000000)
    mi = np.ones(len(data_dic["Norway"]))*100000000000
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





def plot_global_error_bar(data_dic,file_name,y_label,locality_index,year_0):
    fig, ax = plt.subplots()
    all_points_x = []
    all_points_y = []
    for country in data_dic:
        for i in range(len(data_dic[country])):
            if(data_dic[country][i] is  None ):
                continue
            all_points_x.append(i+year_0)
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
        x.append(i + year_0)
    plt.scatter(all_points_x, all_points_y, s = 5)
    ax.errorbar(x, y, yerr=y_err, fmt='o',c = "red")
    #ax.errorbar(x, y,yerr = y_err)

    ax.set_xlabel('År')
    ax.set_ylabel(y_label)
    if(file_name):
        plt.savefig(file_name,format='eps')

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


file_name = "data/country_region.csv"
country_region, region_list = get_country_region_from_file(file_name, 0, 1)

country_plot_order_origin = []
for region in region_list:
    for country in region_list[region]:
        country_plot_order_origin.append(country)
