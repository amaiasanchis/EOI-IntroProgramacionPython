#Construir una clase simple desde cero. Ya se ha creado una instancia para usted y 
# los atributos de la instancia se incluyen dentro del print. Tome esas pistas y 
# con estos datos cree la clase.

class Nobel:
    def __init__(self,categoria,ano,ganadore):
        self.category = categoria
        self.year = ano
        self.winner = ganadore


nq2019=Nobel("Chemistry", 2019, "John B. Goodenough")
print(nq2019.category, nq2019.year, nq2019.winner)
