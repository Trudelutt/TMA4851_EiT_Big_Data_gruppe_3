import csv
import numpy as np
import matplotlib.pyplot as plt

country_col = 0
food_t_col = 1
year_0_col = 3
n_years = 6
# years: 1961-1971-1981-1991- 2001- 2011

# get data from file, and devide into 3 arrays. One with name, one with type of food and one with each column being a countries spesific food types protein quantity per captia per year
def get_data_from_file(file_name):
    try:
        f = open(file_name,'r')
    except IOError:
        print("could not open file")
    reader = csv.reader(f, delimiter=",")
    country = []
    food_type = []
    protein_quantity=[]
    for row in reader:
        quantity = [float(row[column]) for column in range(year_0_col,year_0_col + n_years)]
        country.append(row[0])
        food_type.append(row[1])
        protein_quantity.append(quantity)
    f.close()
    return country,food_type,protein_quantity

# get total number of protein for a certain category ( meat, total etc.)
def get_total_protein_per_category(country,protein_quantity):
    temp = {};
    last_country= country[0]
    total =[0,0,0,0,0,0];
    for j in range(0,len(country)):
        if(last_country != country[j]):
            temp[last_country] = total
            total =[0,0,0,0,0,0];
            last_country = country[j]
        else:
            for i in range(0,n_years):
                total[i] += protein_quantity[j][i]
    return temp

# plot protein from meat per capita per year vs. protein ( summed every food categorty) per capita per year
# 6 points per color = a country protein comparison for 6 years
def meat_vs_total_protein_plot(country_list,country_total_protein, country_toatal_meat_protein):
    fig, ax = plt.subplots()
    colour_array = ['red', 'green', 'blue','yellow','pink','purple']
    country_array  = ['Norway', 'Angola', 'Australia','United Arab Emirates','Sweden','Viet Nam'] # for testing
    for i in range(0,len(country_array)):
        x = country_total_protein[country_array[i]]
        y = country_toatal_meat_protein[country_array[i]]
        ax.scatter(x, y,c=colour_array[i],  label=country_array[i],s = 60)
    ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
    ax.set_xlabel('total protein per capita per year (g/capita/day)')
    ax.set_ylabel('protein from meat per capita per year (g/capita/day)')
    ax.grid(True)
    plt.show()


file_name = "data/all_protein.csv"
country_all,food_type_all,protein_quantity_all = get_data_from_file(file_name)
country_total_protein= get_total_protein_per_category(country_all,protein_quantity_all)

file_name = "data/meat_protein.csv"
country_meat,food_type_meat,protein_quantity_meat = get_data_from_file(file_name)
country_toatal_meat_protein = get_total_protein_per_category(country_meat,protein_quantity_meat)

meat_vs_total_protein_plot(country_all,country_total_protein, country_toatal_meat_protein)
