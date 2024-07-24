cont = 1
lista = []
while cont <= 10:
    numero = int(input("Digite um número: "))
    lista.append(numero)
    cont = cont + 1

lista.sort()
print(lista)