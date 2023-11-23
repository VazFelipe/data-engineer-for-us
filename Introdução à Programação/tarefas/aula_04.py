
# exercício 1
print("Exercício 1")
bebida_favorita = "cerveja de trigo"
bebida_preco = 5.99
indica_alcoolica = True

print(bebida_favorita, type(bebida_favorita), sep=" , ")

print(bebida_preco, type(bebida_preco), sep=" , ")

print(indica_alcoolica, type(indica_alcoolica), sep=" , ")

# exercício 2
print("Exercício 2")
almoco_favorito = "churrasco"
almoco_preco = 79
orçamento = 70

print("Meu orçamento é", orçamento)
print("Meu almoço foi " + almoco_favorito + " e custou " + str(almoco_preco), sep=", ")
print("O saldo após o almoço é", orçamento - almoco_preco)

# Exercício 3

print("Exercício 3")
indica_amigo_dinheiro = False

if orçamento >= almoco_preco:
    print("Posso pagar o almoço")
elif indica_amigo_dinheiro:
    print("Pedir ajuda ao amigo")
else:
    print("Lavar a louça no restaurante")