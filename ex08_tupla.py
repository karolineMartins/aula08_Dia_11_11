#Aplicação com tupla 

print("=== PARTE 1: Estatistica em Tupla numericas ==")

#Criando uma tupla com 5 numeros para descobrir o maior e o menor valor
numeros = (10, 4, 8, 2, 7)
print(f"Tupla de numeros:{numeros} ")
print("Maior numero: ",max(numeros))
print("Menor numero: ",min(numeros))

print("/n=== PARTE 2: Percorrendo uma Tupla com for ===")

#Criando uma Tupla de cores e mostrando os elementos um por um 
cores = ("Azul", "Vermelho", "Verde", "Amarelo")
print("Exibindo as cores das tuplas:")
for cor in cores:
    print(cor)

print("/n=== PARTE 3: Contanto Elementos (count) ===")

#contando quantas vazes um numero especifico aparecer na tupla
valores = (1, 2, 3, 4, 2, 5)
print(f"Tupla de Referencia? {valores}")
num = int(input("Digite um numero para contar na tupla: "))
print(f"O numero {num} aparece {valores.count(num)} vez(es).")

print("/n=== PARTE 4: Encontrando a Posiçao (index) ===")

#Buscando a posiçao (indice) de um elemento com validacao de segurança
letras = ("a", "b", "c", "d", "e")
print(f"Tupla de letras disponiveis: {letras}")
valor = input("Digite uma letra para descobrir a posiçao: ")

if valor in letras:
    print(f"Posição (indice) de letra '{valor}':",letras.index(valor))
else:
    print("Letra nao encontrado na tupla.")    