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
#Read aleatory samples
df.sample(10)
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
#Describe columns only numerics
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

#Category columns
df.describe(include=['object'])

#List all columns
df.describe(include='all')

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

#Time      2
#V1        1
#V2        3
#dtype: int64

#Ordenando as colunas com nulos descrescente
df.isnull().sum().sort_values(ascending = False)
#Time      3
#V1        2
#V2        1
#dtype: int64

#Exibindo em percentual e somente os maiores que zero
nulos=df.isnull().sum().sort_values(ascending = False)
nulos[nulos>0]/df.shape[0]*100

# Removemo as linhas com valores nulos e salva o resultado no próprio dataframe através do parâmetro : inplace = True
df.dropna(inplace = True)

######################################################
# Verifica registros duplicados
df.duplicated().sum()

#Deleta registros duplicados baseados em todas as colunas
df.drop_duplicates()

#Deleta registros duplicados baseado em uma coluna
df.drop_duplicates(subset=['coluna_a'])

#Deleta registros duplicados baseado em duas colunas e mantem a última ocorrência
df.drop_duplicates(subset=['coluna_a', 'coluna_b'], keep='last')

######################################################
#Removendo colunas
df.drop(['coluna_a','coluna_b'],axis = 1, inplace = True)

######################################################
#Ordering by a field
df = df.sort_values('nome do campo', ascending=False) #To ordering ascending, just put True or omit de parameter.

######################################################
# Merge entre dataframes
df_a = df_a.merge(df_b, on = 'coluna id')

######################################################
# Filtrando o dataframe e mantendo somente as colunas desejadas
df = df[['coluna_a', 'coluna_b']]

######################################################
# Criando uma nova coluna no dataframe
df['coluna_c'] = df_outro['coluna_z']

######################################################
# Showing the columns
df.columns
Index(['Country', 'Year', 'Status', 'Life expectancy ', 'Adult Mortality',
       'infant deaths', 'Alcohol', 'percentage expenditure', 'Hepatitis B',
       'Measles ', ' BMI ', 'under-five deaths ', 'Polio', 'Total expenditure',
       'Diphtheria ', ' HIV/AIDS', 'GDP', ' Population',
       ' thinness  1-19 years', ' thinness 5-9 years',
       'Income composition of resources', 'Schooling'],
      dtype='object')

# Rename the columns
df = pd.DataFrame({'country': df_dsa['Country'],
                   'life_expectancy': df_dsa['Life expectancy '],
                   'year': df_dsa['Year'],
                   'status': df_dsa['Status'],
                   'adult_mortality': df_dsa['Adult Mortality'],
                   'inf_death': df_dsa['infant deaths'],
                   'alcohol': df_dsa['Alcohol'],
                   'hepatitisB': df_dsa['Hepatitis B'],
                   'measles': df_dsa['Measles '],
                   'bmi': df_dsa[' BMI '],
                   'polio': df_dsa['Polio'],
                   'diphtheria': df_dsa['Diphtheria '],
                   'hiv': df_dsa[' HIV/AIDS'],
                   'gdp': df_dsa['GDP'],
                   'total_expenditure': df_dsa['Total expenditure'],
                   'thinness_till19': df_dsa[' thinness  1-19 years'],
                   'thinness_till9': df_dsa[' thinness 5-9 years'],
                   'school': df_dsa['Schooling'],
                   'population': df_dsa[' Population']})

######################################################
# Aplicando uma função para tratar o conteúdo de uma coluna
df['coluna_a'] = df['coluna_a'].apply(nome_da-função)

# Se a função chamada exige parâmetros, basta informar usando o comando "args=(,)" e dentro dos parenteses passar o parâmetro, e após o parâmetro, dever terminar com uma vírgula ","
df['coluna_a'] = df['coluna_a'].apply(nome_da-função,args=('param1',))

# Split do conteúdo
df['coluna_a'] = df['coluna_a'].apply(lambda x:x.split()) #Como não foi informado nada no split(), aplica o split usando o espaço como serador, mas poderia usar split(';').

# Join do conteúdo
df['coluna_a'] = df['coluna_a'].apply(lambda x:" ".join(x))

# Substiui espaço por vazio.
df['coluna_a'] = df['coluna_a'].apply(lambda x:[i.replace(" ","") for i in x])

# Transforma conteúdo em minúsculo
df['coluna_a'] = df['coluna_a'].apply(lambda x:x.lower())

######################################################
# Tratando os nulos, preenchendo com a mediana dos demais valores (Usando transform ao invés do apply)
def calc_median(valores):
    return valores.fillna(valores.median())
  
df.coluna_a = df['coluna_a'].transform(calc_median)

######################################################
#Faz group by pelo campo escolhido, e count dos registros
df.groupby("Class").size()
#Class
#0    284315
#1       492
#dtype: int64


# Agrupar as transações por classe e selecionar a variável "Amount"
data = df.groupby("Class")["Amount"].apply(list)

data.head()
#Class
#0    [149.62, 2.69, 378.66, 123.5, 69.99, 3.67, 4.9...
#1    [0.0, 529.0, 239.93, 59.0, 1.0, 1.0, 1.0, 1.0,...
#Name: Amount, dtype: objec

#Ler colunas específica
df[['Coluna A','Coluna B']]

######################################################
#Count values / Frequency
df['Column_A'].value_counts()
#Column_A
#Sim    282
#Nao    118
#Name: count, dtype: int64

######################################################
#Contingency table
pd.crosstab(df['status_entrega'], df['area_urbana'])
#   area_urbana Nao Sim
#status_entrega		
#           Bom	28   57
#         Medio	68  151
#          Ruim	22   74


#Using three columns
pd.crosstab(index = [df['status_entrega'], df['area_urbana']], 
            columns = df['cliente_local'],
            margins = True, 
            margins_name = "Total")

#    cliente_local Nao	Sim	Total
#status_entrega	area_urbana			
#           Bom	Nao  6	22	28
#               Sim	18	39	57
#         Medio	Nao	29	39	68
#               Sim	55	96	151
#          Ruim	Nao	11	11	22
#               Sim	23	51	74
#Total		         142 258 400
