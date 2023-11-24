from time import sleep

def main():
  rest_time = input("Digite o tempo de descanso em segundos: ")
  rest_at_gym(rest_time)

def rest_at_gym(rest_time):
  counter = 0
  while counter < int(rest_time):
    counter += 1
    if counter % 2 == 0:
      print(f'Expire {counter}')
      sleep(1)
    else:
      print(f'Inspire {counter}')
      sleep(1)
  print('Iniciar a série! bom trabalho :)')

main()
