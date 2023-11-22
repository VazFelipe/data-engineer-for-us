"""
Desenvolva um algoritmo que utilize as seguintes características de um veículo:
- Quantidade de rodas
- Peso bruto em quilogramas
- Quantidade de pessoas no veículo

Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
A: Veículos com duas ou três rodas;
B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas; 
E: Veículos com quatro rodas ou mais e com mais de 6000 kg.
"""

def main():
    """Retorna a categoria desejada de acordo com as variáveis quantidade de rodas, peso bruto e quantidade de pessoas.
    """
    quantidade_rodas = int(input("Informe e quantidade de rodas em número inteiro: "))
    peso_bruto = int(input("Informe o peso bruto em número inteiro: "))
    quantidade_pessoas = int(input("Informe a quantidade de pessoas em número inteiro: "))

    if categoria_a(quantidade_rodas, peso_bruto, quantidade_pessoas):
        print("Categoria A", end="")
    elif categoria_b(quantidade_rodas, peso_bruto, quantidade_pessoas):
        print("Categoria B", end="")
    elif categoria_c(quantidade_rodas, peso_bruto, quantidade_pessoas):
        print("Categoria C", end="")
    elif categoria_d(quantidade_rodas, peso_bruto, quantidade_pessoas):
        print("Categoria D", end="")
    elif categoria_e(quantidade_rodas, peso_bruto, quantidade_pessoas):
        print("Categoria E", end="")
    else:
        print("Você atribuiu números inteiros que não se referem a nenhuma categoria entre A e E", end="")


def categoria_a(quantidade_rodas, peso_bruto, quantidade_pessoas):
    """
    Retorna verdadeiro se o veículo tiver duas ou três rodas.
    Desconsidera as variáveis peso bruto e quantidade de pessoas, mas elas precisam ter sido criadas.

    Argumentos:
        quantidade_rodas (int): quantidade de rodas do veículo
        peso_bruto (int): peso bruto do veículo
        quantidade_pessoas (int): quantidade de pessoas que o veículo acomoda

    Retorno:
        True or False: booleano quando a condição for aceita. 
    """
    quantidade_rodas = quantidade_rodas
    peso_bruto = peso_bruto
    quantidade_pessoas = quantidade_pessoas
    if peso_bruto != 0 or quantidade_pessoas != 0:
        if 2 <= quantidade_rodas <= 3:
            return True
    else:
        return False


def categoria_b(quantidade_rodas, peso_bruto, quantidade_pessoas):
    """
    Retorna verdadeiro se o veículo tiver quatro rodas, acomoda até oito pessoas e seu peso é de até 3500 kg.

    Argumentos:
        quantidade_rodas (int): quantidade de rodas do veículo
        peso_bruto (int): peso bruto do veículo
        quantidade_pessoas (int): quantidade de pessoas que o veículo acomoda

    Retorno:
        True or False: booleano quando a condição for aceita. 
    """
    quantidade_rodas = quantidade_rodas
    peso_bruto = peso_bruto
    quantidade_pessoas = quantidade_pessoas
    if quantidade_rodas == 4 and peso_bruto <= 3500 and quantidade_pessoas <= 8:
        return True
    else:
        return False


def categoria_c(quantidade_rodas, peso_bruto, quantidade_pessoas):
    """
    Retorna verdadeiro se o veículo tiver quatro rodas ou mais e o peso entre 3500 e 6000 kg.
    Desconsidera a variável quantidade de pessoas, mas ela precisa ter sido criada.

    Argumentos:
        quantidade_rodas (int): quantidade de rodas do veículo
        peso_bruto (int): peso bruto do veículo
        quantidade_pessoas (int): quantidade de pessoas que o veículo acomoda

    Retorno:
        True or False: booleano quando a condição for aceita. 
    """
    quantidade_rodas = quantidade_rodas
    peso_bruto = peso_bruto
    quantidade_pessoas = quantidade_pessoas
    if quantidade_pessoas != 0:
        if quantidade_rodas >= 4 and 3500 <= peso_bruto <= 6000:
            return True
    else:
        return False


def categoria_d(quantidade_rodas, quantidade_pessoas, peso_bruto):
    """
    Retorna verdadeiro se o veículos tiver quatro rodas ou mais e acomoda mais de oito pessoas.
    Desconsidera a variável peso bruto, mas ela precisa ter sido criada.

    Argumentos:
        quantidade_rodas (int): quantidade de rodas do veículo
        peso_bruto (int): peso bruto do veículo
        quantidade_pessoas (int): quantidade de pessoas que o veículo acomoda

    Retorno:
        True or False: booleano quando a condição for aceita. 
    """
    quantidade_rodas = quantidade_rodas
    quantidade_pessoas = quantidade_pessoas
    peso_bruto = peso_bruto
    if peso_bruto != 0:
        if quantidade_rodas >= 4 and quantidade_pessoas <= 8:
            return True
    else:
        return False


def categoria_e(quantidade_rodas, peso_bruto, quantidade_pessoas):
    """
    Retorna verdadeiro se o veículo tiver quatro rodas ou mais e com mais de 6000 kg.
    Desconsidera a variável quantidade de pessoas, mas ela precisa ter sido criada.

    Argumentos:
        quantidade_rodas (int): quantidade de rodas do veículo
        peso_bruto (int): peso bruto do veículo
        quantidade_pessoas (int): quantidade de pessoas que o veículo acomoda

    Retorno:
        True or False: booleano quando a condição for aceita. 
    """
    quantidade_rodas = quantidade_rodas
    peso_bruto = peso_bruto
    quantidade_pessoas = quantidade_pessoas
    if quantidade_pessoas != 0:
        if quantidade_rodas >= 4 and peso_bruto > 6000:
            return True
    else:
        return False

main()