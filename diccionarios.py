dict = {"red":"rojo","blue":"azul","green":"verde"}
print("diccionario inicial",dict)
#anadir elemento
dict["black"]="negro"
print("dict + negro",dict)
#quitar elemento
dict.pop("green")
print("dict - verde",dict)

#usamos diccionario
print("Red en castellano",dict["red"])
print("Blue en castellano",dict["blue"])

#recorremos 
for key in dict:
    print(key,'->',dict[key])