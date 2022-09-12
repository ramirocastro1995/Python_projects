class Perro():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def sentarse(self):
        print(self.nombre.title() + ' ahora esta sentado')

    def dar_una_vuelta(self):
        print(self.nombre.title() + ' da una vuelta')

class Gato():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def maullar(self):
        print(self.nombre.title() + ' ahora esta maullando')

    def comer(self):
        print(self.nombre.title() + ' ahora esta comiendo')



def Test():
    mi_perro = Perro('Dugg', 7)
    tu_perro = Perro('Greg', 6)
    mi_gato = Gato('Emiratos',4)
    print('El nombre de mi perro es '+ mi_perro.nombre.title())
    print('La edad de mi perro es de' + str(mi_perro.edad))
    mi_perro.sentarse()
    mi_perro.dar_una_vuelta()
    tu_perro.sentarse()
    tu_perro.dar_una_vuelta()
    print('El nombre de mi gato es ' + mi_gato.nombre.title())
    print('La edad de mi gato es ' + str(mi_gato.edad))
    mi_gato.comer()
    mi_gato.maullar()




Test()
