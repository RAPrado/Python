import pandas as pd
pd.__version__

df = pd.read_csv('Portugal.csv',delimiter=';')

#Read top lines
df.head()

#or specifing lines to read
df.head(10)

#              Indicador   Ano      Valor
#0  População residente   1960   8.865,00
#1  População residente   1970   8.680,40
#2  População residente   1981   9.851,30
#3  População residente   1991   9.960,20
#4  População residente   2001  10.362,70

#Read bot lines
df.tail()

#                  Indicador   Ano      Valor
#16  Jovens menos de 15 anos  1981  2.493.763
#17  Jovens menos de 15 anos  1991  1.959.671
#18  Jovens menos de 15 anos  2001  1.679.191
#19  Jovens menos de 15 anos  2011  1.588.663
#20  Jovens menos de 15 anos  2021  1.365.940

#Info about the file
df.info()

#<class 'pandas.core.frame.DataFrame'>
#RangeIndex: 21 entries, 0 to 20
#Data columns (total 3 columns):
  #   Column     Non-Null Count  Dtype 
#---  ------     --------------  ----- 
# 0   Indicador  21 non-null     object
# 1   Ano        21 non-null     int64 
# 2   Valor      17 non-null     object
#dtypes: int64(1), object(2)
#memory usage: 636.0+ bytes