class Vehiculo:
    #metodo privado
    def __privado(self):
        #metodo supuestamente privado
        print('Soy privado')
    
    #metodo publico para acceder a __privado
    def metodo_publico(self):
        self.__privado()

g1 = Vehiculo()
#g1.__privado() no se puede acceder
g1._Vehiculo__privado()
g1.metodo_publico()

#property
class partner:
    def __init__(self):
        self._age = 0 

    def get_age(self):
        return self._age

    def set_age(self,a):
        if (a<10): #no admitir edades menores a 10
            raise ValueError('edad no permitida')
        self._age = a
    
    def del_age(self):
        del self._age
    
    age = property(get_age,set_age, del_age)

mark = partner()
mark.age = 45 #resuelve set
print(mark.age) #resuelve get


#herencia
class Persona:
    def __init__(self,nombres,apellidos):
        self.Nombres = nombres
        self.Apellidos = apellidos

class Alumno(Persona):
    Curso = None # le dice a la variable que aun no tiene valor
    def __init__(self,nombres,apellidos,curso):
        self.Curso = curso
        super().__init__(nombres,apellidos)


estudiante = Alumno('Ricardo', 'montalban', 'Azure Fndamentals')
print(f'{estudiante.Nombres} {estudiante.Apellidos} {estudiante.Curso}')

#polimorfismo
class Figura:
    def dibujar(self,nombre):
        print(f'Dibujando un: {nombre}')

class Triangulo(Figura):
    def __init__(self,nombre):
        self.nombre = nombre

class Cuadrado(Figura):
    def __init__(self,nombre):
        self.nombre = nombre

class Rectangulo(Figura):
    def __init__(self,nombre):
        self.nombre = nombre

def DibujarFigura(figura):
    figura.dibujar(figura.nombre)

triangulo = Triangulo('Triangulo verde')
cuadrado = Cuadrado('Cuadrado rojo')
rectangulo = Rectangulo('Rectangulo amarillo')

DibujarFigura(triangulo)
DibujarFigura(cuadrado)
DibujarFigura(rectangulo)
