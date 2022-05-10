#5. Sumar todos los numeros pares entre 2 y 100.

suma = 0
nro = 2
while (nro<=100):
    if(nro%2 == 0):
        suma+=nro
    nro+=1
#finwhile
print(f"la suma de los pares entre 2 y 100 es {suma}")

suma = 0
nro = 2
while (nro<=100):
    suma+=nro
    nro+=2
#finwhile
print(f"la suma de los pares entre 2 y 100 es {suma}")