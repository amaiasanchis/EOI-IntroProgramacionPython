# 10. Adivinar una palabra.


```
Algortimo AdivinarPalabra
Palabra <- "Fiesta"        
R = "Si"             
Repetir          
	Escribir "Entre palabra a adivinar"      
	Leer PalabraEntrada         
	If Palabra = PalabraEntrada      
		Escribir "Has adivinado"        
	Sino   
		Escribir "Otra oportunidad (si/no)"
		Leer R
Hasta que R = "no"
Escribir "Gracias por jugar"
FinAlgoritmo

```
palabrasecreta = "Fiesta"
R = "Si"

palabra = input("Inserte palabra: ")
if palabra == palabrasecreta:
    print("Victoria")
else: 
    

