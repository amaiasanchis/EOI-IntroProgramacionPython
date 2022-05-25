from pymongo import MongoClient 

#client para conectarnos a la BBDD
# objeto que representa la BBDD
clientDB = MongoClient('mongodb://localhost:27017/')
# conectarse como administrador
db = clientDB.admin 
resultado = db.command('serverStatus')
print('Host:',resultado['host'])
print('Version:',resultado['version'])
print('Process:',resultado['process'])

