# Hacer un programa que procese 100 mujeres y hombres (M/H).  
# Mostrar el porcentaje de hombres y mujeres y si hay más mujeres que hombres, 
# si hay igualdad o si hay más hombres que mujeres. |
from random import randint

#simulamos una muestra aleatoria de 100 personas
#para ello, creamos una lista con 0 (chica) y 1 (chico) aleatorios
listaaleatoria = []
for i in range(1,101):
    listaaleatoria.append(randint(0,1))
#print(listaaleatoria)

#mostrar porcentaje de hombres y mujeres
#para ello, contamos cuantos hombres y cuantas mujeres hay
'''
numhombres = 0
nummujeres = 0 
for num in listaaleatoria:
    if num == 0:
        nummujeres +=1
    else:
        numhombres += 1
 '''
numhombres = listaaleatoria.count(1)
nummujeres = listaaleatoria.count(0)
#print('mujeres:',nummujeres,'hombres:',numhombres)


# y calculamos el porcentaje
print(f'Porcentaje de mujeres: {nummujeres}% y porcentaje de hombres: {numhombres}%')

#mostrar si hay mas mujeres, mas hombres o igualdad

if nummujeres > numhombres:
    print('Hay mas mujeres que hombres')
elif nummujeres == numhombres:
    print('Hay igual numero de mujeres que de hombres')
else: 
    print('Hay mas hombres que mujeres')


