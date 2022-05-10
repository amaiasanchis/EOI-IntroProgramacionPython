#11. Si un número ingresado es primo o no. 

nro = input("Ingrese un número: ")
if (nro.isdigit()):
	nro = int(nro)
	div = 2
	band = True
	if nro == 1:
		print("Es primo")
	else:
		while band and (nro>div): # no hace falta poner band == True, porque python ya interpreta como true
			if (nro % div) == 0:
				band = False
				break
			div += 1
		if band:
			print("Es primo")
		else: 
			print("No es primo")
else:
	print("Ingrese un numero valido")