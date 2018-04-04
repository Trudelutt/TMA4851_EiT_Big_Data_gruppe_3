import csv
import numpy as np
import matplotlib.pyplot as plt

country_col = 0
food_t_col = 1
year_0_col = 3
n_years = 6
# years: 1961-1971-1981-1991- 2001- 2011

# get data from file, and devide into 3 arrays. One with name, one with type of food and one with each column being a countries spesific food types protein quantity per captia per year
def get_country_kcal(file_name):
    try:
        f = open(file_name,'r')
    except IOError:
        print("could not open file")
    reader = csv.reader(f, delimiter=",")
    kcal_countries = {}
    for row in reader:
        quantity = [float(row[column]) for column in range(year_0_col,year_0_col + n_years)]
        country = row[0]
        if( country in kcal_countries):
            for i in range(0,n_years):
                kcal_countries[country][i] += quantity[i]
        else:
            kcal_countries[country] = quantity;
    f.close()
    return kcal_countries




def development_trend_plot(data,countries):
    fig, ax = plt.subplots()
    color_count = 0;
    for country in data:
        x = []
        y = []
        for i in range(0,n_years):
            y.append(data[country][i])
            x.append( 1961 +i*10)
        ax.plot(x, y,label = country)
        color_count += 1
    ax.set_xlabel('year')
    ax.set_ylabel('total kcal\capita\day')
    ax.grid(True)
    ax.legend()
    plt.title("Global development")
    plt.show()


file_name = "data/kcal_food_data_2.csv"
kcal_countries = get_country_kcal(file_name)
#kcal_countries = get_country_group(file_name)
test_country_array = ["Chad","Norway","Sweden","Afghanistan","Senegal","Zimbabwe"]

development_trend_plot(kcal_countries,test_country_array)
