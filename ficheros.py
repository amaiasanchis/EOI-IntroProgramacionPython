#funcion para saber si un fichero existe
'''
def fichero_existe(nombre_fichero):
    try:
        open(nombre_fichero,'rt')
    except FileNotFoundError:
        return False
    return True
'''
#existe  una funcion preconstruida
from os.path import exists

try: 
    file = 'fichero.txt'
    # si el fichero existe, lo abrimos para leerlo (modo lectura)
    #(evitamos sobreescribir)
    if exists(file):
        fichero = open(file,'rt',encoding='UTF-8')
        contenido = fichero.read()
        print(contenido)    
    # si el fichero no existe, lo creamos modo escritura
    else:
        fichero = open(file,'wt',encoding='UTF-8')
        contenido = 'hola,\nesto es un fichero\ncon varias lineas'
        fichero.write(contenido)
except Exception as e:
    print(f'E:{e}')
    
finally:
    fichero.close()


