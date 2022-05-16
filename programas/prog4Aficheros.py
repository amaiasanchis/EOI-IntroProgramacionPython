from random import randint
from prog2Aficheros import lee_o_crea_fichero_a_partir_de_una_lista as leer_escribir


ListaCiudades = ['Malaga','Alava','Albacete','Alicante','Almería','Asturias','Avila','Badajoz','Barcelona','Burgos','Cáceres','Cádiz','Cantabria','Castellón','Ceuta','Ciudad Real','Córdoba','Cuenca','Formentera','Girona']
dicc = {}

for ciudad in ListaCiudades: 
    listatemperaturas = [] 
    for i in range(0,12): 
        temperaturas = randint(0,50) 
        listatemperaturas.append(temperaturas) 
    dicc[ciudad] = listatemperaturas 

file = 'DatosProg4.txt'

leer_escribir(file,dicc)