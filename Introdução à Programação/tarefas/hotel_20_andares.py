def main():
  """ 
  Função principal que realiza a entrada de dados.
  Chama a função imprimir_numero_hotel().
  Imprime os números do hotel em ordem descrescente e desconsidera o andar supersticioso.

  Argumentos
  ----------
  qtd_andares_funcao (str) : quantidade de andares do hotel.
  supersticao (str) : número do andar supersticioso.

  Retorno
  -------
  Número do andar em ordem descrescente desconsiderando o andar supersticioso.
  
  """
  laco_repeticao = input('Digite ou while ou for para o laço de repetição: ')
  qtd_andares_hotel = input('Digite a quantidade de andares do hotel: ')
  supersticao = input('Digite o andar supersticioso: ')
  if laco_repeticao == 'while':
    imprimir_numero_hotel_while(qtd_andares_hotel, supersticao)
  else:
    imprimir_numero_hotel_for(qtd_andares_hotel, supersticao)

def imprimir_numero_hotel_while(qtd_andares_hotel, supersticao):
  """ 
  Função que imprime os números dos andares do hotel, excluindo o andar supersticioso.

  Argumentos
  ----------
  qtd_andares_hotel (str) : quantidade de andares do hotel.
  supersticao (str) : número do andar supersticioso.
  contador (int) : contador de andares do hotel.

  Retorno
  -------
  Número do andar em ordem descrescente desconsiderando o andar supersticioso.
  """
  contador = int(qtd_andares_hotel) + 1
  while True:
    contador -= 1
    if contador == int(supersticao):
      continue 
    elif contador == 0:
      break
    else:
      print(contador)

def imprimir_numero_hotel_for(qtd_andares_hotel, supersticao):
  """ 
  Função que imprime os números dos andares do hotel, excluindo o andar supersticioso.

  Argumentos
  ----------
  qtd_andares_hotel (str) : quantidade de andares do hotel.
  supersticao (str) : número do andar supersticioso.
  contador (int) : contador de andares do hotel.

  Retorno
  -------
  Número do andar em ordem descrescente desconsiderando o andar supersticioso.
  """
  for contador in range(int(qtd_andares_hotel), 0, -1):
    if contador != int(supersticao):
      print(contador)

main()
