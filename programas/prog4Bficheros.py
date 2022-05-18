from os.path import exists

def Proceso(contenido):
    pass
    file_resultado = 'programas/DatosProg4resul.txt'
    fichero_resultado = None
    try:
        dicc = eval(contenido)
        fichero_resultado = open(file_resultado,'wt',encoding='UTF-8')
        DiccPromedioAnual={} 
        for clave,valor in dicc.items(): 
            fichero_resultado.write(f'{clave} -> {valor}\n') 
            tuplatemperaturas = tuple(valor) 
            MediaAnuales = (round(sum(tuplatemperaturas)/12 ,2)) 
            DiccPromedioAnual[clave] = MediaAnuales 
        
        fichero_resultado.write('{} \n'.format('='*80))

        MaxProAnual = max(DiccPromedioAnual.values()) 
        MinProAnual = min(DiccPromedioAnual.values()) 

        fichero_resultado.write(f'La ciudad con el promedio anual mas ALTO es {list(DiccPromedioAnual.keys())[list(DiccPromedioAnual.values()).index(MaxProAnual)]} con un promedio de: {MaxProAnual} ºC\n')
        fichero_resultado.write(f'La ciudad con el promedio anual mas BAJO es {list(DiccPromedioAnual.keys())[list(DiccPromedioAnual.values()).index(MinProAnual)]} con un promedio de: {MinProAnual} ºC \n') 

        fichero_resultado.write('{} \n'.format('='*80))

        ListaPromedioAnual = sorted(DiccPromedioAnual,key=DiccPromedioAnual.get,reverse=True)
        fichero_resultado.write(f'La lista de las ciudades ordenadas es :\n{ListaPromedioAnual}')

        # para sacar ciudad y temperatura ordenadas
        columna = 1
        for ciudad in ListaPromedioAnual:
            #if columna%2 == 0:
                #fichero_resultado.write('\n')
            #else:
                #fichero_resultado.write('\t')
            fichero_resultado.write(' {} \t {}ºC {}'.format(ciudad,DiccPromedioAnual[ciudad],'\n' if columna%2 == 0 else '\t'))
            columna +=1
            




    except Exception as e:
        print(f'E(Proceso):{e}')
    finally:
        fichero_resultado.close()


try:
    file = 'programas/DatosProg4.txt'
    fichero = None
    if exists(file):
        fichero = open(file,'rt',encoding = 'UTF-8')
        contenido = fichero.read()
        Proceso(contenido)
        #print(f'El contenido del fichero es {contenido}')
    else: 
        print('No se puede procesar la info')
except Exception as e:
    print(f'E:{e}')
finally:
    if fichero != None: 
        fichero.close()

