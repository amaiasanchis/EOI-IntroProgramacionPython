ciudad = "madrid"
print(ciudad.isdigit())
minombre="amaia"
print(len(minombre))

print(minombre[0])
print(minombre[1])
print(minombre[4])
#print(minombre[5]) error out of indexprint
print(minombre[2:]) #del tercer caracter (incluido) al final
print(minombre[:3]) #del principio al cuarto caracter (sin incluir)
print(minombre[2:4]) #del tercer caracter (incluido) al quinto (sin incluir)
print("2: "+minombre[2])
print("-2"+minombre[-2])
print(minombre[1:10])
print(minombre[-4]) #cuenta desde el final


mensaje="noemi"
ciudad= "albacete"
#para la concatenacion, usar format es mucho mas eficiente que con +
print("hola {m} de {c}".format(m=mensaje,c=ciudad))
print("hola "+mensaje+" de "+ciudad) #poco eficiente

numero = 10/3
print("El numero sin formato es: {}".format(numero))
print("El numero con formato es: {n:1.2f}".format(n=numero))
print(f"Hola {mensaje} de {ciudad}")
