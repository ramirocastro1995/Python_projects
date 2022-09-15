class Usuario():
    def __init__(self,nombre,apellido,dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def descripcionNombreUsuario(self):
        print('tu nombre es' + self.nombre)
        
class CasosDeTestUsuarios():
    def testNombre():
        
        nombre1 = Usuario.descripcionNombreUsuario('Ramiro')
        print(nombre1)

CasosDeTestUsuarios.testNombre()
