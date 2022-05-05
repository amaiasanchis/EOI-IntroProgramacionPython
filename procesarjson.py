import json

jsonventas= '{"departamento": 8,"nombredepto": "Ventas","director": "Juan Rodriguez","empleados": [{"nombre": "Pedro","apellido": "Fernandez"},{"nombre": "Jacinto","apellido": "Benavente"}]}'
#segundojson= "{'departamento': 8,'nombredepto': 'Ventas','director': 'Juan Rodriguez','empleados': [{'nombre': 'Pedro','apellido': 'Fernandez'},{'nombre': 'Jacinto','apellido': 'Benavente'}]}"
print(type(jsonventas))
print(jsonventas)

#SERIALIZAR: DUMPS
#al usar dumps hacemos una serializacion, el output es un str
datosDepartamento=json.dumps(jsonventas)
print(type(datosDepartamento))
print("Json 1:",datosDepartamento)

#DESERIALIZAR: LOADS
datosDepart = json.loads(jsonventas)
print(type(datosDepart))
print(datosDepart)

# la variable q debo usar para procesar el JSON
#como una coleccion compleja (compuesta) es el deserializado (loads)

#for val in datosDepart:
    #print (val)


for val in datosDepart:
    if val!='empleados':
        print(val,":",datosDepart[val])
    else:
        print('Integrantes dpto:')
        for integrantes in datosDepart['empleados']:
            print('\t\t',integrantes['nombre'],' ', integrantes['apellido'])


