def main():
    iniciar_programa()
    regar()

def iniciar_programa():
    alternativas_rega = ["\nEste é o programa de regar plantas!\n", "Regar batatas", "Regar tomates", "Regar plantas ao contrário", "Sair do programa\n"]
    numero_alternativas = len(alternativas_rega)
    contador = 0

    while contador < numero_alternativas:
        if contador == 0:
            print(alternativas_rega[contador])
            contador += 1
        else:
            print(f'Opção {contador}:', alternativas_rega[contador])
            contador += 1

def regar():

    escolha_usuario = input("Digite a opção desejada [1, 2, 3, 4]: ")
    if escolha_usuario == "1":
        regar_batatas()
    elif escolha_usuario == "2":
        regar_tomates()
    elif escolha_usuario == "3":
        regar_contrario()
    elif escolha_usuario == "4":
        return print("\nAté a próxima!")
    else:
        while True:
            print("Não temos esta opção. Tente novamente :)\n")
            regar()
            break  

def regar_batatas():
    batatas = ["tomate", "tomate", "tomate", "batata", "batata", "batata"]

    contador_total = 0
    print("\nO robô tem estas plantas para regar:")
    for legume in batatas:
        print(f'Planta {contador_total}:', legume)
        contador_total += 1

    contador_batatas = 0
    print("\nMas ele vai regar somente as batatas:")
    for i in range(len(batatas)):
        if batatas[i] == "batata":
            print(f'Planta {i}:', batatas[i])
            contador_batatas += 1

def regar_tomates():
    tomates = ["tomate", "tomate", "batata", "batata", "tomate", "batata"]

    contador_total = 0
    print("\nO robô tem estas plantas para regar:")
    for legume in tomates:
        print(f'Planta {contador_total}:', legume)
        contador_total += 1

    contador_tomates = 0
    print("\nMas ele vai regar somente os tomates:")
    for i in range(len(tomates)):
        if tomates[i] == "tomate":
            print(f'Planta {i}:', tomates[i])
            contador_tomates += 1

def regar_contrario():
    contrario = ["tomate", "batata", "cenoura", "tomate", "batata", "cenoura"]

    contador_total = 0
    print("\nO robô tem estas plantas para regar:")
    for legume in contrario:
        print(f'Planta {contador_total}:', legume)
        contador_total += 1

    contador_tomates = len(contrario)
    print("\nMas ele vai regá-las ao contrário:")
    for i in range(len(contrario)):
        print(f'Planta {len(contrario) - 1 - i}:', contrario[len(contrario) - 1 - i])
        contador_tomates -= 1

main()