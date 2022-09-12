class Usuario():
    def __init__(self,nombre,apellido,dni,intentosLogin):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.intentosLogin = intentosLogin
    def aumentarLogin(self,intentos):
        self.intentosLogin += intentos


def main():
    login()


def login():
    print('ingresa tu nombre')
    nombreUsuario = input()
    print('ingresa tu apellido')
    apellidoUsuario = input()
    print('Ingresa tu DNI')
    dniUsuario = input()
    intentoLogin = 0
    if dniUsuario != '38826235':
        intentoLogin += 1
    
    usuarioA = Usuario(nombreUsuario,apellidoUsuario,dniUsuario,intentoLogin)



def testUsuario():
    usuarioTest = Usuario('Ramiro','Castro','38826235',0)
    print(usuarioTest.nombre)
    


testUsuario()