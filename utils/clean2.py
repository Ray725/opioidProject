#Combine data 
#Jason Mohabir

import pandas as pd

codes = "states-codes.csv"
codes_db = pd.read_csv(codes)
print codes_db

death_1999_2015 = "Interpolated_Death_Year_Opioid.csv"
death_1999_2015_db = pd.read_csv(death_1999_2015)
print death_1999_2015_db

db0 = pd.merge(codes_db, death_1999_2015_db, on="Abbreviation", how="left")

#db0.to_csv("merged_death_1999_2015.csv")


