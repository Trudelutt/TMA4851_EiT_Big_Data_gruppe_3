import csv
import numpy as np

file_name = "data/all_protein.csv"
country_col = 0
food_t_col = 1
year_0_col = 3
n_years = 6
# years: 1961-1971-1981-1991- 2001- 2011


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

def get_country_total(country,protein_quantity):
    country_total;
    temp = {};
    last_contry = ""
    total =[0,0,0,0,0,0];
    for j in range(0,len(country)):
        if(last_contry != country[j]):
            temp = {"country":last_country,"quantity":total}
            country_total.append(temp)
            total =[0,0,0,0,0,0];
            last_country = countr[j]
        else:
            for i in range(0,n_years):
                total[i] += protein_quantity[j][i]

    return country_total


country,food_type,protein_quantity = get_data_from_file(file_name)
