from random import randint
from os.path import exists,split

def GestionFicherosValidacion(file_nombre,lista_datos):
    try:
        fichero=None
        carpeta, file = split(file_nombre)
        if (exists(carpeta)):
            if(exists(file_nombre)):
                fichero = open (file_nombre,'rt',encoding='UTF-8')
                contenido = fichero.read()
                print(f'Fichero:"{file}", previamente creado, este es su contenido:\n{contenido}')
            else:
                fichero = open(file_nombre,'wt',encoding='UTF-8')
                fichero.write(str(lista_datos))
                print(f'Fichero:"{file}" - generado')
        else:
            raise Exception(f"Carpeta:'{carpeta}' no existe")
        return True
    except Exception as e:
        print(f'E-1:{e}')
        return False
    finally:
        if fichero != None: fichero.close()

def connectBBDD(version=False):
    from pymongo import MongoClient


    clientDB = MongoClient('mongodb://localhost:27017/')
    db = clientDB.admin
    if(version):
        resultado = db.command('serverStatus')
        print('Host:',resultado['host'])
        print('Version:',resultado['version'])
        print('Process:',resultado['process'])
        print(clientDB.list_database_names())
    return clientDB

def CreateDB(name,clientDb):
    database_name=name # 'Estadisticas'
    db=clientDb[database_name]
    return db

#Create a collection
def createCollection(name,db):
    collection_name=name #'ListasTemperaturas
    collection=db[collection_name]
    #print(db.list_collection_names())
    return collection


#inserting documents in the collection
def insertDocument(document,col):
    id=randint(1,1000)
    docBB= {'Id':id,'Data':str(document)}
    col.insert_one(docBB)
    return id

#Retrieving the data from the collection
def retrievingDocument(query,col):
    result= col.find_one(query)
    return result['Data']


if __name__ == '__main__':
    lista={'Malaga': [27, 7, 3, 17, 9, 18, 33, 30, 37, 19, 12, 3], 'Alava': [13, 2, 41, 7, 1, 30, 25, 11, 45, 49, 17, 24], 'Albacete': [21, 21, 0, 48, 40, 14, 10, 12, 13, 37, 32, 16], 'Alicante': [36, 34, 41, 14, 6, 3, 42, 44, 18, 16, 31, 30], 'Almería': [49, 4, 33, 43, 24, 33, 14, 34, 49, 24, 19, 47], 'Asturias': [21, 28, 47, 48, 2, 36, 41, 30, 11, 21, 19, 30], 'Avila': [46, 48, 11, 44, 34, 23, 14, 27, 43, 41, 17, 20], 'Badajoz': [14, 10, 18, 5, 34, 5, 47, 37, 3, 43, 31, 48], 'Barcelona': [50, 0, 16, 48, 26, 43, 40, 42, 49, 18, 1, 18], 'Burgos': [38, 13, 9, 27, 20, 14, 7, 0, 36, 23, 14, 29], 'Cáceres': [31, 50, 16, 36, 39, 30, 8, 27, 45, 44, 23, 0], 'Cádiz': [20, 41, 40, 28, 13, 29, 39, 17, 46, 3, 10, 49], 'Cantabria': [40, 49, 14, 13, 32, 27, 22, 1, 34, 33, 42, 17], 'Castellón': [0, 50, 16, 27, 21, 25, 3, 10, 31, 33, 30, 5], 'Ceuta': [17, 2, 29, 20, 16, 36, 28, 37, 45, 2, 15, 37], 'Ciudad Real': [7, 14, 49, 40, 40, 8, 20, 11, 4, 7, 6, 44], 'Córdoba': [31, 0, 38, 13, 5, 22, 13, 3, 40, 6, 22, 1], 'Cuenca': [33, 46, 8, 35, 23, 4, 7, 28, 22, 15, 38, 7], 'Formentera': [29, 24, 43, 48, 37, 22, 42, 42, 14, 19, 38, 23], 'Girona': [34, 46, 6, 50, 19, 16, 26, 21, 37, 39, 49, 11]}
   # try:
    fichero_procesar='./scr/ejmongodatosiniciales.txt'
    con=None
    db=None
    col=None
    if GestionFicherosValidacion(fichero_procesar,lista):
        print('Proceso inicia')
        fichero = open(fichero_procesar,'rt',encoding='UTF-8')
        contenido = fichero.read()
        con=connectBBDD();
        db=CreateDB('Temperaturas',con)
        col=createCollection('ListaTemperaturas',db)
        if (con!=None):
            id=insertDocument(contenido,col)
            query={'Id':id}
            res=retrievingDocument(query,col)
            lista=eval(res)
            print(lista)
    else:
        print('proceso no inicia')


    #except Exception as e:
        #print(f'E-0:{e}')