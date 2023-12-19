import random
import sys

def main():
    adivinhar()

def numero_maximo():

    while True:
        try:
            maximo = int(input("Digite um número inteiro máximo para tentar adivinhar: "))

            if maximo < 0:
                raise ValueError
            else:
                numero_aleatorio = random.randint(1,maximo)
                break
        except ValueError:
            continue

    return numero_aleatorio

def adivinhar():

    numero_aleatorio = numero_maximo()

    while True:
        try:
            chute = int(input("Chute: "))

            if chute < 0:
                raise ValueError
            if chute == numero_aleatorio:
                sys.exit("GOOOOOOOOOOLLLLL!")
            elif chute <= numero_aleatorio:
                print("Chute baixo!")
            else:
                print("Chute alto!")
        except ValueError:
            continue

main()