def converter_fahrenheit_para_celsius(temperatura_fahrenheit):
    temperatura_celsius = 5 * ((temperatura_fahrenheit - 32) / 9)
    return temperatura_celsius

temperatura_fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
temperatura_celsius = converter_fahrenheit_para_celsius(temperatura_fahrenheit)

print(f"A temperatura em graus Celsius é: {temperatura_celsius:.2f}")
