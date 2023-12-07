def main():

    print(iniciar_programa())
    
    print(definir_proprietario())
    
    lista_produtos_padrao = ["abacaxi", "banana", "uva", "melancia", "manga", "amora", "carambola"]
    
    listar_produtos(lista_produtos_padrao)

    # apresenta_funcoes()

    print(adicionar_produtos(lista_produtos_padrao))
    
    print(substituir_produtos(lista_produtos_padrao))

    print(remover_produtos(lista_produtos_padrao))


def iniciar_programa():
    mensagem = "Este é o controle de estoque V1.\n"
    return mensagem

def definir_proprietario():
    try:
        while True:

            proprietário = input("Digite o nome do proprietário da loja: ")

            if len(proprietário) > 0:
                proprietário
                break
            else:
                continue
    except ValueError:
        pass
    
    mensagem = f'\nOlá {proprietário}!'

    return mensagem 

def apresenta_funcoes():

    lista_funcoes = ["definir_proprieatrio", "listar_produtos", "adicionar_produtos", "substituir_produtos", "remover_produtos"]

    lista = [funcao for funcao in lista_funcoes]

    print(lista)

def listar_produtos(lista_produtos_padrao):

    print('\nAbaixo nossa lista de produtos em estoque:\n')

    lista_produtos_padrao.sort()

    for indice in range(len(lista_produtos_padrao)):
        print(f'{indice} - {lista_produtos_padrao[indice]}')

def adicionar_produtos(lista_produtos_padrao):
    
    lista_adicionar_produtos = input("\nPara adicionar produtos digite-os separados por espaços: ").split(" ")

    lista_produtos_padrao.extend(lista_adicionar_produtos)
    lista_produtos_padrao.sort()

    listar_produtos(lista_produtos_padrao)

    mensagem = f'\nA nova lista de produtos em estoque é: {lista_produtos_padrao}\n'


    return mensagem

def substituir_produtos(lista_produtos_padrao):
    
    lista_indice_substituir = input("Digite em número inteiro e separado por espaços qual o item da lista para substituir: ").split(" ")

    lista_para_substituir = []

    for produto in range(len(lista_produtos_padrao)):
        for indice in range(len(lista_indice_substituir)):
            	if produto == int(lista_indice_substituir[indice]):
                    lista_para_substituir.append(lista_produtos_padrao[produto])
                # TODO else:
        
    lista_produtos_substitutos = input(f'\nEsta lista {lista_para_substituir} será substituída por quais produtos? Digite-os separados por espaços: ').split(" ")
    
    for indice in range(len(lista_indice_substituir)):
        lista_produtos_padrao[int(lista_indice_substituir[indice])] = lista_produtos_substitutos[indice]

    lista_produtos_padrao.sort()
    
    listar_produtos(lista_produtos_padrao)

    mensagem = f'\nA nova lista de produtos em estoque é: {lista_produtos_padrao}\n'

    return mensagem

def remover_produtos(lista_produtos_padrao):

    lista_indice_remover = input("Digite em número inteiro qual o item da lista para remover: ").split(" ")

    lista_para_remover = []

    for produto in range(len(lista_produtos_padrao)):
        for indice in range(len(lista_indice_remover)):
                if produto == int(lista_indice_remover[indice]):
                    lista_para_remover.append(lista_produtos_padrao[produto])
                # TODO else:

    lista_produtos_remover = f'\nEsta lista {lista_para_remover} será removida.'

    print(lista_produtos_remover)

    lista_indice_remover = [int(indice) for indice in lista_indice_remover]
    print(lista_indice_remover)
    nova_lista_produtos_padrao = []
    for produto in range(len(lista_produtos_padrao)):
        if produto not in lista_indice_remover:
            nova_lista_produtos_padrao.extend(lista_produtos_padrao[produto])
            # lista_produtos_padrao = lista_produtos_padrao[produto]
    
    lista_produtos_padrao = nova_lista_produtos_padrao
    
    lista_produtos_padrao.sort()
    
    listar_produtos(lista_produtos_padrao)

    mensagem = f'\nA nova lista de produtos em estoque é: {lista_produtos_padrao}\n'

    return mensagem

main()