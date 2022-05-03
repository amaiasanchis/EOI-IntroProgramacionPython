#5. Volumen y Area de un Cilindro *hecho*

import math
#print(type(math.pi))
pi = math.pi
try:
    h = float(input("Inserte altura en m: "))
    r = float(input("Inserte radio en m: "))
    A = 2 * r * (h + r) * pi
    V = r**2 * h * pi
    print(f"Area (m): {round(A,2)}, Volumen (m^2): {round(V,2)}")
    #otra version para redondear
    print("Area (m): {m:1.2f}, Volumen (m^2): {n:1.2f}".format(m=A,n=V))

    #otra version para redondear y sin crear variables, con la formula directamente
    print("Area (m): {n:1.2f}, Volumen (m^2): {m:1.2f}".format(n=(2*r*(h + r)*pi), m=(r*r*h*pi)))
except ValueError:
    print("Ingrese numero correcto")
