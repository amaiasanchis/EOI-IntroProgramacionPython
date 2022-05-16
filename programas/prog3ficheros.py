
from random import randint
#recuperamos la funcion del ejercicio 2
from prog2ficheros import lee_o_crea_fichero_a_partir_de_una_lista as leer_escribir

#print(f'Ejercicio 3: {__name__}')
genero = [randint(0,1) for i in range(1,101)]
mujeres = [randint(0,100) for g in genero if g==0]
hombres = [randint(0,100) for g in genero if g==1]


filechicos = 'DatosProg3Hombres.txt'
filechicas = 'DatosProg3Mujeres.txt'

leer_escribir(filechicos, hombres)
leer_escribir(filechicas, mujeres)
