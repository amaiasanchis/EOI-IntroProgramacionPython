numeros=(8,85,362,2,54,5,23.9)
print(numeros[3])
print(max(numeros))
print(min(numeros))
print(sum(numeros))

#concatena la tubla x veces (2)
print(numeros*2) 
numeros *= 2
print(numeros)


print(list(enumerate(numeros)))

dias = ('lun','mar','mie','jue','vie','sab','dom')
for dia in dias:
    print(dia)

#enumeramos los elementos de la tubla a partir de un valor (1 en este caso)
for dia_numero in enumerate(dias,1):
    print(dia_numero)


#tubla con letras del abecedario
letras='abcdefghijklmnopqrstuvwxyz'
#sacar letras, no hace falta tupla
for letra in letras:
    print(letra)

#creamos tupla y podemos enumerar con el valor que queramos (en este caso desde el 40)
letrasAlfabeto = tuple(x for x in letras)
print(letrasAlfabeto)
for letra in enumerate(letrasAlfabeto,40):
    print(letra)

#desempaquetar valores de la tupla
postres = ('flan','tiramisu','pudin')
postrea,postreb,postrec = postres

print(postrea,postreb,postrec)