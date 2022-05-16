#simulamos una muestra aleatoria de 100 personas 
# (suponemos que todas las edades son igual de probables)
from random import randint
from os.path import exists

#funcion
def lee_o_crea_fichero_a_partir_de_una_lista(file_nombre,personas):
    try: 
    
        if exists(file_nombre):
            fichero = open(file_nombre,'rt',encoding = 'UTF-8')
            contenido = fichero.read()
            print(f'Fichero previamente creado, este es su contenido: {contenido}')
        else: 
            fichero = open(file_nombre,'wt',encoding = 'UTF-8')
            fichero.write(str(personas))
            print(f'Fichero {file_nombre} generado')
    except Exception as e:
        print(f'E:{e}')
    finally: 
        fichero.close()

# para poder reutilizar esta funcion
# este if indica que estamos en el file de origen
#print(f'Ejercicio2 : {__name__}')
if __name__ == '__main__':
    personas = [randint(0,125) for i in range(1,101)]
    file = 'DatosProg2.txt'
    lee_o_crea_fichero_a_partir_de_una_lista(file, personas)
else:
    pass