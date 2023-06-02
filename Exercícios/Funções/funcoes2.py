def contarDigitos(frase):
    quantidade_digitos = sum(char.isdigit() for char in frase)
    return quantidade_digitos

# Exemplo de uso da função
frase = input("Digite uma frase: ")
quantidade = contarDigitos(frase)
print("Quantidade de dígitos na frase:", quantidade)
