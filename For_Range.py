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


#Exemple 3 using yield to calculate Fibonacci
def fibonacci(n):
    a,b=0,1
    
    for _ in range(n):
        yield a
        a,b=b,a+b

n=int(input('Infomre um número para calcular a sequencia Fibonacci :'))
print(list(fibonacci(n)))


#Example 4 using list comprehension and zip
vetor_a= [1,5]
vetor_b=[2,6]

# Calcula o produto escalar entre os dois vetores
produto_escalar = sum(a * b for a, b in zip(vetor_a, vetor_b))
#print(set(zip(vetor_a, vetor_b))) #Usar o set para poder visualizar o resultado do zip

print(produto_escalar)
