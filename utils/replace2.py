#Replace incorrect Geo-JSON with CORRECT OPIOID
import pandas as pd
import json

file = "Interpolated_Death_Year_Opioid.csv"
df1 = pd.read_csv(file)
df2 = df1.set_index("State")
grouped = df2.groupby('Year')

with open('us-states.geojson') as data_file:    
    data = json.load(data_file)

for n in range(50):
    del data["features"][n]["properties"]["deaths"] 

    state = data["features"][n]["properties"]['name']
   
    for i in range(1999,2015):
        deaths = grouped.get_group(i)["Deaths"].loc[state,]
        year_death = str(i)+'death'
        data["features"][n]["properties"][year_death] = deaths

with open('us-states-opioid_update.geojson', 'w') as outfile:
    json.dump(data, outfile)
