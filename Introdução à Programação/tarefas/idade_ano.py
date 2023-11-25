def main():
    """
    Chama a função idade_usuario e imprime o resultado.

    Retorna:
    Nenhum
    """
    print(idade_usuario())

def idade_usuario():
    """
    Solicita ao usuário seu nome completo e ano de nascimento.
    Solicita ao usuário o ano de referência para cálculo da idade. 
    
    Exceção:
    ValueError: Se os dados fornecidos não estiverem no formato esperado.
    
    Retorno:
    mensagem (str): Uma mensagem contendo o nome completo do usuário e sua idade calculada.
    """
    while True:
        try:                    
            entrada_dados = input("Digite seu nome completo e ano de nascimento com 4 números inteiros: ")
            ano_referencia = input("Digite o ano de referência com 4 números inteiros para cálculo da idade: ")
            ano_nascimento = int(entrada_dados[len(entrada_dados)-4:])
            ano_referencia = int(ano_referencia)
            nome_completo = entrada_dados[:-5]

            idade = ano_referencia - ano_nascimento
            mensagem = f'{nome_completo} {idade}' 
        except ValueError:
            print(f'{ValueError}: Ops, algo deu errado. Digite novamente, por exemplo: Meu Nome 2000')
        else:
            break
    return mensagem

main()