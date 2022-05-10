
#el molde Persona se puede utilizar para crear 
#distintos tipos de objetps (ej. profesor, alumno, admin)


class Persona:
    # los atributos los creamos en la funcion constructor
    #Nombres=""
    #Apellidos = ""

    #las clases pueden contener funciones

    #funcion constructor 
    def __init__(self,nombre,apellidos):
        self.Nombres = nombre
        self.Apellidos = apellidos

    def __str__(self):
        return '{} {}'.format(self.Nombres,self.Apellidos)

    def caminar(n):
        print('caminando')

#creamos distintos objetos
#profesor
profesor = Persona('Billy', 'Vanegas')
#si no tenemos funcion constructor
#profesor = Persona()
#profesor.Nombres= "Billy" #setter
#profesor.Apellidos= "Vanegas" #setter

#alumno
alumno = Persona('Olga','Sanchez')
#alumno.Nombres = 'Olga'
#alumno.Apellidos = 'Sanchez'

#administrativo
administrativo = Persona('Maria','Lopez')
#administrativo.Nombres = 'Maria'
#administrativo.Apellidos = 'Lopez'

print('El profesor {} {}'.format(profesor.Nombres, profesor.Apellidos))
print('La alumna {} {}'.format(alumno.Nombres, alumno.Apellidos))
print('La administrativa {} {}'.format(administrativo.Nombres, administrativo.Apellidos))

print('El alumno: ', alumno) # si no establecemos la funcion str propia, python da la respuesta 
#<__main__.Persona object at 0x0000025B0A0CBB20>, debido al metodo str que esta incluido en la variable alumno



profesor.caminar()

