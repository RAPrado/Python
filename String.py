#Example 1
a="Teste de codigo"
print(a.lower()) #Resultado: teste de codigo
print(a.upper()) #Resultado: TESTE DE CODIGO
print(a.capitalize()) #Resultado: Teste de codigo
print(a.replace('e','a')) #Resultado: Tasta da codigo
print(a.find('de')) #Resultado: 6


#Example 2 - Getting specifics position in a string
data="10/dezembro/2023"

posicao=data.find('/')
dia = data[0:2]           #Get 2 left positions
mes = data[posicao+1:-5]  #Get the month, starting after de bar position, minus the last 5 positions
ano = data[-4:]           #Get 4 right positions

print(dia) #Resulsato : 10
print(mes) #Resulsato : dezembro
print(ano) #2023
