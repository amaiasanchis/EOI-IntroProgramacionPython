from os.path import exists

def Proceso(contenido):
    pass
    
    listaedades = eval(contenido)

    file_resultado = 'DatosProg2resul.txt'
    try: 
        fichero_resultado = open(file_resultado,'wt',encoding='UTF-8')
        mayores = len([edad for edad in listaedades if edad >= 18])
        menores = len([edad for edad in listaedades if edad < 18])
        fichero_resultado.write(f"Hay {mayores} mayores de edad y {menores} menores de edad.\n")
    
        fichero_resultado.write('La persona de mayor edad tiene {m} años y la de menor edad, {n} años'.format(m=max(listaedades),n=min(listaedades)))

        listaedades.sort()
        diccedades = {edad:listaedades.count(edad) for edad in listaedades}
        fichero_resultado.write(f'{diccedades}\n')

        fichero_resultado.write('Porcentaje edades:\n')
        for key in diccedades:
            fichero_resultado.write(f'Edad: {key}, porcentaje: {diccedades[key]}%\n')

    except Exception as e:
        print(f'E(Proceso):{e}')
    finally:
        fichero_resultado.close()


try:
    file = 'DatosProg2.txt'
    if exists(file):
        fichero = open(file,'rt',encoding = 'UTF-8')
        contenido = fichero.read()
        Proceso(contenido)
        print(f'El contenido del fichero es {contenido}')
    else: 
        print('No se puede procesar la info')
except Exception as e:
    print(f'E:{e}')
finally:
    fichero.close()


