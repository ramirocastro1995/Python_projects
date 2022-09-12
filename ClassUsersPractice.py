
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



    

def testUsuarios():
    usuario = Usuarios('Ramiro','Castro','38826235')
    usuarioA = Usuarios('Junior','Corrado', '298465135')
    usuario.bienvenidaUsuario()
    usuario.describirUsuarios()
    usuarioA.bienvenidaUsuario()
    usuarioA.describirUsuarios()

def testAutos():
    autoA = Auto('Ford','Focus','2006')
    autoB = Auto('Ford','Fiesta','2008')
    autoA.descripcionDeAuto()
    autoB.descripcionDeAuto()
    autoA.actualizar_kilometraje(23)
    autoA.descripcionDeAuto()



testUsuarios()
testAutos()
    


        