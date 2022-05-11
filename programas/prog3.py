#Hacer un programa que procese un total de 100 personas y establecer cuantas son mujeres 
# mayores de edad y cuantos hombres menores de edad. Deberá sacar el hombre y la mujer 
# con menor edad, el hombre y la mujer con mayor edad, promedio de edades de las mujeres 
# y promedio de edades de los hombres.
from random import randint
'''
#generamos un set aleatorio de cien personas (hombres(1) y mujeres (0)) con edades aleatorias
#entre 0 y 100 años
listamujeres = []
listahombres = []

# 100 personas
for i in range(1,101):
    # genero
    genero = randint(0,1)
    # edad
    edad = randint(0,100)
    # creamos una lista de mujeres y otra de hombres
    if genero == 0: 
        listamujeres.append(edad)
    else: 
        listahombres.append(edad)

#print(listamujeres, listahombres)
'''
#pasamos lo anterior a listas de comprension
# mujeres y hombres aleatorios en 100 personas
genero = [randint(0,1) for i in range(1,101)]
#lista de edades entre 0 y 100 anos mujeres
listamujeres = [randint(0,100) for g in genero if g==0]
#lista de edades entre 0 y 100 anos hombres
listahombres = [randint(0,100) for g in genero if g==1]



# porcentaje por generos
print(f'Mujeres: {len(listamujeres)}% y hombres:{len(listahombres)}% ')


#mujeres mayores de edad
'''
mujeresmayores = 0 
for edad in listamujeres:
    if edad >= 18:
        mujeresmayores += 1
'''
mujeresmayores = [edad for edad in listamujeres if edad >= 18]

print(f"Hay {len(mujeresmayores)} mujeres mayores de edad")

#hombres menores de edad
'''
hombresmenores = 0 
for edad in listahombres:
    if edad < 18:
        hombresmenores += 1
'''
hombresmenores = [edad for edad in listahombres if edad < 18]
print(f"Hay {len(hombresmenores)} hombres menores de edad")

#hombre y mujer de mayor y menor edad
def mayormenor(lista,genero):
    mayoredad = max(lista)
    menoredad = min(lista)
    print(f'{genero} de mayor edad tiene {mayoredad} años y de menor edad, {menoredad} años')

mayormenor(listamujeres, 'Mujer')
mayormenor(listahombres, 'Hombre')

# promedio edad mujeres y promedio edad hombres
def promedioedad(lista, genero):
    '''
    contadoredad = 0
    for edad in lista:
        contadoredad += edad
    '''
    contadoredad = sum([edad for edad in lista])
    promedio = contadoredad / len(listamujeres)
    print("Edad promedio en {g}: {p:1.2f} años".format(g= genero,p=promedio))


promedioedad(listamujeres,'mujeres')
promedioedad(listahombres,'hombres')

