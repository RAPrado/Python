#Reference : https://stackoverflow.com/questions/52763680/jupyter-notebook-cant-find-pyxlsb-module
#            https://acervolima.com/como-importar-um-arquivo-excel-para-python-usando-pandas/

pip install pyxlsb

import pandas as pd

#Exemplo 1
df = pd.read_excel("arquivo.xlsb",sheet_name="Nome_da_sheet")
print(df) 

#Exemplo 2 - definindo a coluna a ser importada
df = pd.read_excel("arquivo.xlsx",index_col = 0)
print(df)

#Exemplo 3 - ignorando header
df = pd.read_excel("arquivo.xlsx",header = None)
print(df) 

#Exemplo 4 - alterando o tipo de dados das colunas
df = pd.read_excel("arquivo.xlsx",
                   dtype = {"Products": str,
                            "Price":float}))

Exemplo 5 - alterando valores de dados desconhecidos para “NaN ”
df = pd.read_excel("arquivo.xlsx",                    
                   na_values =['item1', 
                               'item2'])
print(df) 
