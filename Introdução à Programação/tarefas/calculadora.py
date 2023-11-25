def main():
    """
    Solicita a operação matemática e números inteiros maiores que zero.
    Imprime o resultado da operação.
    
    Argumentos:
    - operacao (str): A operação matemática a ser realizada.
    - numero_1 (int): O primeiro número inteiro maior que zero.
    - numero_2 (int): O segundo número inteiro maior que zero.

    Retorno:
    - Resultado da operação.
    
    Exceção:
    - ValueError: Se os números informados não forem válidos.
    """
    operacao = input('Informe o nome da operação matemática: ')
    
    while True:
        try:
            numero_1 = int(input('Digite um número inteiro maior do que zero: '))
            numero_2 = int(input('Digite outro número inteiro maior do que zero: '))
            print(calculadora(numero_1, numero_2, operacao))
        except ValueError:
            print('Você digitou um valor inválido.')
        else:
            break
def calculadora(numero_1, numero_2, operacao):
    """
    Realiza uma operação matemática com dois números e retorna o resultado.

    Argumentos:
    - numero_1 (int): O primeiro número para a operação.
    - numero_2 (int): O segundo número para a operação.
    - operacao (str): A operação a ser realizada. 
      - Pode ser 'soma', 'subtração', 'multiplicação' ou 'divisão'.

    Retorno:
    - int: O resultado da operação matemática.

    Exceção:
    - ValueError: Se os números informados não forem válidos.
    """
    try:
        numero_1 = int(numero_1)
        numero_2 = int(numero_2)

        if operacao.lower() == 'soma':
            return int(numero_1) + int(numero_2)
        elif operacao.lower() == 'subtração':
            return int(numero_1) - int(numero_2)
        elif operacao.lower() == 'multiplicação':
            return int(numero_1) * int(numero_2)
        elif operacao.lower() == 'divisão':
            while True:
                try:
                    return int(numero_1) / int(numero_2)
                except ZeroDivisionError:
                    numero_2 = int(input('Digite outro número inteiro maior do que zero: '))
                    print('Não é possível dividir um número por zero.')
                else:
                    break
        else:
            return 0
    except ValueError:
        return 0

main()
