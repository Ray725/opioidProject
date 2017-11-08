#Combine data 
#Jason Mohabir

import pandas as pd

codes = "states-codes.csv"
codes_db = pd.read_csv(codes)
#print codes_db

death_2013_2014 = "2013-2014-death-data.csv"
death_2013_2014_db = pd.read_csv(death_2013_2014)
#print death_2013_2014_db

death_2015 = "2015-death-data.csv"
death_2015_db = pd.read_csv(death_2015)

death_2015_db = death_2015_db.iloc[:,0:4]
#print death_2015_db

db0 = pd.merge(codes_db, death_2013_2014_db, on="Abbreviation", how="left")
db1 = pd.merge(db0, death_2015_db, on="Abbreviation", how="left")

db1.to_csv("merged_deaths.csv")


