# 7. Encontrar el mayor número de tres números 

try:
    listanumeros = []  
    for i in range(1,4):
        numero = float(input(f"Ingrese numero {i}: "))
        listanumeros.append(numero)
    #print(listanumeros)

    mayor = listanumeros[0]
    for elemento in listanumeros:
        if elemento > mayor:
            mayor = elemento
    print(f"El numero mayor es {mayor}")
    

except:
    print("Inserte numeros adecuados")

#version2

#MAYOR DE 3  
Num1=input("Ingrese numero 1: ")
Num2=input("Ingrese numero 2: ")
Num3=input("Ingrese numero 3: ")

if(Num1.replace(".","",1).isdigit() and Num2.replace(".","",1).isdigit() and Num3.replace(".","",1).isdigit()):
    Num1=float(Num1)
    Num2=float(Num2)
    Num3=float(Num3)

    if(Num1>=Num2 and Num1>=Num3):
        print(f"Numero mayor es: {Num1} ")
    elif (Num2>=Num1 and Num2>=Num3):
        print(f"Numero mayor es: {Num2} ")
    else:
        print(f"Numero mayor es: {Num3} ")
else:
    print("Introduzca un numero valido")       

