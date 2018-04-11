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

def write_CO2_to_file(data, file_name):
    f = open(file_name, 'w')
    output = []
    for country in data:
        temp = []

        temp.append(country)
        for element in data[country]:
            temp.append(element)
        output.append(temp)
    with f:
        writer = csv.writer(f)
        writer.writerows(output)
    print("Writing complete")



file_name = "data/food_supply_quantity.csv"
food_quantity_countries = get_food_supply_quantity_from_file(file_name)
file_name = "data/CO2_per_food_type_v3.csv"
CO2_food_type =  get_CO2_foodtypes_from_file(file_name)
#test_country_array = ["Norway"]
test_country_array = ["Chad","Norway","Sweden","Afghanistan","Senegal","Zimbabwe"]

data_dic ={}
for country in food_quantity_countries:
    food_quantity = food_quantity_countries[country]
    data = get_total_CO2_country(CO2_food_type, food_quantity)
    data_dic[country] = data

file_name ="data/total_CO2_v3.csv"
write_CO2_to_file(data_dic, file_name)
