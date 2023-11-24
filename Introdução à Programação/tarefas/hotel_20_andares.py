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
  qtd_andares_hotel = input('Digite a quantidade de andares do hotel: ')
  supersticao = input('Digite o andar supersticioso: ')
  imprimir_numero_hotel(qtd_andares_hotel, supersticao)

def imprimir_numero_hotel(qtd_andares_hotel, supersticao):
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

main()
