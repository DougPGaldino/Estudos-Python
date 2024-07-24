print("Converta sua temperatura em Celsius para Fahrenheit e Kelvin")
tempC = float(input("Digite a temperatura: "))
tempF = (tempC * 9/5) + 32
tempK = tempC + 273.15

print(f"Sua temperatura em Fahrenheit é de: {tempF}")
print (f"Sua temperatura em Kelvin é de: {tempK}")

print("Converta sua temperatura de Fahrenheit para Kelvin")
tempK = float(input("Digite a temperatura em Fahrenheit: "))
tempFF = (tempK - 32) * 5/9 + 273.15
print(f"Sua temperatura em Fahrenheit para Kelvin: {tempFF}")