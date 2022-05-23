import pyodbc


server = 'LAPTOP-U1RN1B8E\MSSQLSERVER01'
database = 'bikerentdb' 
username = 'developer' 
password = 'P4$$w0rd' 

#Conecction String

#informamos del controlador driver 17
driver='DRIVER={ODBC Driver 17 for SQL Server};'
#aqui le informamos del servidor, la base de datos, usuario y contrasena
others=f"SERVER={server};DATABASE={database};UID={username};PWD={password}"
#ponemos toda la info en una variable: cadena de conexion
connection_string='{}{}'.format(driver,others)

#conectamos a la bbdd
#connect conecta con el servidor
#pyodbc con la base de datos 
con = pyodbc.connect(connection_string)

#cursor es el intermediario entre la base de datos y sus objetos
cur = con.cursor()
res=cur.execute("SELECT @@VERSION AS 'SQL Server Version Details'")
for r in res:
    print(r[0])
