# Hacer un programa que procese 100 mujeres y hombres (M/H).  
# Mostrar el porcentaje de hombres y mujeres y si hay más mujeres que hombres, 
# si hay igualdad o si hay más hombres que mujeres. |
from random import randint

#simulamos una muestra aleatoria de 100 personas
personas = []
for i in range(1,101):
    genero = (randint(0,1))
    if genero == 1:
        personas.append('H')
    else: 
        personas.append('M')
print(personas)

#guardamos eso en un fichero
from os.path import exists

file = 'DatosProg1.txt'
if exists(file):
    print('Fichero previamente generado, no se sobreescribe')
    fichero = open(file,'rt',encoding = 'UTF-8')
    contenido = fichero.read()
    print(f'El contenido del fichero es {contenido}')
else: 
    fichero = open(file,'wt',encoding = 'UTF-8')
    fichero.write(str(personas))

fichero.close()

