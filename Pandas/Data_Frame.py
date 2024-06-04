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


############################################################################################
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


############################################################################################
#3-Add new row in a dataframe
import pandas as pd
Texto = {
        'Coluna_Nome':[
         """Linha 1""",
         """Linha 2"""]
        }

df = pd.DataFrame(Texto) #Create the dataframe

df2 = pd.DataFrame(["Linha 3"], columns=['Coluna_Nome']) #Create a new df with de new row.
df = pd.concat([df, df2], ignore_index=True) #Use pd.concat to concatenate the new row in existing df.


############################################################################################
#4-Changing column datatype
import pandas as pd

df1 = pd.DataFrame([],columns=['Coluna_a','Coluna_b'])
print(df1.dtypes)

df1['Coluna_a'] = df1['Coluna_a'].astype(str)
df1['Coluna_b'] = df1['Coluna_b'].astype(float)
print(df1.dtypes)
