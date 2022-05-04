colores = ['azul','blanco','verde']
print(colores)

colores.append('rosa')
colores.insert(2,'violeta')
print(colores)

#eliminar valor
try:
    color = input("Inserte color a eliminar: ")
    colores.remove(color)
    print(colores)
except ValueError:
    print("El color no esta en la lista")

#saber posicion
try:
    col = input("Inserte color para saber su posicion: ")
    print(colores.index(col))
except ValueError:
    print("El color no esta en la lista")

#unir listas
colores2 = ['gris', 'negro','rosa']
colores.extend(colores2)
print("union de listas",colores)

#ordenar elementos
colores.sort()
print("lista ordenada alfabeticamente",colores)

#pop
colores.pop(3)
print("Eliminamos tercerelemento",colores)

#reverse
colores.reverse()
print("orden descendente",colores)

colores.sort(reverse=True)
print("orden descendente",colores)