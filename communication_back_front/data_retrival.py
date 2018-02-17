import csv

# file FAO.CSV column header
country_col = 2
lat_col = 8
lon_col = 9

def get_all_lat_lon_time():
    f = open("FAO.csv")
    reader = csv.reader(f)
    rownum = 0
    prev_country = " "
    country = []
    lat = []
    lon = []
    for row in reader:
        if(row[country_col] != prev_country and rownum != 0):
            country.append(str(row[country_col]))
            lat.append(float(row[lat_col]))
            lon.append(float(row[lon_col]))
            prev_country = row[country_col]
        rownum += 1
    f.close()
    return country,lat,lon
