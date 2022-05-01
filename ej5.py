#5. Volumen y Area de un Cilindro *hecho*

import math

#print(type(math.pi))
h = float(input("Inserte altura en m: "))
r = float(input("Inserte radio en m: "))
A = 2 * r * (h + r) * math.pi
V = r**2 * h * math.pi
print(f"Altura (m): {round(A,2)}, Volumen (m^2): {round(V,2)}")

