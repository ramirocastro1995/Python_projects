import random, sys

perdidas = 0
ganadas = 0
empatadas = 0

while True:
    print('Piedra papel o tijera')
    while True:
        print('%s Ganadas, %s Perdidas, %s empatadas' % (ganadas,perdidas,empatadas))
        movimientoJugador = input()
        print('ingresa tu movimiento (Pi)edra,(Pa)pel,(Ti)jera o (S)alir')
        if movimientoJugador == 'S':
            sys.exit()
        if movimientoJugador == 'PI':
            print('piedra contra...')
        elif movimientoJugador == 'PA':
            print('papel contra')
        elif movimientoJugador == 'TI':
            print('Tijeras contra..')
        
        