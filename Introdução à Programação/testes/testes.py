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
plantas = ["tomate","banana","maça","melancia","abacate","laranja"]
contador = 0
max_plantas = len(plantas)

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
while contador < max_plantas:
    mensagem = f'Rega a planta {plantas[contador]}'
    
    
    if plantas[contador] == "tomate":
        print(mensagem)    
    
    contador += 1

# teste fim
while True:
    mensagem = f'Rega a planta {plantas[contador]}'

    if plantas[contador] == "tomate":
        print(mensagem)
        contador += 1
        break