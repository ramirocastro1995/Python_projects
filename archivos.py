def main():
    nombreDeArchivo = 'prueba.txt'

    with open(nombreDeArchivo) as texto:
        lineas = texto.readlines()
            
    for linea in lineas:
        print(linea.rstrip())

    textoString = ''
    for linea in lineas:
        textoString += linea.rstrip()

    print(textoString)
    print('cantidad de numeros de pi '+ str(len(textoString)))
    print(textoString[:10])
    cumpleanios = getCumpleanios()
    if cumpleanios in textoString:
        print('tu cumpleaños esta en Pi!')
    else:
        print('tu cumpleaños no esta en Pi!')


def getCumpleanios():
    print('ingresa tu cumpleaños: ')
    cumpleanios = input()
    return cumpleanios


main()





