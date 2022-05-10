#9. Encontrar si un numero en mayor o menor a un número dado. *hecho*


numdado = float(input("Inserte numero base: "))
numproblema = float(input("Inserte numero problema: "))

if numproblema > numdado:
    print("Mayor")
elif numproblema < numdado:
    print("Menor")
else: 
    print("Los numeros son iguales")