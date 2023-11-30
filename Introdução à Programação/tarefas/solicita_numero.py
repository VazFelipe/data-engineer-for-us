def main():
    programa()

def programa():
    """
    Função principal que solicita um número inteiro ao usuário e realiza algumas verificações.

    A função solicita um número inteiro ao usuário e realiza as seguintes verificações:
    - Se o número está entre zero e cem (inclusive);
    - Se o número é par;
    - Se o número é divisível por dois e três.

    Se todas as verificações forem verdadeiras, imprime a mensagem "Número entre zero e 100, que é par e divisível por 2 e 3."
    Se apenas a primeira e a segunda verificações forem verdadeiras, imprime a mensagem "Número entre zero e 100 e que é par."
    Se apenas a primeira verificação for verdadeira, imprime a mensagem "Número entre zero e 100."
    Caso contrário, não imprime nenhuma mensagem.

    Raises:
        ValueError: Se o usuário digitar algo diferente de um número inteiro.

    Returns:
        None
    """
    
    entrada_dados = input("Digite um número inteiro: ")

    while True:
        try:
            converte_inteiro = int(entrada_dados)
            if entre_zero_cem(converte_inteiro) and numero_par(converte_inteiro) and divisivel_dois_tres(converte_inteiro):
                print("Número entre zero e 100, que é par e divisível por 2 e 3.")
            elif entre_zero_cem(converte_inteiro) and numero_par(converte_inteiro):
                print("Número entre zero e 100 e que é par.")
            elif entre_zero_cem(converte_inteiro):
                print("Número entre zero e 100.")
                
        except ValueError:
            print("\nVocê digitou algo diferente de um número inteiro. Tente novamente!")
            break

def entre_zero_cem(numero):
    """
    Verifica se um número está entre zero e cem (inclusive).

    Args:
        numero (int): O número a ser verificado.

    Returns:
        bool: True se o número está entre zero e cem (inclusive), False caso contrário.
    """
    return 0 <= numero <= 100

def numero_par(numero):
    """
    Verifica se um número é par.

    Args:
        numero (int): O número a ser verificado.

    Returns:
        bool: True se o número é par, False caso contrário.
    """
    return numero % 2 == 0

def divisivel_dois_tres(numero):
    """
    Verifica se um número é divisível por dois e três.

    Args:
        numero (int): O número a ser verificado.

    Returns:
        bool: True se o número é divisível por dois e três, False caso contrário.
    """
    return numero % 2 == 0 and numero % 3 == 0

def entre_zero_cem(entrada_dados):
    if 1 <= entrada_dados <= 100:
        return True
    else:
        return False
    
def numero_par(entrada_dados):
    if (entrada_dados % 2) == 0:
        return True
    else:
        return False
    
def divisivel_dois_tres(entrada_dados):
    if (entrada_dados % 2) == 0 and (entrada_dados % 3) == 0:
        return True
    else:
        return False
    
main()