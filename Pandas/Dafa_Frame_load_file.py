#Reference : https://www.w3schools.com/python/pandas/pandas_csv.asp

import pandas as pd

#Show the number of rows defined to be displayed
print(pd.options.display.max_rows) 

#Defined a new number of rows to be displayed
pd.options.display.max_rows = 20

#Load a csv file
df = pd.read_csv('teste.csv')

#print just part of lines, according with maxrows
print(df) 

#print the entire DataFrame
#print(df.to_string())
