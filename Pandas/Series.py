#Reference : https://www.w3schools.com/python/pandas/pandas_getting_started.asp
#A Pandas Series is like a column in a table. It is a one-dimensional array holding data of any type.

############################################################################################################
#1-Create a simple Pandas Series from a list
#import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

#Returning all the series
print(myvar)

#Returning the position 1
print(myvar[1])

############################################################################################################
#2-With the index argument, you can name your own labels.
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar["y"])

############################################################################################################
#3-You can also use a key/value object, like a dictionary, when creating a Series.
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

############################################################################################################
#4-Create a Series using only data from "day1" and "day2":
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)
