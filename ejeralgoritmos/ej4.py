#4. Realizar las cuatro operaciones básicas 
# (Suma, Resta, Multiplicación, División)


#flag
i = 0
while i == 0:
    #introducir las variables
    Num1 = input("Introduce primer numero: ")
    Num2 = input("Introduce segundo numero: ")
    operacion = input("Introduce operacion: ")

    #comprobar que los numeros son realmente numericos
    # para comprobarlo, quitamos el (posible) punto y vemos si es digito
    # ojo, si se introdujese un numero con varios puntos (89.09.0) tambien lo daria como bueno!! 
    # para evitar problemas, hacemos que reemplace solo una vez (los numeros con varios puntos daran error)
    
    if (Num1.replace(".","",1).isdigit() and Num2.replace(".","",1).isdigit()):

        Num1 = float(Num1)
        Num2 = float(Num2)
        if operacion == '+':
            print(Num1+Num2)
        elif operacion == '-':
            print(Num1-Num2)
        elif operacion == '*':
            print(Num1*Num2)
        elif operacion == '/':
            try:
                print(Num1/Num2)
            except (ZeroDivisionError):
                print("No se puede dividir entre cero")

        else:
            print("La operacion introducida no es correcta")

    else:
        print("Ingrese numero correcto")

    
    respuesta = input("¿Desea seguir haciendo operaciones? (si/no): ")
    if respuesta == "no":
        i = 1
