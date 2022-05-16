from os.path import exists

def Proceso(contenido_hombre,contenido_mujer):
    pass
    lista_mujer = eval(contenido_mujer)
    lista_hombre = eval(contenido_hombre)

    file_resultado = 'programas\DatosProg3resul.txt'
    try: 
        #numero de personas del genero
        fichero_resultado = open(file_resultado,'wt',encoding='UTF-8')
        fichero_resultado.write(f"Numero de mujeres: {len(lista_mujer)}\n")
        fichero_resultado.write(f"Numero de hombres: {len(lista_hombre)}\n")

        #mayor/menor edad
        mayoresedad=len([n for n in lista_mujer if n>=18])
        menoresedad=len([n for n in lista_hombre if n<18])
        fichero_resultado.write(f'Mujeres mayores de edad: {mayoresedad}\n')
        fichero_resultado.write(f'Hombres menores de edad: {menoresedad}\n')

        # personas de mayor edad y de menor edad 
        edadmenor_mujer= min(lista_mujer)
        edadmenor_hombre = min(lista_hombre)
        fichero_resultado.write(f"Mujer con menor edad tiene {edadmenor_mujer} años\n")
        fichero_resultado.write(f"Hombre con menor edad tiene {edadmenor_hombre} años\n")


        edadmayor_mujer=max(lista_mujer)
        edadmayor_hombre=max(lista_hombre)
        fichero_resultado.write(f"Mujer con mayor edad tiene {edadmayor_mujer} años\n")
        fichero_resultado.write(f"Hombre con mayor edad tiene {edadmayor_hombre} años\n")

        #promedio edad
        promedio_edad_mujer=sum(lista_mujer)/len(lista_mujer) 
        promedio_edad_hombre=sum(lista_hombre)/len(lista_hombre) 
        fichero_resultado.write(f"La edad promedio de las mujeres es: {round(promedio_edad_mujer,2)}\n")
        fichero_resultado.write(f"La edad promedio de los hombres es: {round(promedio_edad_hombre,2)}\n")


    except Exception as e:
        print(f'E(Proceso):{e}')
    finally:
        fichero_resultado.close()


try:
    file_male = 'programas\DatosProg3Hombres.txt'
    file_female = 'programas\DatosProg3Mujeres.txt'
    if exists(file_male and file_female):
        fichero_hombre = open(file_male,'rt',encoding = 'UTF-8')
        fichero_mujer = open(file_female,'rt',encoding = 'UTF-8')
        contenido_hombre = fichero_hombre.read()
        contenido_mujer = fichero_mujer.read()
        Proceso(contenido_hombre,contenido_mujer)
        #print(f'El contenido del fichero es {contenido}')
        fichero_mujer.close()
        fichero_hombre.close()
    else: 
        print('No se puede procesar la info')
except Exception as e:
    print(f'E:{e}')

