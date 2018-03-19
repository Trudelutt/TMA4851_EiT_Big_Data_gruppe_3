import json

count = 0
with open('world-50m-with-population.json', encoding='utf-8') as data_file:
    map_data = json.loads(data_file.read())
with open('locality.json', encoding='utf-8') as data_file:
    locality_data = json.loads(data_file.read())
for i in range(len(map_data["objects"]["units"]["geometries"])):
    for k in range(1,29):
        map_data["objects"]["units"]["geometries"][i]["properties"]["year_"+str(1985+k)] = 0
    #print(map_data["objects"]["units"]["geometries"][i]["properties"]["name"])
    tempcount = 0
    for j in range(len(locality_data)):
        if(map_data["objects"]["units"]["geometries"][i]["properties"]["name_long"] == locality_data[j]["FIELD1"]):
            count += 1
            for k in range(1,29):
                map_data["objects"]["units"]["geometries"][i]["properties"]["year_"+str(1985+k)] = locality_data[j]["FIELD"+str(k+1)]
        else:
            tempcount += 1
        if tempcount == len(locality_data):
            print(map_data["objects"]["units"]["geometries"][i]["properties"]["name_long"])
print(count, len(locality_data))
#print(map_data["objects"]["units"]["geometries"][i]["properties"][1986+i])

jsonFile = open("heatmap.json", "w+")
json.dump(map_data, jsonFile)
jsonFile.close()
print(count, len(locality_data), len(map_data["objects"]["units"]["geometries"]))
    #print(locality_data[i]["FIELD1"])
