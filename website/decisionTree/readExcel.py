import pprint

import pandas as pd

file = r'data/Data1.xls'
data = pd.read_excel(file, sheet_name=0)
data.drop(data.columns[[0, -3]], axis=1, inplace=True)
data.fillna('', inplace=True)
features = list(data)
features.pop(-1)
print(features)
data = data.values.tolist()
dataSet = []
for item in data:
    print(item)
    dataSet.append(item)