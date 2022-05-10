# suma de dos numeros

Num1=input("Escribir numero 1: ")
Num2=input("Escribir numero 2: ")
if (Num1.isdigit() and Num2.isdigit()):
    #Num1=int(Num1)
    #Num2=int(Num2)
    Rta=int(Num1)+int(Num2)
    print(f"El resultado es: {int(Num1)+int(Num2)}")
else:
    print("Los valores proporcionados no son validos")