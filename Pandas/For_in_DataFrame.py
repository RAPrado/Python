#Iterando as linhas de um DataFrame
#Reference : https://www.youtube.com/watch?v=rsyvErL0Bo8

#Cria um df lendo um csv
df = pd.read_csv('Origem.csv',encoding='utf-8',delimiter=';')

#Forma 1 de iterar um DataFrame - método mais rápido
for row in df.itertuples():
    print(row.Nome_Coluna)

#Forma 2 de iterar um DataFrame
for item in range(len(df)):
    print(df['Nome_Coluna'][item])
