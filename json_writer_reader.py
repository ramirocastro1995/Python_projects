import json

def jsonWriter():
    numeros = [2,4,10,12,16,22]
    archivo = 'numeros.json'
    with open(archivo, 'w') as archivoJson:
        json.dump(numeros,archivoJson)

def jsonReader():
    archivo = 'numeros.json'
    with open(archivo) as archivoJson:
        numeros = json.load(archivoJson)

    print(numeros)

jsonWriter()
jsonReader()