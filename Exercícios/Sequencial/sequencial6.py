def converter_celsius_para_fahrenheit(temperatura_celsius):
    temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32
    return temperatura_fahrenheit

temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))
temperatura_fahrenheit = converter_celsius_para_fahrenheit(temperatura_celsius)

print(f"A temperatura em graus Fahrenheit é: {temperatura_fahrenheit:.2f}")
