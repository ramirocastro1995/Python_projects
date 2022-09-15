nombreDeArchivo = 'prueba.txt'

def buscarCumpleañosPI():
    

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
    print('Ingresa tu cumpleaños con el siguiente formato: 951995')
    cumpleanios = input()
    return cumpleanios



#appending to a file
def append():
    with open(nombreDeArchivo,"a")as archivoObjeto:
        archivoObjeto.write('hola')
        archivoObjeto.write('chau')

append()

buscarCumpleañosPI()




