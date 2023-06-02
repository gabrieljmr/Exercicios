def calculo1(num_int1, num_int2):
    produto = (2 * num_int1) * (num_int2 / 2)
    return produto

def calculo2(num_int1, num_real):
    soma = (3 * num_int1) + num_real
    return soma

def calculo3(num_real):
    cubo = num_real ** 3
    return cubo

num_int1 = int(input("Digite o primeiro número inteiro: "))
num_int2 = int(input("Digite o segundo número inteiro: "))
num_real = float(input("Digite o número real: "))

produto = calculo1(num_int1, num_int2)
soma = calculo2(num_int1, num_real)
cubo = calculo3(num_real)

print(f"O produto do dobro do primeiro com metade do segundo é: {produto}")
print(f"A soma do triplo do primeiro com o terceiro é: {soma}")
print(f"O terceiro elevado ao cubo é: {cubo}")
