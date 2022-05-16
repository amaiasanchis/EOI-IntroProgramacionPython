from os.path import exists

def Proceso(contenido,genero):
    pass
    lista = eval(contenido)
    file_resultado = 'programas\DatosProg3resul.txt'
    try: 
        #numero de personas del genero
        fichero_resultado = open(file_resultado,'wt',encoding='UTF-8')
        fichero_resultado.write(f'{genero}\n')
        fichero_resultado.write(f"Numero de {genero}: {len(lista)}\n")

        #mayor/menor edad
        mayoresedad=len([n for n in lista if n>=18])
        menoresedad=len([n for n in lista if n<18])
        fichero_resultado.write(f'{genero} mayores de edad: {mayoresedad}\n')
        fichero_resultado.write(f'{genero} menores de edad: {menoresedad}\n')

        # persona de mayor edad y de menor edad 
        edadmenor= min(lista)
        fichero_resultado.write(f"{genero} con menor edad tiene(n) {edadmenor} años\n")

        edadmayor=max(lista)
        fichero_resultado.write(f"{genero} con mayor edad tiene(n) {edadmayor} años\n")

        #promedio edad
        promedio_edad=sum(lista)/len(lista) 
        fichero_resultado.write(f"La edad promedio de {genero} es: {promedio_edad}\n")


    except Exception as e:
        print(f'E(Proceso):{e}')
    finally:
        fichero_resultado.close()


try:
    files = ['programas\DatosProg3Hombres.txt','programas\DatosProg3Mujeres.txt']
    for file in files: 
        if exists(file):
            fichero = open(file,'rt',encoding = 'UTF-8')
            contenido = fichero.read()
            if file.count('Hombres'):
                Proceso(contenido,'Hombres')
            else: 
                Proceso(contenido,'Mujeres')
            #print(f'El contenido del fichero es {contenido}')
            fichero.close()
        else: 
            print('No se puede procesar la info')
except Exception as e:
    print(f'E:{e}')

