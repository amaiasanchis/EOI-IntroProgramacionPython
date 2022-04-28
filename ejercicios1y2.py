#ejercicio 1
print("Hola mundo")

#ejercicio 2
#decir si un numero es menor, igual o mayor a 9
#traducimos el algoritmo que hicimos previamente

#N=0, sobra porque aunque se asigne N como numerico, al hacer el input va a cambiar a texto
print("Escribir el numero")
N=input() #input da valor tipo str, por lo que hay que convertir a int
#sin embargo, no convertimos a int en el input, sino que comprobamos que sea un digito para evitar errores
if(N.isdigit()):
    N=int(N)
    if (N==9):
        print("El numero es igual a 9")
    else: 
        if (N>9):
            print("El numero es mayor a 9")
        else:
            print("El numero es menor a 9")
    #FinSi
#FinAlgoritmo 