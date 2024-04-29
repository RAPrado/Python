#Calcula a determinante e a inversa da matriz.
import numpy as np

matriz = np.array([[1, 2], [2, 2]])

#Calcula a Determinante da matriz.
print(np.linalg.det(matriz))
#-2.0

#Usando fórmula
print(matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0])
#2



#Calcula a Inversa da matriz. Quando a determinante for zero, não tem inversa.
#Usando numpy
print(np.linalg.inv(matriz))
#[[-1.   1. ]
#[ 1.  -0.5]]

#Usando fórmula
def inversa_2x2(matriz):
    det = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    if det == 0:
        return "A matriz não tem inversa pois o determinante zero."
    else:
        return [[matriz[1][1] / det, -matriz[0][1] / det],
                [-matriz[1][0] / det, matriz[0][0] / det]]

print(inversa_2x2(matriz))
#[[-1.0, 1.0], [1.0, -0.5]]
