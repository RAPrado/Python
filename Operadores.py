#Referência : https://openclassrooms.com
#Operador de comparação
1 == 2 # -> False
3 != 2 # -> True
4 < 3  # -> False
2 > 3  # -> True
3 >= 3 # -> True
3 <= 3 # -> True

#Operador lógico
True and True # True
True and False # False
False and False # False
True or False # True
True or True # True
False or False # False
not(True) # False
not(False) # True

#Operador in
myList = [4, 2, 3, 2, 10]
myStringList = ["a", "b", "c", "d"]
myString = "The weather is really good today!"

4 in myList # True
0 in myList # False
0 in myStringList # False
"c" in myStringList # True
"e" in myStringList # False
"weather" in myString # True
"really" in myString # True
"rain?" in myString # False
