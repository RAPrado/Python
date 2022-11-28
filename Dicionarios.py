#Referência : https://openclassrooms.com

#Cria um dicionário com chave e valor
accounts = {'Marion Weaver': 10000, 'Alberto Mendoza': 150, 'Katharine Tyler': 300, 'Isaac Steele': 1800.74}
print(accounts['Alberto Mendoza']) # -> 150

#Manipula os valores
accounts['Marion Weaver'] -= 2000 # Subtrai 2000 do valor
accounts['Kristian Roach'] = 1000 # Adiciona uma nova chave e valor

#Deleta uma chave do dicionário
accounts.pop('Alberto Mendoza') # Deleta a chava

#Retorna o tamnho
len(accounts) # -> 3
