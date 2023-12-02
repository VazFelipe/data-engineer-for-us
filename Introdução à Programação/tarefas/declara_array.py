def main():
    """
    Função principal que solicita ao usuário a entrada de produtos da loja de bebidas e anos de nascimento dos familiares.
    Em seguida, chama a função lista_array() para processar e exibir as listas de entrada.
    """
    produtos_loja_bebidas = input("Digite separado por espaços os produtos da loja de bebidas: ")
    ano_nascimento_familiares = input("Digite separado por espaços os anos de nascimento dos seus familiares: ")
    print(lista_array(produtos_loja_bebidas, ano_nascimento_familiares))

def lista_array(produtos_loja_bebidas, ano_nascimento_familiares):
    """
    Função que recebe duas strings contendo produtos da loja de bebidas e anos de nascimento dos familiares,
    e retorna uma string formatada com informações sobre as listas de entrada.

    Args:
        produtos_loja_bebidas (str): String contendo os produtos da loja de bebidas separados por espaços.
        ano_nascimento_familiares (str): String contendo os anos de nascimento dos familiares separados por espaços.

    Returns:
        str: String formatada com informações sobre as listas de entrada.
    """
    lista_produtos_loja_bebidas = produtos_loja_bebidas.split()
    lista_ano_nascimento_familiares = ano_nascimento_familiares.split()

    lista_1 = f'Produtos da loja de bebidas: tipo {type(lista_produtos_loja_bebidas)}, valor {lista_produtos_loja_bebidas}'
    lista_2 = f'Anos de nascimento dos familiares: tipo {type(lista_ano_nascimento_familiares)}, valor {lista_ano_nascimento_familiares}'

    lists = f'{lista_1}\n{lista_2}' 
    return lists

main()