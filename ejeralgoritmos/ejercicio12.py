#12 . Sumar los dígitos de un número ingresado. Ejemplo: Si se ingresa 123, 
# debería devolver 6.


nro = input("Ingrese un numero: ")
resul = 0
#comprobar que el numero lo es
if (nro.isdigit()):
    nro = int(nro)
    while nro != 0:
        resul += nro%10
        nro = nro//10

    print(f"El resultado es: {resul}")
else:
    print("Inserte numero valido")