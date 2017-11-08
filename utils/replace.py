#Replace incorrect Geo-JSON
import pandas as pd
import json

file = "merged_deaths.csv"
df1 = pd.read_csv(file)
df2=df1.set_index("State")
#print df2


with open('us-states.geojson') as data_file:    
    data = json.load(data_file)

states = len(data["features"])

for n in range(50):
    del data["features"][n]["properties"]["deaths"] 

    state = data["features"][n]["properties"]['name']
    num_2015 = df2.loc[state,"2015Number"]
    num_2014 = df2.loc[state,"2014Number"]
    num_2013 = df2.loc[state,"2013Number"]

    data["features"][n]["properties"]['2015death'] = int(num_2015.replace(',',''))
    data["features"][n]["properties"]['2014death'] = int(num_2014.replace(',',''))
    data["features"][n]["properties"]['2013death'] = int(num_2013.replace(',',''))

with open('us-states-update.geojson', 'w') as outfile:
    json.dump(data, outfile)
