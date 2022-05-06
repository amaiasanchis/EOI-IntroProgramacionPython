#funciones que no necesitan argumentos
def ProcesoInicial():
    print('Hola Mundo')


#funciones en las que no sabemos el numero de paramentros (N parametros)
def SaludarATodes(*nombres):
    for i in nombres:
        print(f'Hola {i}')

#funcion con arg diccionario
def SaludarATodesDict(**nombres):
    for i in nombres:
        print(f'hola:{i} {nombres[i]}')

#funcion con parametro por defecto
def Ciudades(país='Noruega',ciudad='Oslo'):
    print(país, ' ', ciudad)


ProcesoInicial()
SaludarATodes('Rosa')
SaludarATodes('Marian','Pedro','Luisa')
SaludarATodes() #no da error pero no aparece nada
SaludarATodesDict(nombre="Amaia",apellidos="Sanchis")
SaludarATodesDict(Amaia='Sanchis')
Ciudades('España','Barcelona')
Ciudades()