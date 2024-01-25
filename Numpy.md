# Numpy - exemplos de arrays

**Importar a biblioteca Numpy**
```python
import numpy as np
```

**Cria array bi-dimensional usando função nativa do Python**
```python
dado = [[1.0,2,3],[4,5.0,6]]
print(meu_array)
```

**Converte o array nativo para Numpy**
```python
meu_array = np.array(dado,dtype=int)<br>
print(meu_array)
```

**Cria array com 1 linha e 10 valores**
```python
meu_array = np.arange(10)
print(meu_array)
```

**Cria array com 3 linhas e 4 colunas, com valores zerados**
```python
meu_array = np.zeros((3,4),dtype=int)
print(meu_array)
```

**Cria array com 3 linhas e 4 colunas, com valor 1**
```python
meu_array = np.ones((3,4),dtype=int)
print(meu_array)
```

**Cria array com 3 linhas e 4 colunas, com valores vazio**
```python
meu_array = np.empty((2,2),dtype=int)
print(meu_array)
```

**Cria array com 3 linhas e 5 colunas, com valores randômicos**
```python
meu_array = np.random.randn(3,5)
print(meu_array)
```


# Compara tempo de processamento usando o array nativo do Python vs usando Numpy
```python
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
```

Referência : https://estruturas.ufpr.br/disciplinas/pos-graduacao/introducao-a-computacao-cientifica-com-python/introducao-python/2-1-o-objeto-array-do-numpy/
