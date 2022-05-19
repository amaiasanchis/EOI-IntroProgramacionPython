import pyodbc 


server = '(localdb)\LAPTOP-U1RN1B8E\MSSQLSERVER01'
database = 'bikerentdb' 
username = 'developer' 
password = 'P4$$w0rd' 

#Conecction String

#controlador driver 17
driver='DRIVER={ODBC Driver 17 for SQL Server};'
#aqui le informamos del servidor, la base de datos, usuario y contrasena
others=f"SERVER={server};DATABASE={database};UID={username};PWD={password}"
#ponemos toda la info en una variable
connection_string='{}{}'.format(driver,others)

#conectamos a la bbdd
con = pyodbc.connect(connection_string)

cur = con.cursor()
res=cur.execute("SELECT @@VERSION AS 'SQL Server Version Details'")
for r in res:
    print(r[0])
