from random import randint

#hacemos una lista con genero (F/M) y edad (0-120)
#cada elemento de la lista es un diccionario del tipo
# {'gender': 'F', 'age': 65}
dataset = list({"gender": "F" if randint(0, 1) == 0 else "M","age": randint(0, 120),} for _ in range(100))

#print(dataset)

#mujeres mayores de edad
mujeres_mayores = len(
    [
        person
        for person in dataset
        if person["gender"] == "F" and person["age"] >= 18
    ]
    )
print(f"Número de mujeres mayores de edad: {mujeres_mayores}")

#hombres menores de edad
hombres_menores = len(
    [
        person
        for person in dataset
        if person["gender"] == "M" and person["age"] < 18
    ]
    )
print(f"Número de hombres menores de edad: {hombres_menores}")

#edad del hombre menor
hombres_menor_edad = min(
    [person['age'] 
    for person in dataset 
    if person['gender'] == 'M'
    ]
)
print('edad hombre menor',hombres_menor_edad)

#edad mujer mayor 
mujeres_mayor_edad = max(
    [person['age'] 
    for person in dataset 
    if person['gender'] == 'F'])
print('edad mujer mayor', mujeres_mayor_edad)

#total hombres y mujeres
total_hombres = len([person for person in dataset if person['gender']=='M'])

total_mujeres = 100 - total_hombres

#promedio edad
#primero hacemos el sumatorio de edades de hombres y mujeres
hombres_suma_edades = sum([person['age'] for person in dataset if person['gender']=='M'])
mujeres_suma_edades = sum([person['age'] for person in dataset if person['gender']=='F'])

print(f'promedio edad hombres:{hombres_suma_edades/total_hombres}')
print(f'promedio edad mujeres:{mujeres_suma_edades/total_mujeres}')

