from itertools import count
from multiprocessing import connection
from random import randint
from os.path import exists,split

def GestionFicherosValidacion(file_nombre,lista_datos):
    try:
        fichero=None
        #creamos las variables carpeta y file a partir del nombre del fichero
        carpeta, file = split(file_nombre)
        if (exists(carpeta)):
            if(exists(file_nombre)):
                #abrimos el fichero en modo lectura
                fichero = open (file_nombre,'rt',encoding='UTF-8')
                #leemos el fichero y guardamos el contenido en la variable contenido
                # contenido = fichero.read() #comentamos porque no lo vamos a sacar por pantalla
                print(f'Fichero:"{file}", previamente creado' )
                #este es su contenido:\n{contenido}')
            else:
                #si no existe el archivo, lo creamos (abrimos en modo escritura)
                fichero = open(file_nombre,'wt',encoding='UTF-8')
                #escribimos en el fichero el contenido de lista_datos
                fichero.write(str(lista_datos))
                print(f'Fichero:"{file}" - generado')
        else:
            raise Exception(f"Carpeta:'{carpeta}' no existe")
        return True
    except Exception as e:
        print(f'E-1:{e}')
        return False
    finally:
        # comprobacion de que el fichero se ha abierto/generado
        if fichero != None: fichero.close()

def connectBBDD(version=False):
    #Create a Database Temperaturas 
    #!!! antes hemos de crear la base de datos desde MSSQL
    import pyodbc
      
    server = 'LAPTOP-U1RN1B8E\MSSQLSERVER01'
    database = 'Temperaturas' 
    username = 'developer'
    password = 'P4$$w0rd'

    #Conecction String
    driver='DRIVER={ODBC Driver 17 for SQL Server};'
    others=f"SERVER={server};DATABASE={database};UID={username};PWD={password}"
    connection_string='{}{}'.format(driver,others)
    con = pyodbc.connect(connection_string) #pyodbc.Connection object 
    #with pyodbc.connect(connection_string) as cur:
    with con as wcon: #wcon???
        res=wcon.cursor().execute("SELECT @@VERSION AS 'SQL Server Version Details'")
        if (version): #comprobacion de version?
            for r in res:
                print(r[0])
    return con

def insertarDatosEstadisticosBBDD(con,contenido):
    with con as wcon:
        id=randint(1,101)
        #!!!! hay que crear primero la coleccion en la base de datos 
        """
        CREATE TABLE DatosEstadisticos(
        id int IDENTITY(1,1) NOT NULL,
        contenidoEstadistico nvarchar(2224) NULL)
        """  
        #en la base de datos> new query pinchando encima de Temperaturas
        #pegamos el codigo anterior pero borramos IDENTITY(1,1) (este genera ID ordenado desde 1)
        #ya que el ID se lo vamos a dar nosotrxs (generamos aleatoriamente en linea 59)
        #cambiamos el nombre de DatosEstadisticos por Temperaturas 
        sql = f"""INSERT INTO Temperaturas (id,contenidoEstadistico) VALUES ({id},?)
            """
        
        rc  = wcon.cursor().execute(sql,contenido)
        con.commit
        print(str(rc.rowcount),'record inserted ')
        return id

def recuperarDatosEstadisticosBBDD(con,id):
    with con as wcon:
        sql = f"""SELECT contenidoEstadistico FROM Temperaturas
                  WHERE id = {id}
        """
        res = wcon.execute(sql).fetchall()
        if len(res)==1:
            return res[0][0]

if __name__ == '__main__':
    lista={'Malaga': [27, 7, 3, 17, 9, 18, 33, 30, 37, 19, 12, 3], 'Alava': [13, 2, 41, 7, 1, 30, 25, 11, 45, 49, 17, 24], 'Albacete': [21, 21, 0, 48, 40, 14, 10, 12, 13, 37, 32, 16], 'Alicante': [36, 34, 41, 14, 6, 3, 42, 44, 18, 16, 31, 30], 'Almería': [49, 4, 33, 43, 24, 33, 14, 34, 49, 24, 19, 47], 'Asturias': [21, 28, 47, 48, 2, 36, 41, 30, 11, 21, 19, 30], 'Avila': [46, 48, 11, 44, 34, 23, 14, 27, 43, 41, 17, 20], 'Badajoz': [14, 10, 18, 5, 34, 5, 47, 37, 3, 43, 31, 48], 'Barcelona': [50, 0, 16, 48, 26, 43, 40, 42, 49, 18, 1, 18], 'Burgos': [38, 13, 9, 27, 20, 14, 7, 0, 36, 23, 14, 29], 'Cáceres': [31, 50, 16, 36, 39, 30, 8, 27, 45, 44, 23, 0], 'Cádiz': [20, 41, 40, 28, 13, 29, 39, 17, 46, 3, 10, 49], 'Cantabria': [40, 49, 14, 13, 32, 27, 22, 1, 34, 33, 42, 17], 'Castellón': [0, 50, 16, 27, 21, 25, 3, 10, 31, 33, 30, 5], 'Ceuta': [17, 2, 29, 20, 16, 36, 28, 37, 45, 2, 15, 37], 'Ciudad Real': [7, 14, 49, 40, 40, 8, 20, 11, 4, 7, 6, 44], 'Córdoba': [31, 0, 38, 13, 5, 22, 13, 3, 40, 6, 22, 1], 'Cuenca': [33, 46, 8, 35, 23, 4, 7, 28, 22, 15, 38, 7], 'Formentera': [29, 24, 43, 48, 37, 22, 42, 42, 14, 19, 38, 23], 'Girona': [34, 46, 6, 50, 19, 16, 26, 21, 37, 39, 49, 11]}

   # try:
    fichero_procesar='./datosejercsql.txt'
    con=None
    if GestionFicherosValidacion(fichero_procesar,lista):
        print('Proceso inicia')
        fichero = open(fichero_procesar,'rt',encoding='UTF-8')
        contenido = fichero.read()
        con=connectBBDD();
        if (con!=None):
            id=insertarDatosEstadisticosBBDD(con,contenido)
            res=recuperarDatosEstadisticosBBDD(con,id)
            lista=eval(res)
            print(lista)
    else:
        print('proceso no inicia')


    #except Exception as e:
        #print(f'E-0:{e}')