#Exemple 1 using for range to calculate the fatorial
n=int(input('Infomre um número para calcular o seu fatorial :'))
fatorial=n

for i in range(n-1,1,-1):
    fatorial *= i

print('Fatorial:', fatorial)


#Exemple 2 using recursive call to calculate the fatorial
def fatorial(n):
    return 1 if n == 0 else n * fatorial(n-1)

n=int(input('Infomre um número para calcular o seu fatorial :'))
print('Fatorial:', fatorial(n))
