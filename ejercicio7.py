#7. Determinar si un alumno aprueba o suspende un 
# curso, sabiendo que aprobará si su promedio de 
# tres calificaciones es mayor o igual a 4.0; 
# supsende en caso contrario. Deberá permitir 
# ingresar las tres calificaciones y luego calcular
#  su promedio.

#permite enteros
Cal1 = (input("Ingrese calificacion 1: "))
Cal2 = (input("Ingrese calificacion 2: "))
Cal3 = (input("Ingrese calificacion 3: "))

if(Cal1.isnumeric() and Cal2.isnumeric() and Cal3.isnumeric()):
    Cal1 = int(Cal1)
    Cal2 = int(Cal2)
    Cal3 = int(Cal3)
    Prom = (Cal1 + Cal2 + Cal3)//3  #// para division entera
    print(Prom)

    if Prom >= 4: 
        print("Aprueba")
    else:
        print("Suspende")


#permite decimales
Cal1 = float(input("Ingrese calificacion 1: "))
Cal2 = float(input("Ingrese calificacion 2: "))
Cal3 = float(input("Ingrese calificacion 3: "))

Prom = (Cal1 + Cal2 + Cal3)/3
print(Prom)

if Prom >= 4: 
    print("Aprueba")
else:
    print("Suspende")

#version teniendo en cuenta que la nota esta entre 0 y 10
#salvando errores

#tomamos las notas 
Cal1 = input("Ingrese calificacion 1: ")
Cal2 = input("Ingrese calificacion 2: ")
Cal3 = input("Ingrese calificacion 3: ")

try:
    #transformamos notas de str a float 
    Cal1 = float(Cal1)
    Cal2 = float(Cal2)
    Cal3 = float(Cal3)

    #condicion de que la nota este entre 0 y 10
    if ((Cal1>=0 and Cal1<=10) and (Cal2>=0 and Cal2<=10) and (Cal3>=0 and Cal3<=10)):
        Prom = (Cal1 + Cal2 + Cal3)/3
        print(Prom)
        if Prom >= 4: 
            print("Aprueba")
        else:
            print("Suspende")
    else: 
        print("El rango de las calificaciones no esta entre 0 y 10")
except:
    print("Ingrese calificaciones numericas")