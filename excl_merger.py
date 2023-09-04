# Author: Alberto Pabon-Castejon

import glob
import pandas as pd

path = "data/" # Place downloaded excel files here

file_list = glob.glob(path + "/*.xlsx") # Recognize each .xlsx file as an excel file.

excel_list = []

for file in file_list: # Goes through each excel file
    excel_list.append(pd.read_excel(file))

excel_merge = pd.concat(excel_list, ignore_index=True)

excel_merge.to_excel("Master_Sheet.xlsx", index = False) # Makes master excel file with all the data.

# df = pd.read_excel("Master_Sheet.xlsx")
# print(df)