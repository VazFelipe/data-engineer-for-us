# def minha_funcao(variavel: str) -> str:
#     print(variavel)

# variavel = 5
# variavel_2 = 4

# minha_funcao(variavel + variavel_2)

lista_alternativas = ["As funções da calculadora são as seguintes:", "1: Soma", "2: Subtração", "3: Multiplicação", "4: Divisão", "0: Sair\n"]

# mensagem = lista_alternativas.index("1")
# mensagem = [alternativa for alternativa in lista_alternativas if "1" in alternativa]

for alternativa in lista_alternativas:
    if "1" in alternativa:
        mensagem = alternativa
print(mensagem)

# for alternativa in lista_alternativas:
#         print(alternativa)
#         if alternativa.index("1"):
#             mensagem = alternativa
#             print(mensagem)