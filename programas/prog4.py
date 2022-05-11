#Hacer un programa que procese las temperaturas mensuales de 20 ciudades. 
# Deberá sacar cuál de las ciudades tiene en promedio anual la temperatura más alta y 
# cual la más baja. También deberá sacar la lista de las 20 ciudades con el promedio de 
# temperaturas anuales desde la más alta hasta la más baja.

from random import randint
from unicodedata import digit

#creamos un diccionario que asocie ciudades y promedio anual de temperatura
dicciudadtemp = {}
#creamos lista que almacene las temperaturas promedio
listapromedios= []
#bucle con 20 ciudades (indice)
for ciudad in range(1,21):

    #creamos una lista de temperaturas
    temperaturas = []
    #bucle con 12 iteraciones, una por cada mes
    for i in range(1,13):
        #anadimos a la lista uns temp mensual entre -5 y 40 aleatoria
        temperaturas.append(randint(-5,40))
    #print(temperaturas)
    #calculamos el promedio anual
    '''
    contador = 0
    for temperatura in temperaturas:
        contador += temperatura
    '''
    sumtemperaturas = sum([temperatura for temperatura in temperaturas])
    promedio = sumtemperaturas / len(temperaturas)
    listapromedios.append(promedio) #round(promedio,2)
    
    #print(promedio)
    #print(ciudad)

    #anadimos entrada al diccionario. key: ciudad. valor: temp promedio
    dicciudadtemp[ciudad] = promedio
#print(listapromedios)
#print(dicciudadtemp)

# ciudad con temp promedio mas alta y mas baja
'''
#ordenamos la lista de temp promedio
listapromedios.sort()
#print(listapromedios)
tempmayor = listapromedios[-1]
tempmenor = listapromedios[0]
#print(tempmayor, tempmenor)
'''
#opcion 1
tempmayor = max(dicciudadtemp.values()) 
tempmenor = min(dicciudadtemp.values()) 

#list(dicciudadtemp.keys())[list(dicciudadtemp.values()).index(tempmayor)]  -> 
#list(dicciudadtemp.values())::: hacemos una lista con los promedios
# [list(dicciudadtemp.values()).index(tempmayor)] ::: hallamos el indice de la mayor temperatura
# buscamos en las keys (ciudades) la correspondiente al indice
#listamos
print(f'\n La ciudad con el promedio anual mas ALTO es {list(dicciudadtemp.keys())[list(dicciudadtemp.values()).index(tempmayor)]} con un promedio de: {tempmayor} ºC')

print(f'\n La ciudad con el promedio anual mas BAJO es {list(dicciudadtemp.keys())[list(dicciudadtemp.values()).index(tempmenor)]} con un promedio de: {tempmenor} ºC \n') 

ciudad_max = max(dicciudadtemp,key=dicciudadtemp)
ciudad_min = min(dicciudadtemp,key=dicciudadtemp)

print(ciudad_max,ciudad_min)

'''
#lista de ciudades ordenadas por temperatura promedio anual (de mas a menos)
print('Ciudades ordenadas por temperatura promedio anual')
listapromedios.sort(reverse=True)
for valor in listapromedios:
    print(f'Ciudad: {dicciudadtemp[valor]}, temperatura {round(valor,2)}')
'''