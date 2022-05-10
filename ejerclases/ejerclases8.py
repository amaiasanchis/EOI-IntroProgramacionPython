#Ahora hagamos algunos cambios en la clase que creamos en el ejercicio anterior de Python.
# Primero haga su función para que tome los parámetros: x e y. x será el número que se 
# eleva, e será la potencia. ¡Entonces, los usuarios pueden elevar los números a cualquier
#  potencia! También cambiemos el nombre de la función a "ElevarAlaPotencia".
# También agreguemos una representación de cadena rápidamente, de modo que cuando un 
# usuario imprima la clase obtenga una descripción significativa.
# Puede ser algo como: Esta clase consistirá en operaciones matemáticas. Solo tenemos una
#  función llamada ElevarAlaPotencia.

class myfunc:
    
    def ElevarAlaPotencia(x,y):
        numelevado = x**y
        return numelevado
    
    def __str__(self):
        return ('Esta clase consistirá en operaciones matemáticas. Solo tenemos una función llamada ElevarAlaPotencia')

 
ans1 = myfunc.ElevarAlaPotencia(5,6)
ans2 = myfunc.__str__(1)

print(ans1)
print(ans2)

# con inputs

num1 = int(input('inserte numero base: '))
num2 = int(input('inserte potencia: '))
ans = myfunc.ElevarAlaPotencia(num1,num2)
print(ans)

