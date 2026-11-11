#Inserir nomes e mostrar em ordem descrecente - lista

nomes = []
for i in range (3):
    nome = input("Digitar um nome: ")
    nomes.append(nome)

# ordena em ordem alfabetica decrescente
nomes.sort(reverse=True)
print("Nomes em ordem alfabetica decrescente:", nomes)