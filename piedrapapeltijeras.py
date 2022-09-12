import random, sys


perdidas = 0
ganadas = 0
empatadas = 0

def main():
    while True:
        print('Piedra papel o tijera')
        movimientoJugador = eligeMovimientoJugador()
        movimientoMaquina = eligeMovimientoMaquina()
        jugada = definirJugada(movimientoJugador, movimientoMaquina)
        if jugada == ('Ganador'):
            ganadas = ganadas +1




def eligeMovimientoJugador():
    movimientoJugador = input()
    if movimientoJugador == 'PI':
        print('piedra contra...')
    elif movimientoJugador == 'PA':
        print('papel contra')
    elif movimientoJugador == 'TI':
            print('Tijeras contra..')
    return movimientoJugador

def eligeMovimientoMaquina():
    valor = ''
    movimientoMaquina = random.randint(1,3)
    if movimientoMaquina == 1:
        valor == 'TI'
        print('Tijera')
    elif movimientoMaquina == 2:
        valor == 'PA'
        print('Papel')
    elif movimientoMaquina == 3:
        valor == 'PI'
        print('Piedra')
    return valor
    
def definirJugada(movimientoJugador,movimientoMaquina):
    if movimientoJugador == movimientoMaquina :
        print('Empate!')
    elif movimientoJugador == 'PA' and movimientoMaquina == 'PI':
        print('Ganaste!')
        return('Ganador')
    elif movimientoJugador == 'PI' and movimientoMaquina == 'PA':
        print('Perdiste!')
        return('Perdedor')






main()