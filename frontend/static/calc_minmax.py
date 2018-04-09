import json

min_value = 10000
min_contry = ""
max_value = -1
max_contry = ""
with open('locality.json', encoding='utf-8') as data_file:
    locality_data = json.loads(data_file.read())
data = {}
jsonFile = open("min_max_locality.json", "w+")
for i in range(1, 29):
    min_value = 10000
    min_contry = ""
    max_value = -1
    max_contry = ""
    for j in range(len(locality_data)):
        if( locality_data[j]["FIELD"+str(i+1)]>0):
            if(locality_data[j]["FIELD"+str(i+1)]> max_value):
                max_value = locality_data[j]["FIELD"+str(i+1)]
                max_contry = locality_data[j]["FIELD1"]
            if(locality_data[j]["FIELD"+str(i+1)]< min_value):
                min_value = locality_data[j]["FIELD"+str(i+1)]
                min_contry = locality_data[j]["FIELD1"]
    data["year_"+str(1985+i)]= {"min_name": min_contry, "min_value": min_value,
     "max_name":max_contry, "max_value": max_value}
    #data["year_"+str(1985+i)] = "0"

    """data["year_"+str(1985+i)]["name_min"] = min_contry
    data["year_"+str(1985+i)]["value_min"] = min_value
    data["year_"+str(1985+i)]["name_max"] = max_contry
    data["year_"+str(1985+i)]["value_max"] = max_value"""


json.dump(data, jsonFile)
jsonFile.close()

    #print(locality_data[i]["FIELD1"])
