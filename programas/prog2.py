#Hacer un programa que procese las edades de 100 personas. Deberá decir cuantas tienen más
#  de (≥18) y cuál es la persona con menor edad y cuál es la persona con mayor edad. 
# También deberá mostrar el porcentaje de edades de las 100 personas.


#simulamos una muestra aleatoria de 100 personas 
# (suponemos que todas las edades son igual de probables)
from random import randint
'''
listaedades = []
for i in range(1,101):
    listaedades.append(randint(0,125))
'''
listaedades = [randint(0,125) for i in range(1,101)]
#print(listaedades)

# cuantas personas tienen mas de 18 
'''
#generamos dos contadores
menores = 0
mayores = 0
#recorremos la lista y sumamos a cada contador segun la edad
for edad in listaedades:
    if edad >= 18:
        mayores += 1
    else:
        menores += 1
'''
#con listas de comprension
mayores = len([edad for edad in listaedades if edad >= 18])
menores = len([edad for edad in listaedades if edad < 18])

print(f"Hay {mayores} mayores de edad y {menores} menores de edad.")

#buscar a la persona de mayor y menor edad
print('La persona de mayor edad tiene {m} años y la de menor edad, {n} años'.format(m=max(listaedades),n=min(listaedades)))

#porcentaje de edades 

#prueba fallida con set
#creamos conjunto en el que tengamos una vez todas las edades presentes
'''conjedades = set()
for edad in listaedades:
    conjedades.add(edad)
print(conjedades)
'''
# creamos un diccionario
listaedades.sort()
#print(listaedades)
'''
diccedades = {}
#hacemos una entrada para cada edad y damos un valor inicial de 1. Si ya existe la clave, sumamos 1 al valor 
for edad in listaedades:
    if edad not in diccedades:
        diccedades[edad] = 1
    else:
        diccedades[edad] += 1

#otra version de bucle
for edad in listaedades:
    diccedades[edad] += 1
'''
diccedades = {edad:listaedades.count(edad) for edad in listaedades}
print(diccedades)

#sacamos cada edad y su porcentaje
print('Porcentaje edades:')
for key in diccedades:
    print(f'Edad: {key}, porcentaje: {diccedades[key]}%')