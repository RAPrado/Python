#Declara uma lista vazia
list = []

#Adiciona um número na lista
list.append(7) # -> [7]
print(list)

#Adiciona outro número na lista, mas no final
list.append(5) # -> [7, 5]
print(list)

#Insere o número 12na lista, mas no indice de posição 1
list.insert(1,12) # [7, 12, 5]
print(list)

#Altera o valor da posição 0 para 4
list[0] = 4 # -> [4, 12, 5]
print(list)

#Remove da lista o valor 12
list.remove(12) # [4, 5]
print(list)

#Exibe o indice onde está armazenado o valor 5
list.index(5) # prints 1

#Adiciona uma nova lista no final da lista existente
list.extend([1, 2, 3]) # [4, 5, 1, 2, 3]
print(list)

#Exclui da lista um valor a partir do seu índice
del list[3] # [4, 5, 1, 3]
print(list)

#Exibe o tamanho da lista
len(list) # will print 4

#Navega por todos os itens da lista
for item in list :
    print(item)
