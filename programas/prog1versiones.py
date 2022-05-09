def ClasificaGenero(dataset, _len=100):
    """
    Función que calcula el % de hombres y mujeres
    El dataset debe ser una lista que contiene "F" para mujeres y "M" para hombres (de tamaño 100 por defecto)
    Devuelve False si el dato no es correcto (e imprime el motivo)
    """

    # Check Type, comprobamos que sea una lista
    if type(dataset) != list:
        print("Dataset is not a list")
        return False

    # Check Len
    if len(dataset) != _len:
        print("Wrong dataset size (must be) 100")
        return False

    #comprobar que en la lista solo hay 'F' y 'M'
    uniq_values = set(dataset) # pasamos a set para eliminar duplicidades
    if uniq_values != {"F", "M"}:
        print("Values must")
        return False

    #calcular porcentajes
    # no hombres es la longitud de una lista en la que incluye M
    n_hombres = len([gender for gender in dataset if gender == "M"])
    p_hombres = n_hombres / _len * 100
    p_mujeres = 100 - p_hombres

    print(f"Hay {p_hombres}% de hombres y {p_mujeres}% mujeres")

    #comparar y determinar si hay mas hombres, mujeres o igual
    if p_hombres > 50:
        print("Hay más hombres")

    elif p_hombres < 50:
        print("Hay más mujeres")

    else:
        print("Hay igualdad")

    return True


def TestHombresMujeres():
    stars = "***********************"

    print(stars)
    print("CASO aleatorio")
    datasetHombresMujeres = ["M" if random.randint(0, 1) else "F" for _ in range(100)]

    ClasificaGenero(datasetHombresMujeres)

    print(stars)
    print("CASO de Igualdad")
    datasetHombresMujeres = list("M" * 50 + "F" * 50)
    ClasificaGenero(datasetHombresMujeres)

    print(stars)

    print("CASO Dataset No es Lista")
    ClasificaGenero(4)

    print(stars)

    print("CASO Dataset Corto")

    ClasificaGenero(["F", "M"])

    print(stars)

    print("CASO Dataset no contiene F/M")
    ClasificaGenero(range(100))

    print(stars)


#version 2
from random import randint



# En este programa, procesa las mujeres como 0 y los hombres como 1

lista = []

for i in range(0,100):
    lista.append(randint(0,1))

print(f"El porcentaje de mujeres es del: {lista.count(0)}%")

print(f"El porcentaje de hombres es del: {lista.count(1)}%")

if(lista.count(0) > lista.count(1)):
    print("Hay más mujeres que hombres")

elif(lista.count(0) == lista.count(1)):
    print("Hay igualdad")

else:
    print("Hay más hombres que mujeres")

respuesta = input("¿Quieres ver el total de los datos? ").lower()

if respuesta == 'si' or respuesta == 'sí' or respuesta == 's' or respuesta == 'yes' or respuesta == 'y':

    print("\nMujeres: {}".format(lista.count(0)))

    print("Hombres: {}".format(lista.count(1)))

    print("Lista: {}".format(lista))

    print("Total de personas: {}".format(len(lista)))

#version 3
'''github.com/TMSamuel/IntroProgramacionPython/blob/main/LISTAS/Ejercicio1.py'''
#version con inputs