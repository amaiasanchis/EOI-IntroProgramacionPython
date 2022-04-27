#iteracion
for numero in range(4): #va de 0 a 3
    print(numero)
for numero in range(1,4): #va de 1 a 3
    print(numero)
for numero in range(1,11,3): #va de 1 a 10, de 3 en 3
    print(numero)
print("next")

#continue
contadornumero = 0
for numero in range(1,21,2): #numeros impares del 1 al 20
    contadornumero+=1
    if (contadornumero<=5): # no muestra los 5 primeros numeros 
        continue
    print(numero)

print("next")

#break
contadornumero = 0
for numero in range(1,21,2): #numeros impares del 1 al 20
    contadornumero+=1
    if (contadornumero>5): 
        break #salta a la linea despues del bloque for
    print(numero)

print("next")

#sentencia repeticion while
#mostrar los 5 primeros numeros excepto el 3
print("antes de while")
valor = 0
while(valor<5):
    valor+=1
    if(valor==3):
        continue
    print(f"valor actual:{valor}")

print("despues de while")

print("next")

#iteracion colecciones
lenguajes=['python','c','c++','java']
print("los lenguajes son:",lenguajes)
print(lenguajes[0])
for lenguaje in lenguajes:
    print(lenguaje)