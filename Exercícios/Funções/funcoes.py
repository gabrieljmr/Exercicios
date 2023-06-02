def somaImposto(taxaImposto, custo):
    imposto = custo * (taxaImposto / 100)
    custo += imposto
    return custo

taxa = 10  
preco = 100 
preco_com_imposto = somaImposto(taxa, preco)
print("Preço com imposto:", preco_com_imposto)
