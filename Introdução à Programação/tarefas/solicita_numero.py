def main():
    programa()

def programa():
    
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