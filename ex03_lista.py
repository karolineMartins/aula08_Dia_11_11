#o usuario escolhe a quantidade de vezes que vai testar a aplicação 
#o programa mostra todos os numeros digitados, depois numeros pares e numero pares 

#Lista vazia para armazenar os numeros
numeros = []

#Solicita ao usuario quantos numeros deseja digitar 
quantidade = int(input("Quantos numeros você quer digitar? "))

#Lê os numeros informados pelo usiario

for i in range (quantidade):
    numero = int(input(f"Digitar o {i+1} numero: "))
    numeros.append(numero)
    

print(f"Numeros digitados: {numeros}")

#Exibe apenas os numeros pares
for n in numeros:
    if n % 2 == 0:
        print(n)

#Exibe apenas os numeros impares
for n in numeros:
    if n % 2 != 0:
        print(n)