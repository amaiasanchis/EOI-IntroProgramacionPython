#saludar
def saludar(nombre):
    print(f'hola {nombre}, buenos dias')

saludar('Amaia')
saludar('Laura')


#suma de dos numeros
def sumar(a,b):
    return(a+b)

print(sumar(8,9))
print(sumar(8,-9))
print(sumar(6.8,0.9))

#anadir elementos a una lista
def addElemento(lista,elemento):
    try:
        lista.append(elemento)
        return True
    except AttributeError:
        return False


colores=['rojo','rosa','azul']
addElemento(colores,'amarillo')
addElemento(colores,'verde')
addElemento(colores,'violeta')
addElemento(colores,'magenta')

saludar(colores)

if (addElemento('hola','gris')): # equivalente a addEl... ==True
    print('Insertado color')
else:
    print('Color no insertado')