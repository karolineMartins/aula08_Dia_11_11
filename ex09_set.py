#Manipulação de conjuntos e Operacões Matematicas com Interação Dinamica

print("=== Conjunto A ===")
a = set()
while True:
    valor = input("Digite um numero para A (ou Enter pra para): ")
    if valor == "":
        break
    a.add(int(valor))

print("=== Conjunto B ===")
b = set()
while True:
    valor = input("Digite um numero para B (ou Enter pra para): ")
    if valor == "":
        break
    b.add(int(valor))

print("Conjunnto A:", a)
print("Conjunnto B:", b)

#Mostrando operaçaoes entre conjuntos
print("União", a | b)
print("Interseção:", a & b)