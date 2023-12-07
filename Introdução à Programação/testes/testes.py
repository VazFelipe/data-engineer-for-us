# # def minha_funcao(variavel: str) -> str:
# #     print(variavel)

# # variavel = 5
# # variavel_2 = 4

# # minha_funcao(variavel + variavel_2)

# lista_alternativas = ["As funções da calculadora são as seguintes:", "1: Soma", "2: Subtração", "3: Multiplicação", "4: Divisão", "0: Sair\n"]

# # mensagem = lista_alternativas.index("1")
# # mensagem = [alternativa for alternativa in lista_alternativas if "1" in alternativa]

# for alternativa in lista_alternativas:
#     if "1" in alternativa:
#         mensagem = alternativa
# print(mensagem)

# # for alternativa in lista_alternativas:
# #         print(alternativa)
# #         if alternativa.index("1"):
# #             mensagem = alternativa
# #             print(mensagem)

# indice = len(plantas)

# for i in range(indice):
#     print("Rega a planta " + str(plantas[i]))


# teste fim
# plantas = ["tomate","batata","batata","tomate","tomate","batata"]
# contador = 0
# max_plantas = len(plantas)

# while True:
#     mensagem = f'Rega a planta {plantas[contador]}'
#     print(mensagem)
#     contador += 1

#     if contador == max_plantas:
#         break

# teste início
# while contador < max_plantas:
#     mensagem = f'Rega a planta {plantas[contador]}'
#     print(mensagem)
#     contador += 1

# regar somente tomates
# teste início
# while contador < max_plantas:
    
#     if plantas[contador] == "tomate":
#         mensagem = f'Rega a planta {contador} {plantas[contador]}'
#         print(mensagem)    
    
#     contador += 1

# teste fim
# while True:

#     if plantas[contador] == "tomate":
#         mensagem = f'Rega a planta {contador} {plantas[contador]}'
#         print(mensagem)
#         break
    
#     contador += 1

# def adicao(numero_1, numero_2):
#     soma = int(numero_1) + int(numero_2)
#     return soma

# resultado_soma = adicao(numero_1=1, numero_2=1)
# print(resultado_soma)


# def subtracao(numero_1, numero_2):
#     subtracao = int(numero_1) - int(numero_2)
#     return subtracao

# resultado_subtracao = subtracao(numero_1=10, numero_2=4)
# print(resultado_subtracao)


# def divisao(numero_1, numero_2):
#     if numero_2 == "0" or numero_2 == 0:
#         return "no denominador não pode ser zero"
    
#     else:
#         divisao = int(numero_1) / int(numero_2)
#         return divisao

# resultado_divisao = divisao(numero_1=1, numero_2=0)
# print(resultado_divisao)


# indices = [1, 3]
# lista = ["tomate", "cebola", "maracujá", "cereja", "bolo"]

# nova_lista = []
# for item in range(len(lista)):
#     if item not in indices:
#         nova_lista.append(lista[item])

# lista = nova_lista
# print(lista)