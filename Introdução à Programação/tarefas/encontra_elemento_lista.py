def main():
    busca_elemento_lista()

def busca_elemento_lista():
    """
    Função que permite ao usuário digitar uma lista de nomes e buscar por um nome específico na lista.

    A função solicita ao usuário que digite uma lista de nomes separados por espaços.
    Em seguida, solicita ao usuário que digite o nome que deseja buscar na lista.
    Se o nome estiver presente na lista, a função exibe a posição em que o nome foi encontrado.
    Caso contrário, exibe uma mensagem informando que o nome não foi encontrado na lista.

    Raises:
        ValueError: Se a lista de nomes ou o nome a ser buscado estiverem vazios.

    """
    try:
        lista_nomes = input("Digite uma lista de nomes separado por espaços: ").split(" ")
        while True:

            print(f'\nEsta é a lista que você digitou {lista_nomes}\n')
            
            nome_buscar = input("Digite o nome que deseja buscar: ")
            
            if len(lista_nomes) == 0 or len(nome_buscar) == 0:
                raise ValueError
            elif nome_buscar in lista_nomes:
                mensagem = f'\nO nome {nome_buscar} foi encontrado na posição {lista_nomes.index(nome_buscar)}.'
                print(mensagem)
                break
            else:
                mensagem = f'\nO nome {nome_buscar} não foi encontrado na lista. Tente novamente!'
                print(mensagem)
    except ValueError:
        mensagem = f'\nDigite pelo menos 1 nome para criar ou encontrar na lista.'
        print(mensagem)

main()