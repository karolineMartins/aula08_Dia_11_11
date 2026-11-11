#Inserir nome, mostre em ordem descrescente e remover - lista


nomes = []
for i in range (3):
    nome = input("Digitar um nome: ")
    nomes.append(nome)

# ordena em ordem alfabetica decrescente
nomes.sort(reverse=True)
print("Nomes em ordem alfabetica decrescente:", nomes)

nome_remover = input("Digite o nome que deseja remover: ")
nomes.remove(nome_remover)

print("Nomes:", nomes)