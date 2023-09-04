import os
import pandas as pd
def import_data(root):
    dataframes = []
    for path, subdirs, files in os.walk(root):
        for name in files:
            file = os.path.join(path, name)
            if '.xlsx' in file:
                acc = pd.read_excel(file)
                dataframes.append(acc)
    return(dataframes)