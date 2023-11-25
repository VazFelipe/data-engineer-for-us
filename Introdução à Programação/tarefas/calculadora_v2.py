"""Pseudocódigo
Premissas
- O programa ficará rodando infinitamente até que o usuário escolha a opção sair
- As operações matemáticas serão escolhidas pelo usuário
- No início do programa será listado as operações matemáticas e a opção sair
    - 1: Soma, 2: Subtração, 3: Multiplicação, 4: Divisão, 0: Sair
    - O usuário irá digitar a alternativa desejada para que o programa realize o cálculo
    - Caso o usuário digite uma alternativa inexistente será mostrada a mensagem "Essa opção não existe"
        - O programa irá retornar ao início e apresentar novamente as alternativas
- Após escolher a operação matemática o programa irá solicitar que o usuário digite o primeiro e o segundo valor
    - Caso o usuário digite um dado diferente de inteiro ou real no primeiro ou segundo valor será solicitado novamente
    - No caso da divisão, se o usuário digitar no segundo valor um dado inteiro ou real igual a zero será solicitado novamente 
- Após o programa irá retornar em tela o resultado do cálculo e reiniciar
"""

def main():
  """
    Função principal que inicia a calculadora.
    Realiza as operações conforme a escolha do usuário.

    Argumentos:
    lista_alternativas (list): lista com as alternativas disponíveis de operações para o usuário
    """

  lista_alternativas = [
    "As funções da calculadora são as seguintes:", "1: Soma", "2: Subtração",
    "3: Multiplicação", "4: Divisão", "0: Sair"
  ]

  while True:
    iniciar_calculadora(lista_alternativas)
    entrada_usuario = input("\nDigite a sua alternativa [1, 2, 3, 4, 0]: ")

    if entrada_usuario != "0":
      escolher_funcao(entrada_usuario, lista_alternativas)
      print(digitar_numeros_calcular(entrada_usuario, lista_alternativas))
    elif entrada_usuario == "0":
      return print("\n0: Sair >> Obrigado por utilizar a Calculadora Versão 2")
    else:
      break


def iniciar_calculadora(lista_alternativas):
  """
    Mostra as opções disponíveis da calculadora.

    Argumentos:
    lista_alternativas (list): lista com as opções disponíveis para o usuário.
    """
  print("Esta é a Calculadora Versão 2\n")
  [print(alternativas) for alternativas in lista_alternativas]


def escolher_funcao(entrada_usuario, lista_alternativas):
  """
    Verifica se a entrada do usuário corresponde a uma das opções disponíveis.

    Argumentos:
    entrada_usuario (str): a alternativa selecionada pelo usuário.
    lista_alternativas (list): a lista de opções disponíveis para o usuário.
    """
  res_lista_alternativas = []
  for alternativa in lista_alternativas[1:5]:
    alternativa = alternativa[:1]
    res_lista_alternativas += alternativa

  while True:
    if entrada_usuario not in res_lista_alternativas:
      print("\nEssa opção não existe\n")
      main()
    else:
      break


def digitar_numeros_calcular(entrada_usuario, lista_alternativas):
  """
    Recebe a entrada do usuário, realiza cálculos com base nessa entrada e retorna o resultado.

    Argumentos:
    entrada_usuario (str): a escolha de operação matemática realizada pelo usuário.
    lista_alternativas (list): a lista de opções disponíveis para a escolha do usuário.

    Returno:
    mensagem (str): A mensagem contendo o resultado da operação.

    Exceção:
    ValueError: Se o usuário digitar um dado inválido.
    ZeroDivisionError: Se o usuário tentar dividir por zero.
    """
  for alternativa in lista_alternativas:
    if entrada_usuario in alternativa:
      alternativa_selecionada = alternativa
      alternativa_operacao = alternativa[2:].lower()

  print(alternativa_selecionada + "\n")

  mensagem = f'O resultado da operação de{alternativa_operacao} foi '

  while True:
    try:

      numero_1 = int(input("Digite o primeiro valor: "))
      numero_2 = int(input("Digite o segundo valor: "))

      if int(entrada_usuario) == 1:
        resultado = '{:.02f}'.format(numero_1 + numero_2)
        return "\n" + mensagem + str(resultado) + "\n"
      elif int(entrada_usuario) == 2:
        resultado = '{:.02f}'.format(numero_1 - numero_2)
        return "\n" + mensagem + str(resultado) + "\n"
      elif int(entrada_usuario) == 3:
        resultado = '{:.02f}'.format(numero_1 * numero_2)
        return "\n" + mensagem + str(resultado) + "\n"
      elif int(entrada_usuario) == 4:
        resultado = '{:.02f}'.format(numero_1 / numero_2)
        return "\n" + mensagem + str(resultado) + "\n"
    except ValueError:
      return "\nDigite números inteiros ou decimais, texto não é permitido. Tente novamente :)\n"
    except ZeroDivisionError:
      return "\nNa divisão o denominador não pode ser zero. Tente novamente :)\n"
    else:
      break

main()