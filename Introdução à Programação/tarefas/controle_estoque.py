import sys
import time

def main():

    print(iniciar_programa())
    
    lista_produtos_padrao = ["abacaxi", "banana", "uva", "melancia", "manga", "amora", "carambola"]
    
    apresenta_funcoes(lista_produtos_padrao)

def iniciar_programa():
    mensagem = "Este é o controle de estoque V1."
    return mensagem

def apresenta_funcoes(lista_produtos_padrao):

    lista_funcoes = ["\nO programa tem as seguintes funções: ", "0 - definir_proprietario", "1 - listar_produtos", "2 - adicionar_produtos", "3 - substituir_produtos", "4 - remover_produtos", "5 - definir_lista", "6 - sair"]
    
    while True:
        try:
            for funcao in lista_funcoes:
                print(funcao)

            escolha_usuario = int(input("\nDigite em número inteiro a função desejada: "))

            if escolha_usuario > 6:
                raise ValueError
            elif escolha_usuario == 0:
                definir_proprietario()
                return apresenta_funcoes(lista_produtos_padrao)
            elif escolha_usuario == 1:
                listar_produtos(lista_produtos_padrao)
                return apresenta_funcoes(lista_produtos_padrao)
            elif escolha_usuario == 2:
                listar_produtos(lista_produtos_padrao)                
                adicionar_produtos(lista_produtos_padrao)
                return apresenta_funcoes(lista_produtos_padrao)
            elif escolha_usuario == 3:
                listar_produtos(lista_produtos_padrao)
                substituir_produtos(lista_produtos_padrao)
                return apresenta_funcoes(lista_produtos_padrao)
            elif escolha_usuario == 4:
                listar_produtos(lista_produtos_padrao)                
                remover_produtos(lista_produtos_padrao)
                return apresenta_funcoes(lista_produtos_padrao)
            elif escolha_usuario == 5:
                return "definir_lista"
            elif escolha_usuario == 6:
                sys.exit("Obrigado por usar o Controle de Estoque V1\n")        

        except ValueError:
            print("\nVocê digitou algo diferente de um número inteiro. Tente novamente!")
            continue
    

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
    
    print(mensagem) 

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

    mensagem = f'\nPronto! A nova lista de produtos em estoque é: {lista_produtos_padrao}'
    print(mensagem)
    
    return lista_produtos_padrao

def substituir_produtos(lista_produtos_padrao):
    
    lista_indice_substituir = input("\nDigite em número inteiro e separado por espaços qual o item da lista para substituir: ").split(" ")

    lista_para_substituir = []

    for produto in range(len(lista_produtos_padrao)):
        for indice in range(len(lista_indice_substituir)):
            	if produto == int(lista_indice_substituir[indice]):
                    lista_para_substituir.append(lista_produtos_padrao[produto])
        
    lista_produtos_substitutos = input(f'\nEsta lista {lista_para_substituir} será substituída por quais produtos? Digite-os separados por espaços: ').split(" ")
    
    for indice in range(len(lista_indice_substituir)):
        lista_produtos_padrao[int(lista_indice_substituir[indice])] = lista_produtos_substitutos[indice]

    lista_produtos_padrao.sort()
    
    listar_produtos(lista_produtos_padrao)

    mensagem = f'\nPronto! A nova lista de produtos em estoque é: {lista_produtos_padrao}'
    print(mensagem)
    
    return lista_produtos_padrao

def remover_produtos(lista_produtos_padrao):

    lista_indice_remover = input("\nDigite em número inteiro qual o item da lista para remover: ").split(" ")

    lista_para_remover = []

    for produto in range(len(lista_produtos_padrao)):
        for indice in range(len(lista_indice_remover)):
                if produto == int(lista_indice_remover[indice]):
                    lista_para_remover.append(lista_produtos_padrao[produto])

    lista_produtos_remover = f'\nEsta lista {lista_para_remover} será removida.'

    print(lista_produtos_remover)
    time.sleep(2)

    lista_indice_remover = [int(indice) for indice in lista_indice_remover]

    nova_lista_produtos_padrao = []
    for produto in range(len(lista_produtos_padrao)):
        if produto not in lista_indice_remover:
            nova_lista_produtos_padrao.append(lista_produtos_padrao[produto])

    lista_produtos_padrao = nova_lista_produtos_padrao

    lista_produtos_padrao.sort()
    
    listar_produtos(lista_produtos_padrao)

    mensagem = f'\nPronto! A nova lista de produtos em estoque é: {lista_produtos_padrao}'
    print(mensagem)
    
    return lista_produtos_padrao

main()