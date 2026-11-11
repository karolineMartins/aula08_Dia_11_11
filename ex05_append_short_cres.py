#Inserir nomes e mostrar em ordem alfabetica - lista

nomes = []
for i in range (3):
    nome = input("Digitar um nome: ")
    nomes.append(nome)

nomes.sort()
print("Nomes em ordem alfabetica:", nomes)
