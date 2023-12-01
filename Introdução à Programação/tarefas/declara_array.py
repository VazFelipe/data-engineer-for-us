def main():
    lista_array()

def lista_array():
    produtos_loja_bebidas = input("Digite separado por espacos os produtos da loja de bebidas: ")
    ano_nascimento_familiares = input("Digite separado por espacos os anos de nascimento dos seus familiares: ")

    lista_produtos_loja_bebidas = produtos_loja_bebidas.split()
    lista_ano_nascimento_familiares = ano_nascimento_familiares.split()

    print(f'Produtos da loja de bebidas: tipo {type(lista_produtos_loja_bebidas)}, valor {lista_produtos_loja_bebidas}')
    print(f'Anos de nascimento dos familiares: tipo {type(lista_ano_nascimento_familiares)}, valor {lista_ano_nascimento_familiares}')

main()