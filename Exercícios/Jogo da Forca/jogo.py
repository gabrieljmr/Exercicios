from palavra_chave import palavra
import random

letras_user = []
chances = 5
ganhou = False
palavra = random.choice(palavra)

print("Use apenas letras minúsculas :)")
while True:
    for letra in palavra:
        
        if letra.lower() in letras_user:
            print(letra, end=" ")

        else:
            print("_", end=" ")

    print("Você tem", chances, "chances !") 
    tentativa = input("Escolha uma letra: ")
    letras_user.append(tentativa.lower()) 
    if tentativa.lower() not in palavra.lower():
        chances -= 1
    
    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_user:
            ganhou = False

    if chances == 0 or ganhou:
        break 

if ganhou:
    print("Você Ganhou! Parabéns :) A palavra era:" , palavra  )
else:
    print("Você pedeu :( Tente novamente! A palavra era:" , palavra )    
