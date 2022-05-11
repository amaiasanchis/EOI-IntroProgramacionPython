#Hacer un programa que procese las temperaturas mensuales de 20 ciudades. Deberá sacar cuál de las ciudades tiene en promedio anual la temperatura más alta y cual la más baja.
#También deberá sacar la lista de las 20 ciudades con el promedio de temperaturas anuales desde la más alta hasta la más baja.

from random import randint

ListaCiudades = ['Malaga','Alava','Albacete','Alicante','Almería','Asturias','Avila','Badajoz','Barcelona','Burgos','Cáceres','Cádiz','Cantabria','Castellón','Ceuta','Ciudad Real','Córdoba','Cuenca','Formentera','Girona']
dicc = {}
# Recorremos la lista de ciudades # Creamos o "Reseteamos" la lista de temperaturas en cada recorrido del bucle, 
# para que sean diferentes en cada ciudad.

for ciudad in ListaCiudades: 
    listatemperaturas = [] 
    for i in range(0,12): 
        # Generamos temperaturas comprendidas entre 0 y 50ºC
        temperaturas = randint(0,50) 
        #Almacenamos las temperaturas en una lista.
        listatemperaturas.append(temperaturas) 
    #Almacenamos en un diccionario el nombre de la ciudad junto a una lista con las temperaturas de 
    # enero a diciembre (12)
    dicc[ciudad] = listatemperaturas 

DiccPromedioAnual={} 

# Recorremos el diccionario. items permite recorrer este diccionario
for clave,valor in dicc.items(): 
    # Mostramos en pantalla los nombres de la ciudad junto a la lista de temperatura de todo el año
    print(f'{clave} -> {valor}') 

    # Creamos una tupla con los valores del diccionario
    tuplatemperaturas = tuple(valor) 
    # Hacemos una media de las temperaturas anuales de cada ciudad
    MediaAnuales = (round(sum(tuplatemperaturas)/12 ,2)) 
    # Creamos un nuevo diccionario con la ciudad y la temperatura media anual.
    DiccPromedioAnual[clave] = MediaAnuales 


# Almacenamos el valor maximo del promedio anual
MaxProAnual = max(DiccPromedioAnual.values()) 
# Almacenamos el vlaor minimo del promedio anual
MinProAnual = min(DiccPromedioAnual.values()) 

#Convertimos a lista las claves y valores del diccionario para posteriormente hacer una busqueda del valor del prom max anual.
print(f'\n La ciudad con el promedio anual mas ALTO es {list(DiccPromedioAnual.keys())[list(DiccPromedioAnual.values()).index(MaxProAnual)]} con un promedio de: {MaxProAnual} ºC')

#Convertimos a lista las claves y valores del diccionario para posteriormente hacer una busqueda del valor del prom min anual.
print(f'\n La ciudad con el promedio anual mas BAJO es {list(DiccPromedioAnual.keys())[list(DiccPromedioAnual.values()).index(MinProAnual)]} con un promedio de: {MinProAnual} ºC \n') 
'''
#Convertimos el diccionario en una lista
ListaPromedioAnual = list(DiccPromedioAnual.items()) 

# Ordenamos la lista de mayor a menor
ListaPromedioAnual.sort(key = lambda x: x[1], reverse=True) 
'''
ListaPromedioAnual = sorted(DiccPromedioAnual,key=DiccPromedioAnual.get,reverse=True)
print(f'La lista de las ciudades ordenadas es :\n{ListaPromedioAnual}')

