#Reference : https://www.w3schools.com/python/pandas/pandas_getting_started.asp

import pandas as pd

mydataset = {
  'cars': ["Mercedes", "Tesla", "Toyota"],
  'passings': [4, 4, 5]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
