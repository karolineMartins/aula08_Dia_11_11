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


#Exibir a quantidades de numeros digitados
print("Quantidades de numeros digitados:",len(numeros))

#Exibe a soma dos numeros digitado
print("Maior numero digitados.",max(numeros))
print("Maior numero digitados.",min(numeros))

#Exibe a soma dos numeros digitados
print("Soma dos numeros digitados.",sum(numeros))

#Exibe a media dos numeros digitados
print("Media dos numeros digitados.",sum(numeros) / len(numeros))
