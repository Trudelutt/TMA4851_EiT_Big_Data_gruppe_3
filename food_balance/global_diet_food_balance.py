import csv
import numpy as np
import matplotlib.pyplot as plt

country_col = 0
food_t_col = 1
year_0_col = 3
n_years = 6
# years: 1961-1971-1981-1991- 2001- 2011

# get data from file, and devide into 3 arrays. One with name, one with type of food and one with each column being a countries spesific food types protein quantity per captia per year
def get_diet_countries_from_file(file_name):
    try:
        f = open(file_name,'r')
    except IOError:
        print("could not open file")
    reader = csv.reader(f, delimiter=",")
    diet_countries = {}
    last_country = " "
    for row in reader:
        quantity = [float(row[column]) for column in range(year_0_col,year_0_col + n_years)]
        item = row[1] + row[2]
        country = row[0]
        if( country in diet_countries):
            diet_countries[country][item] = quantity;
            #print(country," type ",item, diet_countries[country][item])
        else:
            diet_countries[country] = {}
            diet_countries[country][item] = quantity;


    f.close()
    return diet_countries

def get_global_diet_from_file(file_name):
    try:
        f = open(file_name,'r')
    except IOError:
        print("could not open file")
    reader = csv.reader(f, delimiter=",")
    global_diet = {};
    global_diet_counter = {}
    num_countires = 0;
    food_type = []
    for row in reader:
        quantity = [float(row[column]) for column in range(year_0_col,year_0_col + n_years)]
        country = row[0]
        item = row[1] + row[2]
        if( item in global_diet):
            for i in range(0,n_years):
                global_diet[item][i] += quantity[i]
        else:
            global_diet[item] = quantity
        num_countires += 1

    f.close()
    for item in global_diet:
        for i in range(0,n_years):
            global_diet[item][i] =global_diet[item][i] / float(num_countires)
    return global_diet

def get_global_development(country, global_diet, countires_diet):
    max_diff = get_max_diff_global_development( global_diet, countires_diet)
    country_diet = countires_diet[country]
    error = [0 for x in range(0,n_years)]
    for item in global_diet:
        if(item in country_diet):
            for j in range(0,n_years):
                if max_diff[item][j] == 0:
                    continue
                error[j] += abs(global_diet[item][j] - country_diet[item][j])/float(max_diff[item][j])
        else:
            for j in range(0,n_years):
                error[j] += 1.0
    return error

def get_max_diff_global_development( global_diet, countires_diet):
    max_diff = {}
    for country in countires_diet:
        country_diet = countires_diet[country]
        for item in global_diet:
            if item not in country_diet:
                continue;
            if(item in max_diff):
                for j in range(0,n_years):
                    diff = abs(global_diet[item][j] - country_diet[item][j])
                    if( diff > max_diff[item][j]):
                        max_diff[item][j] = diff
            else:
                max_diff[item] = [0 for column in range(0, n_years)];
                for j in range(0,n_years):
                    diff = abs(global_diet[item][j] - country_diet[item][j])
                    max_diff[item][j] = diff
    return max_diff

def development_trend_plot(error_array):
    fig, ax = plt.subplots()
    colour_array = ['red', 'green', 'blue','yellow','pink','purple']
    color_count = 0;
    for country in error_array:
        x = []
        y = []
        for i in range(0,n_years):
            y.append(error_array[country][i])
            x.append( 1961 +i*10)
        ax.scatter(x, y,c = colour_array[color_count],s = 60,label = country)
        color_count += 1
    ax.set_xlabel('year')
    ax.set_ylabel('error from global diet')
    ax.grid(True)
    ax.legend()
    plt.title("Global development")
    plt.show()


file_name = "data/global_diet_data.csv"
global_diet = get_global_diet_from_file(file_name)
countires_diet =  get_diet_countries_from_file(file_name)
test_country_array = ["Chad","Norway","Sweden","Afghanistan","Senegal","Zimbabwe"]
error_array = {}
for test_country in test_country_array :
    error = get_global_development(test_country, global_diet, countires_diet)
    error_array[test_country] = error
development_trend_plot(error_array)



'''for country in diet_countires:
    print ("***************",country, ": ")
    for y in diet_countires[country]:
        print (country,y,diet_countires[country][y] )'''
