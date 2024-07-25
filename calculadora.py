numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite um segundo número: "))
operacao = int(input("Insira a sua operação. 1 para soma, 2 para subtração, 3 para divisão e 4 para multiplicação: "))

match operacao:
  case 1:
    print(f"{numero1} + {numero2} = {numero1 + numero2}")
  case 2:
    print(f"{numero1} - {numero2} = {numero1 - numero2}")
  case 3:
    print(f"{numero1} / {numero2} = {numero1/numero2}")
  case 4:
    print(f"{numero1} x {numero2} = {numero1 * numero2}")
  case _:
    print("Insira uma operação válida.")


