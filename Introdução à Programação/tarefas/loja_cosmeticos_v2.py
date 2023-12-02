def main():
    """
    Função principal que exibe uma mensagem de boas-vindas e lista os produtos disponíveis na loja de cosméticos.
    """
    lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']

    print('\nBem-vindo(a) à loja de cosméticos!\n')
    print('Aqui você encontra os melhores produtos de beleza!\n')
    print('Confira a lista atualizada de produtos disponíveis:\n')
    
    lista_atualizada_produtos(lista_produtos)
    
    print('\nAgradecemos a preferência!\n')


def lista_novos_produtos(lista_produtos):
    """
    Imprime os novos produtos disponíveis para venda.

    Args:
        lista_produtos (list): Uma lista contendo os produtos disponíveis.

    Returns:
        None
    """
    tamanho_lista = len(lista_produtos)
    contador = 0
    while contador < tamanho_lista:
        print(f'Temos {lista_produtos[contador]} à venda!')
        contador += 1

def lista_atualizada_produtos(lista_produtos):
    """
    Atualiza a lista de produtos removendo os produtos indesejados e substituindo outros.

    Args:
        lista_produtos (list): A lista de produtos a ser atualizada.

    Returns:
        None
    """
    lista_atualizada_produtos = ["rímel", "cremes hidratantes"]
    lista_remover_produtos = ["delineadores"]

    tamanho_lista = len(lista_produtos)

    contador = 0
    while contador < tamanho_lista:
        if lista_produtos[contador] in lista_remover_produtos:
            lista_produtos.pop(contador)
        elif lista_produtos not in lista_atualizada_produtos:
            if lista_produtos[contador] == "batons":
                lista_produtos[contador] = "**"+lista_atualizada_produtos[0]+"**"
            elif lista_produtos[contador] == "loções":
                lista_produtos[contador] = "**"+lista_atualizada_produtos[1]+"**"
        contador += 1
    
    novos_produtos = input("Se preferir, digite novos produtos separados por espaço: ").split()
    lista_produtos.extend(novos_produtos)

    for produto in range(len(lista_produtos)):
        print(f'Temos {lista_produtos[produto]} à venda!')
        contador += 1

main()