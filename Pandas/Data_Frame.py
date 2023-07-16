#Reference : https://www.w3schools.com/python/pandas/pandas_getting_started.asp
#Data sets in Pandas are usually multi-dimensional tables, called DataFrames. Series is like a column, a DataFrame is the whole table.

#1-Example
import pandas as pd

mycars = {
  'cars': ["Mercedes", "Tesla", "Toyota"],
  'passings': [4, 4, 5]
}

#load data into a DataFrame object:
df = pd.DataFrame(mycars)

print(df)

#Returning a specified row
print(df.loc[0])

#use a list of indexes, returning rows 0 and 1
print(df.loc[[0, 1]])


#2-Add a list of names to give each row a name
import pandas as pd

mycars = {
  'cars': ["Mercedes", "Tesla", "Toyota"],
  'passings': [4, 4, 5]
}

#load data into a DataFrame object:
df = pd.DataFrame(mycars)

df = pd.DataFrame(mycars, index = ["line1", "line2", "line2"])

print(df)

#refer to the named index:
print(df.loc["line1"])
