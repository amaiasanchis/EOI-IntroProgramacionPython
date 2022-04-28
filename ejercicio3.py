#decidir si un numero es par o impar

#print("Escriba numero"), no hace falta porque se puede poner directamente en input
nro=input("Escriba numero entero: ")
if (nro.isdigit()):
    nro = int(nro)
    if (nro%2==0):
        print("Es par")
    else:
        print("Es impar")
else:
    print("Ingrese numero valido")