#Referência : https://openclassrooms.com

#Dupla são listas que não podem ser modificadas. São declaradas usando parenteses e não chaves (contrário das listas puras).
my_tuple = (1, 2, 3, 'a', 'b')

#Imprime o conteúdo
print(my_tuple[1]) # -> 2
print(my_tuple[4]) # -> 'b'

#Tenta atribuir um valor, mas dá erro.
my_tuple[1]=2

#---------------------------------------------------------------------------
#TypeError                                 Traceback (most recent call last)
#<ipython-input-7-61754d14ee68> in <module>
#----> 1 my_tuple[1]=2
#TypeError: 'tuple' object does not support item assignment
