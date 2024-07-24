from math import comb

def gerar_traingulo_pascal(n):
    if n <= 0:
        raise ValueError("n deve ser um inteiro positivo")
    for i in range(n):
        linha = [comb(i,j) for j in range(i+1)]
        print(linha)

n = int(input("Insira seu número: "))
gerar_traingulo_pascal(n)