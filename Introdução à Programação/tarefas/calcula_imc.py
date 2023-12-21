def main():
    peso, altura = entrada_usuario()
    calculo = calcula_imc(peso, altura)
    print(define_classificacao(calculo))


def entrada_usuario():
    # 1 o usuario vai informar o peso e a altura
    peso = int(input("informar peso em quilos: "))
    altura = float(input("informar altura: "))
    return peso, altura

def calcula_imc(peso, altura):
    # 2 calcula o imc ( peso / (altura*2)  )
    calcula_altura = altura * altura
    calculo = peso / calcula_altura
    return round(calculo, 2)

def define_classificacao(calculo):
    # 3 retorna condicao de acordo com o resultado
    if 0 <= calculo <= 18.59:
        mensagem = "Abaixo do peso"
    elif 18.60 <= calculo <= 24.99:
        mensagem = "Normal"
    elif 25 <= calculo <= 29.99:
        mensagem = "Sobrepeso"
    elif 30 <= calculo <= 39.99:
        mensagem = "Obesidade"
    else:
        mensagem = "Obesidade grave"
    
    return mensagem, calculo

main()