#Code to parse all .xlsx sheets in a directory

#imports
import pandas as pd
from helpers import import_data

data = import_data('./data/')

print(data)



