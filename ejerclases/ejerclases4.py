#Agregue otro atributo llamado "cantidad" al 
# método de inicialización (generalmente denominado
#  constructor o init).
# Luego defina "asignar" este atributo al atributo
#  self.quantity dentro del constructor.
# Luego cree 2 instancias para: F14 y Mirage2000
#  con cantidades 87 y 35.

class Jets:
    model = None
    country = 0

    def __init__(self, name, cantidad, country='?'):
        self.name = name
        self.origin = country
        self.quantity = cantidad
    
    def __str__(self):
        return "{}, {}, {}".format(self.name, self.quantity, self.origin)

#Escriba su respuesta aquí.        
first_item= Jets('F14',87)
second_item= Jets('Mirage2000',35)
total= [str(first_item), str(second_item)]
print(total)