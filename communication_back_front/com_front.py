# https://www.sohamkamani.com/blog/2015/08/21/python-nodejs-comm/

from data_retrival import *

#pythonDictionary = {'type':'latLongAll', 'age':44, 'isEmployed':1}
import sys, json, numpy as np

#commands: CountryLatLon' -> give out country, lat and long

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    return json.loads(lines[0])

def main():
    #get our data as an array from read_in()
    info_node = read_in()

    # get command from node
    command = info_node['type']
    
    #command = 'CountryLatLon'
    if(command == 'CountryLatLon'):
        #data = get_all_lat_lon_time()
        country,lat,lon = get_all_lat_lon_time()
        data = {'country': country, 'lat':lat,'lon':lon}
    print(json.dumps(data))



if __name__ == '__main__':
        main()
