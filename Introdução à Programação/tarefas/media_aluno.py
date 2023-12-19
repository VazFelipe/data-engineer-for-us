notas = [7, 6, 6]

denominador = len(notas)

numerador = 0
for nota in range(len(notas)):
    numerador += notas[nota]    

media = numerador / denominador 

if 4 <= media <= 6:
    mensagem = 'Recuperação'
elif media > 6:
    mensagem = 'Aprovado'
else:
    mensagem = 'Reprovado'

print(mensagem)