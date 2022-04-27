#error div entre 0
numero1 = 100
numero2 = 0
#print(numero1/numero2) da error porque no se puede dividir por 0
try:
    print(numero1/numero2)
except ZeroDivisionError: #excepcion personalizada
    print("Error al dividir por cero")
except:
    print("Error")
else:
    print("La division se ha producido correctamente")
finally:
    print("fin del programa")
print("next")


#con error div entre 0, mas elementos en try
numero1 = 100
numero2 = 0
#print(numero1/numero2) da error porque no se puede dividir por 0
try:
    print("instrucción1")
    print("instrucción2")
    print(numero1/numero2)
    print("instrucción4") #no se ejecutan estas lineas porque hay un error previo. salta a except
    print("instrucción5")
except ZeroDivisionError: #excepcion personalizada
    print("Error al dividir por cero")
except:
    print("Error")
else:
    print("La division se ha producido correctamente")
finally:
    print("fin del programa")

print("next")

#sin error, va a else y finally
numero1 = 100
numero2 = 5
try:
    print(numero1/numero2)
except ZeroDivisionError: #excepcion personalizada
    print("Error al dividir por cero")
except:
    print("Error")
else:
    print("La division se ha producido correctamente")
finally:
    print("fin del programa")

print("next")

#con error al intentar convertir palabra en entero
numero1 = 100
numero2 = 5
a = "madrid"
try:
    print("instrucción1")
    print("instrucción2")
    print(numero1/numero2)
    print("instrucción4")
    c = int(a)
    print("instrucción6")
except ZeroDivisionError: #excepcion personalizada
    print("Error al dividir por cero")
except ValueError:
    print("Error valor al convertir palabra a entero")
except:
    print("Error")
else:
    print("Las instrucciones se han completado correctamente")
finally:
    print("fin del programa")

print("next")
