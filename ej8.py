#8. Factorial de cualquier número

numero = input("Ingrese numero: ")

if numero.isdigit():
    numero = int(numero)
    if numero > 0:
        factorial = 1
        while numero != 0:
            factorial *= numero
            numero -= 1
        print(f"Factorial = {factorial}")
    elif numero == 0:
        print("Factorial = 1")
    else:
        print("No existe factorial")
else:
    print("Ingrese numero valido")

# version 2, usando funcion
from math import factorial

numero = int(input("Ingrese numero: "))
print(f"Factorial = {factorial(numero)}")