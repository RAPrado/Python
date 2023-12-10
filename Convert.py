#Converter para inteiro
x = int(10.1) #Resultado = 10
y = int('10') #Resultado = 10

#Converter para decimal
x = float(10) #Resultado = 10.0
y = float('10') #Resultado = 10.0

#Converter para character
x = str(10) #Resultado = 10

#Coverter para data
from datetime import datetime
dia = str(1)
mes = str(12)
ano = str(2023)

#Exemplo 1
data = dia+'/'+mes+'/'+ano #1/12/2023
data_convertida =  datetime.strptime(data,/ '%d/%m/%Y').date()
print(data_convertida) #01/12/2023

#Exemplo 2
data = ano+'/'+mes+'/'+dia #2023/12/1
data_convertida = datetime.strptime(str_date, '%Y-%m-%d').date()
print(data_convertida) #2023/12/01
