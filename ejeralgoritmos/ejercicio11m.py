#11m. Mostrar los x primeros numeros primos 

nroprimos = input("Numero de primos a mostrar: ")

try:
    nroprimos = int(nroprimos)
    nro = 1
    while nroprimos > 0: # a cada primo que saque por pantalla se restara 1 a nroprimos
        div = 2
        band = True
        if nro == 1:
            print(nro)
            nroprimos -= 1
            
        else:
            while band and (nro>div): # no hace falta poner band == True, porque python ya interpreta como true
                if (nro % div) == 0:
                    band = False
                div += 1
            if band:
                print(nro)
                nroprimos -= 1
            #else: 
                #print("No es primo")
        nro += 1
    
except:
    print("Ingrese numero valido")