#Clase Padre
class Usuarios():
    def __init__(self,nombre,apellido,dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def describirUsuarios(self):
        print('Nombre : ' + self.nombre)
        print('Apellido : ' + self.apellido)
        print('DNI : ' + self.dni)

    def bienvenidaUsuario(self):
        print('Bienvenido ' + self.nombre)

#Clase Hija

class Admin(Usuarios):
    def __init__(self, nombre, apellido, dni):
        super().__init__(nombre, apellido, dni)
        self.privilegios = ['puede modificar usuarios','puede borrar posts']
    
    def mostrarPrivilegiosDeAdmin(self):
        print(self.privilegios)

#Clase Padre
class Auto():
    def __init__(self,marca,modelo,anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = 0

    def descripcionDeAuto(self):
        print('Este auto es de marca ' + self.marca)
        print ('Este auto es del modelo ' + self.modelo)
        print ('Este auto es del año ' + self.anio )
        print('Este auto tiene '+ str(self.kilometraje) + ' kilometros')
        
    def actualizar_kilometraje(self, km):
        self.kilometraje = km
    
    def incrementar_kilometraje(self,km):
        self.kilometraje += km

#Clase Hija
class AutoElectrico(Auto):
    def __init__(self, marca, modelo, anio):
        super().__init__(marca, modelo, anio)
        self.bateria = Bateria()

    def incrementar_kilometraje(self):
        print('este feature no esta para autos electricos')
    

#Crear una instancia de un atributo
class Bateria():
    def __init__(self,tamanio = 70):
        self.tamanio = tamanio

    def imprimirTamaniodeBateria(self):
        print('el tamaño de la bateria es' + str(self.tamanio))

    def definirAutoBateria(self):
        if self.tamanio < 100:
            print('Bateria chica')
        else:
            print('Bateria grande')


def testUsuarios():
    usuario = Usuarios('Ramiro','Castro','38826235')
    usuarioA = Usuarios('Junior','Corrado', '298465135')
    usuarioC = Admin('Pedro','Lampone','38826245')
    usuario.bienvenidaUsuario()
    usuario.describirUsuarios()
    usuarioA.bienvenidaUsuario()
    usuarioA.describirUsuarios()
    usuarioC.mostrarPrivilegiosDeAdmin()

def testAutos():
    autoA = Auto('Ford','Focus','2006')
    autoB = Auto('Ford','Fiesta','2008')
    autoC = AutoElectrico('Tesla','xxxx','2022')
    autoA.descripcionDeAuto()
    autoB.descripcionDeAuto()
    autoA.actualizar_kilometraje(23)
    autoA.descripcionDeAuto()
    autoA.incrementar_kilometraje(20)
    autoA.descripcionDeAuto()
    autoC.descripcionDeAuto()
    autoC.bateria.imprimirTamaniodeBateria()
    autoC.incrementar_kilometraje()
    autoC.bateria.definirAutoBateria()

testUsuarios()
testAutos()
    


        