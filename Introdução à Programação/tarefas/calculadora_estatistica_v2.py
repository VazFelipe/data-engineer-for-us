# quantidade de elementos, soma e média dos números

numeros = [25, 32, 72, 24, 60, 10]

quantidade = 0
soma = 0

minimo = numeros[0]
maximo = numeros[0]

for numero in numeros:
    quantidade = quantidade + 1
    soma += numero

    if numero < minimo:
      minimo = numero
    elif numero > maximo:
      maximo = numero

media = round(soma / quantidade, 2)

for i in range(0, len(numeros)):
    for j in range(i+1, len(numeros)):
        if numeros[i] >= numeros[j]:
            numeros[i], numeros[j] = numeros[j],numeros[i]


print(quantidade, soma, media, minimo, maximo)
print(numeros)