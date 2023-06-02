def calcular_peso_ideal_homem(altura):
    peso_ideal_homem = (72.7 * altura) - 58
    return peso_ideal_homem

def calcular_peso_ideal_mulher(altura):
    peso_ideal_mulher = (62.1 * altura) - 44.7
    return peso_ideal_mulher

altura = float(input("Digite a altura da pessoa em metros: "))
sexo = input("Digite o sexo da pessoa (M para homem ou F para mulher): ")

if sexo.upper() == "M":
    peso_ideal = calcular_peso_ideal_homem(altura)
elif sexo.upper() == "F":
    peso_ideal = calcular_peso_ideal_mulher(altura)
else:
    print("Sexo inválido!")
    exit()

print(f"O peso ideal para uma pessoa com altura {altura} metros e sexo {sexo} é de {peso_ideal:.2f} kg.")
