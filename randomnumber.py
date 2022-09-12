import random
numeroSecreto = random.randint(1,20)

def main():
    print('Adivina un numero,del 1 al 20')
    for instanciasUsadas in range(1,7):
        print('Adivina!')
        numeroJugador = int(input())
        if numeroJugador < numeroSecreto:
            print('Numero muy bajo!')
        elif numeroJugador > numeroSecreto:
            print('Numero muy alto!')
        else:
            break
    if numeroJugador == numeroSecreto:
        print('Excelente! Adivinaste!')

main()


