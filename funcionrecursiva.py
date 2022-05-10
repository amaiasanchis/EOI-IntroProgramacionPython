#funcion factorial
'''
def Factorial(N):
    if (N==1 or N == 0):
        return 1
    elif N < 0:
        return 'No existe factorial'
    else:
        return N * Factorial(N-1)


n = input('Desea calcular el factorial de: ')
try:
    n = int(n)
    r = Factorial(n)
    print(f'El factorial de {n} es {r}')
except TypeError:
    print('Introduzca un numero valido')
    '''

# fibonacci
def Fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return (Fibonacci(n-1) + Fibonacci(n-2))


N = input("¿Que numero de la serie quiere?: ")
try:

    N = int(N)
    seriefib=[]
    for i in range(1,N+1):
        r=Fibonacci(i)
        seriefib.append(r)
    print(f'El numero en esa posicion es {r}') 
    print('La serie es:',*seriefib)   

except:
    print('Inserte numero valido')
