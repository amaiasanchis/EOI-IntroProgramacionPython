#6. Pedir un libro en una biblioteca 
 
librosbiblio = ["La plaça del diamant", "Romancero gitano", "La Celestina"]
print("Ir a la biblioteca")
print("Ir al mostrador")
titulo = input("Inserte titulo del libro: ")
if titulo in librosbiblio:
    print("Dar el carnet")
    print("Retirar libro")
else:
    print("Libro no disponible")
print("Abandonar la biblioteca")
