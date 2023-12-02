def main():
    programa()

def programa():
    """
    Função que imprime os músicos presentes em uma lista e chama a função imprime_indices.

    A função percorre a lista de músicos e imprime o índice e o nome de cada músico.
    Em seguida, chama a função imprime_indices passando a lista de músicos como argumento.

    Parâmetros:
    - Nenhum

    Retorno:
    - Nenhum
    """
    lista_musicos = ['Djavan', 'Roberto Carlos', 'Elis Regina', 
                     'Tom Jobim', 'Milton Nascimento', 'Chico Buarque', 
                     'Nara Leão', 'Pitty', 'Simonal', 
                     'Moacir Santos', 'Caetano Veloso', 'Elza Soares', 
                     'Paulinho da Viola', 'Yamandú Costa', 'Gal Costa\n']
    print('\n')
    for i in range(len(lista_musicos)):
        print(f'{i} - {lista_musicos[i]}')
    
    imprime_indices(lista_musicos)

def imprime_indices(lista):
    """
    Imprime os elementos da lista de acordo com os índices fornecidos.

    Args:
        lista (list): A lista de elementos.

    Raises:
        IndexError: Se um índice inválido for fornecido.
        ValueError: Se um valor não inteiro for fornecido como índice.

    """
    tamanho_lista = len(lista)

    try:
        indices = input(f'Digite os índices desejados separados por espaço: ')
        indices = indices.split()
        for i in indices:
            print(lista[int(i)])
    except IndexError:
        print(f'Erro: índice inválido. A lista possui {tamanho_lista} elementos iniciando em 0 e terminando em {tamanho_lista-1}.')
    except ValueError:
        print(f'Erro: você não digitou um número inteiro. A lista possui {tamanho_lista} elementos iniciando em 0 e terminando em {tamanho_lista-1}.')

main()