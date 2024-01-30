import pandas as pd
pd.__version__

df = pd.read_csv('Portugal.csv',delimiter=';')

######################################################
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

######################################################
#Read bot lines
df.tail()

#                  Indicador   Ano      Valor
#16  Jovens menos de 15 anos  1981  2.493.763
#17  Jovens menos de 15 anos  1991  1.959.671
#18  Jovens menos de 15 anos  2001  1.679.191
#19  Jovens menos de 15 anos  2011  1.588.663
#20  Jovens menos de 15 anos  2021  1.365.940

######################################################
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


#Ou uma versão mais reduzida
df.dtypes

######################################################
#Describe columns
df.describe()

#          CampoA
#count     6.485300e+04
#mean      5.671174e+06
#std       4.080150e+06
#min       4.316000e+03
#25%       3.921216e+06
#50%       5.871981e+06
#75%       7.225856e+06
#max       9.900000e+07

df.describe().applymap('{:,.2f}'.format) #Formating with 2 decimal positions
#          CampoA
#count     6.48
#mean      5.67
#std       4.08
#min       4.31
#25%       3.92
#50%       5.87
#75%       7.22
#max       9.90

######################################################
# Saber o tamanho do dataset : linhas/colunas
df.shape
#(284807, 31)

######################################################
#Saber o total de valores ausentes ("missing values") em cada coluna. 
df.isnull().sum()

#Time      0
#V1        0
#V2        0
#dtype: int64
  
