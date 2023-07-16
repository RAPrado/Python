#Reference : https://www.w3schools.com/python/pandas/pandas_getting_started.asp
#Data sets in Pandas are usually multi-dimensional tables, called DataFrames. Series is like a column, a DataFrame is the whole table.

import pandas as pd

mydataset = {
  'cars': ["Mercedes", "Tesla", "Toyota"],
  'passings': [4, 4, 5]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
