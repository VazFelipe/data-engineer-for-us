def main():
    """
    Função principal que exibe uma mensagem de boas-vindas e lista os produtos disponíveis na loja de cosméticos.
    """
    lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 
    
    print('\nBem-vindo(a) à loja de cosméticos!\n')
    print('Aqui você encontra os melhores produtos de beleza!\n')
    print('Confira a lista de produtos disponíveis:\n')
    
    lista_novos_produtos(lista_produtos)
    
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

main()