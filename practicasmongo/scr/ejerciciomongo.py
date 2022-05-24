from random import randint
from os.path import exists,split

def GestionFicherosValidacion(file_nombre,lista_datos):
    try:
        fichero=None
        carpeta, file = split(file_nombre)
        if (exists(carpeta)): # hay que meter el nombre con ruta. comprobacion de que existe la carpeta
            # si existe el fichero, lo leemos y sacamos info por pantalla
            if(exists(file_nombre)): 
                fichero = open (file_nombre,'rt',encoding='UTF-8')
                # contenido = fichero.read()
                print(f'Fichero:"{file}", previamente creado')
                # este es su contenido:\n{contenido}')
            # si no existe previamente, lo creamos a partir de la info almacenada en una lista
            else:
                fichero = open(file_nombre,'wt',encoding='UTF-8')
                fichero.write(str(lista_datos))
                # aviso de que se ha generado correctamente el ficherod
                print(f'Fichero:"{file}" - generado')
        else:
            raise Exception(f"Carpeta:'{carpeta}' no existe")
        return True
    except Exception as e:
        print(f'E-1:{e}')
        return False
    finally:
        # comprobacion de que se ha abierto/creado el fichero y se puede cerrar
        if fichero != None: fichero.close()

# funcion de conexion a mongoDB
def connectBBDD(version=False):
    from pymongo import MongoClient


    clientDB = MongoClient('mongodb://localhost:27017/')
    db = clientDB.admin
    #duda: para que sirve este bucle? que es version? no entra
    if(version):
        resultado = db.command('serverStatus')
        print('Host:',resultado['host'])
        print('Version:',resultado['version'])
        print('Process:',resultado['process'])
        print(clientDB.list_database_names())
    # clientDB = MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True) 
    # print('clientdb',clientDB)
    return clientDB 

# funcion de creacion de la base de datos 
def CreateDB(name,clientDb):
    database_name=name # 'Temperaturas', se lo daremos al llamar la funcion
    db=clientDb[database_name]
    # db = Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'Temperaturas')
    return db

#Create a collection
def createCollection(name,db):
    collection_name=name #'ListasTemperaturas'
    collection=db[collection_name]
    # print(db.list_collection_names()) --> ['ListaTemperaturas']
    return collection


#inserting documents in the collection
def insertDocument(Ciudad,Temperatura,TemperaturaMedia,col,document=None):
    id=randint(1,1000)
    docBB= {'Id':id,'Data':document, 'Ciudad': Ciudad, 'Temperatura': Temperatura, 'MediaAnual': TemperaturaMedia}
    col.insert_one(docBB) #insert_one para crear un documento, una entrada
    return id

#Retrieving the data from the collection
def retrievingDocument(query,col):
    result= col.find_one(query)
    return result['Data']


if __name__ == '__main__':
    #en este caso, la lista esta vacia porque los datos los tomamos de otro doc
    # si se generaran en el propio programa, se almacenarian en una lista para 
    # despues generar un fichero
    lista=[]
   # try:
    fichero_procesar='./scr/resultadosdata.txt'
    con=None
    db=None
    col=None

    # la funcion GestionFicherosValidacion devuelve True a no ser que haya algun error
    # si es true, implica que el fichero existe
    if GestionFicherosValidacion(fichero_procesar,lista):
        print('Proceso inicia')
        # abrimos el fichero de los datos
        fichero = open(fichero_procesar,'rt',encoding='UTF-8')
        contenido = fichero.read()
        # con == clientDB, que es lo que devuelve connectBBDD
        con=connectBBDD();
        # db == db, es lo que devuelve CreateDB
        db=CreateDB('Temperaturas',con)
        # col == collection
        col=createCollection('ListaTemperaturas',db)

        if (con!=None): #es decir, si se ha podido conectar
            id=insertDocument(None,None,None,col,contenido) #insertDocument devuelve id
            #entrada de identificador
            query={'Id':id}
            #entrada de info asociada al id
            res=retrievingDocument(query,col) #devuelve collection
            diccResultado=eval(res)
            print(diccResultado)
            #hacemos un bucle para anadir los elementos 
            for ciudad,temperatura in diccResultado.items():
                id=randint(1,1000)
                Ciudad = ciudad
                Temperatura = temperatura
                TemperaturaMedia = round(sum(temperatura)/12 ,2)
                insertar = insertDocument(Ciudad,Temperatura,TemperaturaMedia,col)
            
    else:
        print('proceso no inicia')


    #except Exception as e:
        #print(f'E-0:{e}')