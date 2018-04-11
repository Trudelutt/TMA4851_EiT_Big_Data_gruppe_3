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
def get_data_from_file(file_name, country_col, year_0_col):
    try:
        f = open(file_name,'r')
    except IOError:
        print("could not open file")
    reader = csv.reader(f, delimiter=",")
    data = {}
    country_not_allowed = {}
    for row in reader:
        temp = []
        country = row[country_col]
        if(country in country_not_allowed):
            continue
        for column in range(year_0_col,n_years):
            if '' == (row[column]):
                temp = []
                country_not_allowed[country] = 0
                break
            else:
                temp.append(float(row[column]))
        if( len(temp) == 0):

            continue
        quantity = np.array([temp])


        if country in data:
            data[country] += quantity
        else:
            data[country] = quantity

    f.close()
    return data

def get_CO2_data_from_file(file_name, country_col, year_0_col,food_approved):
    try:
        f = open(file_name,'r')
    except IOError:
        print("could not open file")
    reader = csv.reader(f, delimiter=",")
    data = {}
    country_not_allowed = {}
    last_country = " "
    for row in reader:
        temp = []
        country = row[country_col]
        item = row[1]
        if(item not in food_approved):
            continue
        if(country in country_not_allowed):
            continue
        for column in range(year_0_col,n_years):
            if '' == (row[column]):
                temp = []
                country_not_allowed[country] = 0
                break
            else:
                temp.append(float(row[column]))
        if( len(temp) == 0):
            continue
        if(len(data) == 0):
            last_country = country
        #if(last_country != country):
        #    exit()

        quantity = np.array([temp])
        #print(country)


        if country in data:
            data[country] += quantity
        else:
            data[country] = quantity
        #print(data[country])

    f.close()
    return data



def write_CO2_to_file(data, file_name):
    f = open(file_name, 'w')
    output = []
    for country in data:
        temp = []
        temp.append(country)
        if( country == 0):
            continue

        for i in range(len(data[country][0])):
            temp.append(data[country][0][i])
        output.append(temp)
    with f:
        writer = csv.writer(f)
        writer.writerows(output)
    print("Writing complete")

def calculate_CO2_per_capita(CO2_dic, pop_dic):
    temp_dic = {}
    for country in CO2_dic:
        if(country not in pop_dic):
            continue
        else:
            temp = []
            for i in range(len(CO2_dic[country][0])):
                temp.append((CO2_dic[country][0][i]*1000000) / (pop_dic[country][0][i]*1000.0))
            temp_dic[country] = [temp]
    return temp_dic

Food_approved = {}
Food_approved["Meat, cattle"] = 0
Food_approved["Milk, whole fresh cow"] = 0
Food_approved["Meat, chicken"] = 0
Food_approved["Eggs, hen, in shell"] = 0
Food_approved["Meat, pig"] = 0

file_name = "data/CO2_per_food_type_v2.csv"
CO2_dic = get_CO2_data_from_file(file_name, country_col, year_0_col,Food_approved)

file_name = "data/population.csv"

pop_dic = get_data_from_file(file_name, country_col, year_0_col)
data_dic = calculate_CO2_per_capita(CO2_dic, pop_dic)

print(pop_dic["Afghanistan"][0][0]*1000.0)
print(CO2_dic["Afghanistan"][0])
country = "Afghanistan"
print( CO2_dic[country][0][0]*1000000 / (pop_dic[country][0][0]*1000.0) )
print(data_dic["Afghanistan"][0])
file_name ="data/total_CO2_v2.csv"
write_CO2_to_file(data_dic, file_name)
