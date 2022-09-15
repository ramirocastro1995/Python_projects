import json

def usuarioAJSON():
    print('Ingresa tu nombre')
    usuario = input()
    archivo = 'user.json'
    with open(archivo, 'w') as datosUsuario:
        json.dump(usuario,datosUsuario)
    print('ya guardamos tu informacion!')

def getJSON():
    archivo = 'user.json'
    with open(archivo) as datosUsuario:
        usuario = json.load(datosUsuario)
    print(usuario)


usuarioAJSON()
getJSON()







