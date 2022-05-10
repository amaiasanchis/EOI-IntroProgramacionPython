#6. Ingresar un numero y muestre todos los divisores del mismo.

#print("Ingrese numero: ")
Num = int(input("Ingrese numero: "))
div = 1
while (div <= Num):
    if (Num%div == 0):
        print(div)
    #FinSi
    div+=1
#FinMientras


#version para que si el numero no es valido vuelva a preguntar
while(True):
    print("Ingrese Numero, (N para salir): ")
    Num = input()
    if (Num.isdigit()): #podriamos anadir .isdecimal() para saber si es decimal, se convierte con float
        Num = int(Num)
        div = 1
        while (div <= Num):
            if (Num%div == 0):
                print(div)
            div+=1
    else:
        if (Num=="N"):
            break
        print("Ingrese numero")
