#11. Si un número ingresado es primo o no. 

```
Algoritmo NumerosPrimos
	Escribir "Ingrese un número: " // 2
	Leer nro
	div <- 2 // 4
	band <- Verdadero 	         
        Si nro=1 Entonces 	 // 6	            
             Escribir "Es primo" 	         
        Sino 		             // 8 
            Mientras band=Verdadero y nro>div Hacer
				Si nro MOD div = 0 Entonces // 10
		    		band <- Falso
				FinSi // 12
		    		div <- div +1
	     	FinMientras    // 14
	     si band= Verdadero Entonces
		Escribir "Es primo"    // 16
	     Sino
		Escribir "No es primo"    // 18
	     FinSi
	FinSi     // 20
FinAlgoritmo
```