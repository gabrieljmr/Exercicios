def reverso_numero(numero):
    reverso = int(str(numero)[::-1])
    return reverso

numero = int(input("Digite um número inteiro: "))
reverso = reverso_numero(numero)
print("Reverso do número:", reverso)
