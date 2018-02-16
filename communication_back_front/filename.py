# https://www.sohamkamani.com/blog/2015/08/21/python-nodejs-comm/


#pythonDictionary = {'type':'latLongAll', 'age':44, 'isEmployed':1}
import sys, json, numpy as np
import csv
#commands: latLongAll

# file FAO.CSV column header
country_col = 2
lat_col = 8
lon_col = 9

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    return json.loads(lines[0])
def get_all_lat_lon_time():
    f = open("FAO.csv")
    reader = csv.reader(f)
    rownum = 0
    prev_country = " "
    data = []
    for row in reader:
        if(row[country_col] != prev_country and rownum != 0):
            data.append({str(row[country_col]): [float(row[lat_col]),float(row[lon_col])]})
            prev_country = row[country_col]
        rownum += 1
    f.close()
    return data

def main():
    #get our data as an array from read_in()
    info_node = read_in()

    # get command from node
    command = info_node['type']

    if(command == 'timeLatLon'):
        data = get_all_lat_lon_time()

    print(json.dumps(data))


#start process
if __name__ == '__main__':
        main()
