# 7. Encontrar el mayor número de tres números 

try:
    listanumeros = []  
    for i in range(1,4):
        numero = float(input(f"Ingrese numero {i}: "))
        listanumeros.append(numero)
    print(listanumeros)

    mayor = listanumeros[0]
    for elemento in listanumeros:
        if elemento > mayor:
            mayor = elemento
    print(f"El numero mayor es {mayor}")
    

except:
    print("Inserte numeros adecuados")