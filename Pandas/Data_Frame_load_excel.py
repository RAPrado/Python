#Reference : https://stackoverflow.com/questions/52763680/jupyter-notebook-cant-find-pyxlsb-module
#            https://acervolima.com/como-importar-um-arquivo-excel-para-python-usando-pandas/

#Caso dê erro na importação, instalar essa biblioteca.
#pip install pyxlsb

import pandas as pd

#Exemplo 1
df = pd.read_excel("arquivo.xlsb")
print(df) 

#Exemplo 2 - definindo a coluna a ser importada
df = pd.read_excel("arquivo.xlsx",index_col = 0)
print(df)

#Exemplo 3 - ignorando header
df = pd.read_excel("arquivo.xlsx",header = None)
print(df) 
