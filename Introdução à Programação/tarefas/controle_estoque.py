def main():

    print(iniciar_programa())
    
    print(definir_proprietario())
    
    lista_produtos_padrao = ["abacaxi", "banana", "uva", "melancia", "manga", "amora", "carambola"]
    
    listar_produtos(lista_produtos_padrao)

    # apresenta_funcoes()

    print(adicionar_produtos(lista_produtos_padrao))
    # substituir_produtos()


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
    
    mensagem = f'\nOlá {proprietário}!\n'

    return mensagem 

def apresenta_funcoes():

    lista_funcoes = ["definir_proprieatrio", "listar_produtos", "adicionar_produtos", "substituir_produtos", "remover_produtos"]

    lista = [funcao for funcao in lista_funcoes]

    print(lista)

def listar_produtos(lista_produtos_padrao):

    print('Abaixo nossa lista de produtos em estoque:\n')

    lista_produtos_padrao.sort()

    for indice in range(len(lista_produtos_padrao)):
        print(f'{indice} - {lista_produtos_padrao[indice]}')

def adicionar_produtos(lista_produtos_padrao):
    
    lista_adicionar_produtos = input("\nPara adicionar produtos digite-os separados por espaços: ").split(" ")

    lista_produtos_padrao.extend(lista_adicionar_produtos)
    lista_produtos_padrao.sort()

    mensagem = f'\nA nova lista de produtos em estoque é: {lista_produtos_padrao}\n'

    return mensagem
        
main()