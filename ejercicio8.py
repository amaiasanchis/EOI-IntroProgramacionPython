#8. Crear un algoritmo que permita ingresar un 
# nombre y una cantidad numérica para escribir este
#  nombre tantas veces como su cantidad ingresada.

#tomar el nombre
nombre = input("Escribe el nombre: ")
num = input("Escribe el numero: ")

#bucle en el que vamos desde num hasta 0, imprimiendo el num cada vez
#correccion de errores por si no es numerico
if num.isdigit():
    num = int(num)
    while num>0:
        print(nombre)
        num -= 1
else:
    print("Ingrese valor numerico")

#version 2
#con while para que se repita

while(True):
    #tomar el nombre
    nombre = input("Escribe el nombre ('fin' para finalizar): ")
    #condicion para acabar
    if (nombre=="fin"):
        print("Gracias por usar este programa")
        break
    #tomamos el numero
    num = input("Escribe el numero: ")

    #bucle en el que vamos desde num hasta 0, imprimiendo el num cada vez
    #correccion de errores 
    #por si el nombre no es una palabra, innecesario a mi gusto pero interesante para practicar
    if (not nombre.isdigit()): 
        if num.isdigit():
            num = int(num)
            while num>0:
                print(nombre)
                num -= 1
        else:
            print("Ingrese valor numerico")
    else: 
        print("Ingrese un nombre adecuado")