from time import sleep

def main():
  rest_time = input("Digite o tempo de descanso em segundos: ")
  rest_at_gym(rest_time)

from time import sleep

def rest_at_gym(rest_time):
  """
  Perform a rest routine at the gym.

  Parameters
  ----------
  rest_time : int
    The total time for the rest routine in seconds.

  Returns
  -------
  None

  Notes
  -----
  This function alternates between expiration and inspiration exercises
  for the specified rest time. It prints the current count and waits for
  1 second between each exercise. After the rest routine is completed,
  it prints a message indicating the start of the workout series.

  Examples
  --------
  >>> rest_at_gym(10)
  Inspire 1
  Expire 2
  Inspire 3
  Expire 4
  Inspire 5
  Expire 6
  Inspire 7
  Expire 8
  Inspire 9
  Expire 10
  Iniciar a série! bom trabalho :)
  """
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
