from os.path import exists

def Proceso(contenido):
    pass
    #evalua una cadena y determina si es valida 
    #para reemplazarla por una instruccion
    # en este caso convierte str a lista
    listaaleatoria = eval(contenido)

    file_resultado = 'DatosProg1resul.txt'
    try: 
        fichero_resultado = open(file_resultado,'wt',encoding='UTF-8')
        numhombres = listaaleatoria.count('M')
        nummujeres = listaaleatoria.count('H')
        fichero_resultado.write(f'Porcentaje de mujeres: {nummujeres}% y porcentaje de hombres: {numhombres}%\n')
    
        if nummujeres > numhombres:
            fichero_resultado.write('Hay mas mujeres que hombres\n')
        elif nummujeres == numhombres:
            fichero_resultado.write('Hay igual numero de mujeres que de hombres\n')
        else: 
            fichero_resultado.write('Hay mas hombres que mujeres\n')
    except Exception as e:
        print(f'E(Proceso):{e}')
    finally:
        fichero_resultado.close()


try:
    file = 'DatosProg1.txt'
    if exists(file):
        print('Fichero previamente generado, no se sobreescribe')
        fichero = open(file,'rt',encoding = 'UTF-8')
        contenido = fichero.read()
        Proceso(contenido)
        print(f'El contenido del fichero es {contenido}')
    else: 
        print('No se puede procesar la info')

    fichero.close()
except Exception as e:
    print(f'E:{e}')
finally:
    fichero.close()

