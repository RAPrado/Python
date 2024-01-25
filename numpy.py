import numpy as np

#Cria array bi-dimensional
dado = [[1.0,2,3],[4,5.0,6]]

#Converte o array para Numpy
meu_array = np.array(dado,dtype=int)
print(meu_array)

#Cria array com 1 linha e 10 valores.
meu_array = np.arange(10)
print(meu_array)

#Cria array com 3 linhas e 4 colunas, com valores zerados.
meu_array = np.zeros((3,4),dtype=int)
print(meu_array)

#Cria array com 3 linhas e 4 colunas, com valor 1.
meu_array = np.ones((3,4),dtype=int)
print(meu_array)

#Cria array com 3 linhas e 4 colunas, com valores vazio.
meu_array = np.empty((2,2),dtype=int)
print(meu_array)

#Cria array com 3 linhas e 5 colunas, com valores randômicos.
meu_array = np.random.randn(3,5)
print(meu_array)

#****************************************************************************************
#Compara usando o array nativo do Python vs usando Numpy
import time
import numpy as np

a = time.time()
L = range(100000000)
[i**2 for i in L]
print (time.time() - a)
#Tempo de execução em segundos : 22.808863401412964

a = time.time()
b = np.arange(10000000)
b**2
print (time.time() - a)
#Tempo de execução em segundos : 0.028621673583984375
