#4. Realizar las cuatro operaciones básicas 
# (Suma, Resta, Multiplicación, División)

#introducir las variables
Num1 = input("Introduce primer numero: ")
Num2 = input("Introduce segundo numero: ")
operacion = input("Introduce operacion: ")

#comprobar que los numeros son realmente numericos 
#if (Num1.isnumeric() and Num2.isnumeric): (no tiene en cuenta los decimales)
    # si lo son,los convertimos en decimales
Num1 = float(Num1)
Num2 = float(Num2)
if operacion == '+':
    print(Num1+Num2)
elif operacion == '-':
    print(Num1-Num2)
elif operacion == '*':
    print(Num1*Num2)
elif operacion == '/':
    print(Num1/Num2)


