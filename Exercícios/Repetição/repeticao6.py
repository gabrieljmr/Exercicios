
convidados = ["Brad Pitt", "Jennifer Aniston", "Leonardo DiCaprio", "Angelina Jolie", "Tom Hanks"]

print("== Envio dos Convites ==")
convite = "Olá {nome}, você está convidado para um jantar em minha casa no próximo sábado. Será um prazer tê-lo(a) conosco!"
for convidado in convidados:
    convite_personalizado = convite.format(nome=convidado)
    print(convite_personalizado)

nao_pode_comparecer = ["Leonardo DiCaprio"]

print("\n== Alteração dos Convites ==")
for convidado in nao_pode_comparecer:
    print(f"{convidado} não poderá comparecer ao jantar.")
    convidados.remove(convidado)

novos_convidados = ["Chris Hemsworth", "Emma Watson"]
convidados.extend(novos_convidados)

print("\n== Novos Convites ==")
for convidado in convidados:
    convite_personalizado = convite.format(nome=convidado)
    print(convite_personalizado)
