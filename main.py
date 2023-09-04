#Code to parse all .xlsx sheets in a directory

#imports
import pandas as pd
from helpers import import_data

data = import_data('./data/')
# create format for mastersheet
df_master = pd.DataFrame(columns=['Name', 'Email', 'Discord', 'Year', 'Major', 'Misc'])
df_format = pd.DataFrame(columns=['Name', 'Email', 'Discord', 'Year', 'Major', 'Misc']) #create format for mastersheet

#misc will contain comma-seperated/dictionary of data from other fields that are not specified

for db in data:
    df_temp = df_format
    print(db.head())
    


