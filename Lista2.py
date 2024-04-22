#Adding two matrices / Somando duas matrizes
import numpy as np

a=[[1,2],[3,4]]
b=[[5,6],[7,8]]

#Example 1-Using numpy
print(np.array(a)+np.array(b))
#[[6, 8], [10, 12]]

#Example 2-Using Python list
resultado = []

for i in range(len(a)):
    linha = []

    for j in range(len(a[0])):
        linha.append(a[i][j] + b[i][j])

    resultado.append(linha)

print(resultado)
[[6, 8], [10, 12]]

#Example 3-Using Python list with list comprehension
print([[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))] ) 
