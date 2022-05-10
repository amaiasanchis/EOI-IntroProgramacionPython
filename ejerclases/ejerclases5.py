#Construir una clase simple desde cero. Ya se ha creado una instancia para usted y 
# los atributos de la instancia se incluyen dentro del print. Tome esas pistas y 
# con estos datos cree la clase.
# 6. ahora usará la función __ str __ para devolver una representación de cadena para la clase cuando sea necesario.

class Nobel:
    def __init__(self,categoria,ano,ganadore):
        self.category = categoria
        self.year = ano
        self.winner = ganadore

    def __str__(self):
        return ("{}, {}, {}".format(self.category, self.year, self.winner))


nq2019=Nobel("Chemistry", 2019, "John B. Goodenough")
print(nq2019.category, nq2019.year, nq2019.winner)

print(nq2019)