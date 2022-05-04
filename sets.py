
ciudades = {'Madrid','Valencia','Burgos','Sevilla','Vigo'}
print(ciudades)

#anadir elementos
ciudades.add('Gijon')
ciudades.add('Valencia') # no lo añade porque ya esa en la coleccion
print("ciudades iniciales mas gijon",ciudades)
for ciudad in ciudades:
    print(ciudad)

#quitar elementos 
ciudades.discard('Madrid')
print("ciudades menos capital",ciudades)
