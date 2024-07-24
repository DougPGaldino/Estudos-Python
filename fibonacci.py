def fibonacci_loop(n):
    if n < 1:
        raise ValueError("n deve ser maior ou igual a 1")

    sequencia = [0,1]
    for i in range(2, n):
        sequencia.append(sequencia[i-1] + sequencia[i-2])
    return sequencia

n = int(input("Insira o numero de termos: "))
sequencia_fibonacci = fibonacci_loop(n)
print(f"Sequência de Fibonacci até o {n} termo: {sequencia_fibonacci}")
    