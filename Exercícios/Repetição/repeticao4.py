numero = int(input("Digite um número: "))

print(f"Tabuada do {numero}:")
for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")
