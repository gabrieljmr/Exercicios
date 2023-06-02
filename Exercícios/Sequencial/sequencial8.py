def calcular_peso_ideal(altura):
    peso_ideal = (72.7 * altura) - 58
    return peso_ideal

altura = float(input("Digite a altura da pessoa em metros: "))
peso_ideal = calcular_peso_ideal(altura)

print(f"O peso ideal para uma pessoa com altura {altura} metros é de {peso_ideal:.2f} kg.")
