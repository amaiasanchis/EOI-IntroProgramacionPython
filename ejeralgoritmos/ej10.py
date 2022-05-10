# 10. Adivinar una palabra.

palabrasecreta = "fiesta"

print("Inserte palabra (n para abandonar): ")

while True:
	palabra = input().lower()
	if palabra == palabrasecreta:
		print("Victoria")
		break #ahorra tener variable boolean comprobando estado
	elif palabra == "n":
		break
	else:
		print("Inserte palabra (N para abandonar): ")
    
#version 2
palabra = "Pirata".lower()
countE = 1
count = 0
intento = input("Intenta adivinar palabra: ").lower()
pistas = ["Les Gusta el Oro", "Les Gusta el Mar", "Usan Parches", "Tienen pata de palo"]
while(palabra != intento):
	if(count == len(pistas)):         
		count = 0        
		print(pistas[count])    
	else: 
		print(pistas[count])    
	intento = input(f"Intenta adivinar palabra llevas {countE} fallos: ").lower()    
	countE += 1    
	count += 1
