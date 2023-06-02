def calcular_salario_mensal(valor_hora, horas_trabalhadas):
    salario_mensal = valor_hora * horas_trabalhadas
    return salario_mensal

valor_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

salario_mensal = calcular_salario_mensal(valor_hora, horas_trabalhadas)

print(f"Seu salário mensal é de R${salario_mensal:.2f}")
