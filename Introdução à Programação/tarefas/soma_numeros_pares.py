def operacao():
     operacao = int(input('Digite a função desejada: '))
     if (operacao == 1):
        return operacao    

def soma_pares(operacao):
    
    operacao = operacao()

    if operacao == 1:
        soma = 0

        for numero in range(1,101):
            if not numero % 2:
                soma += numero
        print(soma)
    else:
        print('esta operação ainda não foi criada')

soma_pares(operacao)