#Cree nuevas instancias hasta el sexto elemento 
# siguiendo este orden: F14, SU33, AJS37, 
# Mirage2000, Mig29, A10.
# Puede tener en cuenta que los orígenes son:
# F14: USA 
# SU33: Russia 
# AJS37: Sweden 
# Mirage2000: France 
# Mig29: USSR 
# A10: USA

class Jets:
    model = None
    country = 0

    #funcion constructora
    def __init__(self, name, country):
        self.name = name
        self.origin = country
    
    def __str__(self):
        return "{} -> {}".format(self.name, self.origin)


#Escriba su respuesta aquí.        
first_item= Jets('F14','USA')
second_item= Jets('SU33','Russia')
third_item=  Jets('AJS37','Sweden')
fourth_item= Jets('Mirage2000','France')
fifth_item= Jets('Mig29','USSR')
sixth_item= Jets('A10','USA')

first_army=[first_item.name,second_item.name,third_item.name,fourth_item.name,fifth_item.name,sixth_item.name]
print(first_army)
# modificar para que quede name->country,

#first_army_country = [first_item,second_item,third_item,fourth_item,fifth_item,sixth_item]
#print(first_army_country) ::::: [<__main__.Jets object at 0x00000194E25CBC70>, <__main__.Jets object at 0x00000194E25CBB80>, <__main__.Jets object at 0x00000194E25CBB20>, <__main__.Jets object at 0x00000194E25CBAC0>, <__main__.Jets object at 0x00000194E25CBA60>, <__main__.Jets object at 0x00000194E25CBA00>]

#este no funciona porque al crear la lista se anaden 
# los elementos COMO OBJETO, NO COMO CADENA DE 
# CARACTERES. Como no se anade como cadena de 
# caracteres, no se llama a la funcion __str__

#para arreglarlo, especificamos que hay que tratarlo
#como cadena de caracteres
first_army_country_fixed = [str(first_item),str(second_item),str(third_item),str(fourth_item),str(fifth_item),str(sixth_item)]
print(first_army_country_fixed)
