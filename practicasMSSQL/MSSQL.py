#Create a Database bikerentdb 
#Table customer
"""
CREATE TABLE customer (CustID int NOT NULL,   
CustName varchar(50) NOT NULL, 
CustAddress varchar(200) DEFAULT NULL,  
CustPhone varchar(20) DEFAULT NULL, 
CustEmail varchar(50) DEFAULT NULL, 
CustCity varchar(50) DEFAULT NULL )
"""
import pyodbc 

def insert(con,cur):
    #read values to be inserted
    #insertamos los datos de la entrada
    cid=input("Enter customer ID:")
    cnm=input("Enter customer Name:")
    cad=input("Enter customer Address:")
    cph=input("Enter customer Phone:")
    cem=input("Enter customer Email:")
    cct=input("Enter customer City:")

    #create the Insert query
    #sentencia sql de insercion
    '''esto es lo que genera el mssql (visor)
    INSERT INTO [dbo].[customer]
           ([CustID]
           ,[CustName]
           ,[CustAddress]
           ,[CustPhone]
           ,[CustEmail]
           ,[CustCity])
     VALUES
     #se nos indica el tipo del que tiene que ser 
     # la variable
           (<CustID, int,>
           ,<CustName, varchar(50),>
           ,<CustAddress, varchar(200),>
           ,<CustPhone, varchar(20),>
           ,<CustEmail, varchar(50),>
           ,<CustCity, varchar(50),>)
           '''

   
    sql = f"""INSERT INTO customer (CustID, 
    CustName, CustAddress,CustPhone, CustEmail, CustCity) 
    VALUES ({cid},'{cnm}','{cad}','{cph}','{cem}','{cct}')"""
    
    #create list of values typed from user to insert in customer table
    #Execute query with values
    # Do the insert
    cur.execute(sql)
    #commit the transaction

    #commit for permanent storage in database
    #commit para confirmar los cambios
    con.commit()
    #display success message
    print(cur.rowcount, "Record inserted.")

def update(con,cur):
    '''management studio da:
    UPDATE [dbo].[customer]
   SET [CustID] = <CustID, int,>
      ,[CustName] = <CustName, varchar(50),>
      ,[CustAddress] = <CustAddress, varchar(200),>
      ,[CustPhone] = <CustPhone, varchar(20),>
      ,[CustEmail] = <CustEmail, varchar(50),>
      ,[CustCity] = <CustCity, varchar(50),>
 WHERE <Search Conditions,,>'''

    #read values to be updated
    cid=input("Enter customer ID:")
    cnm=input("Enter customer Name:")
    cad=input("Enter customer Address:")
    cph=input("Enter customer Phone:")
    cem=input("Enter customer Email:")
    cct=input("Enter customer City:")
    #create update query
    #condicion: no se varia el ID. cid no en set sino en where
    sql = f"""update customer set CustName='{cnm}', 
    CustAddress='{cad}',CustPhone='{cph}', CustEmail='{cem}', 
    CustCity='{cct}' where CustID={cid}"""
    
    #Execute Update query on opened cursor
    cur.execute(sql)
    #commit Changes to DB
    con.commit()
    #display success message
    #se tiene que poner despues del commit, ya que 
    #este puede dar error
    print(cur.rowcount, "Record updated.")

def delete(con,cur):
    '''
    DELETE FROM [dbo].[customer]
      WHERE <Search Conditions,,>'''

    #read the customer ID for which record to be deleted
    cid=input("Enter customer ID to delete:")
    #Create Delete Query
    sql = f"delete FROM customer where CustID = '{cid}'"
    #execute delete query
    cur.execute(sql)
    #commit changes to DB
    con.commit()
    #display success message
    #rowcount me da cuantas filas han sido afectadas 
    #por la ultima solicitud ejecutada
    #esta a nivel del cursor
    print(cur.rowcount, "Record deleted.")

def display(cur):
    #Execute SELECT statement 
    cur.execute("SELECT * FROM customer")
    #Fetch all records from table
    #fetchall para que devuelva los valores de la solicitud
    res = cur.fetchall()
    #print
    linea='-'*80
    print(linea)
    print("CustID CustName   CustAddress  CustCity   CustPhone  CustEmail")
    print(linea)
          
    for x in res:
        print('{:6} {:10} {:12} {:10} {:10} {:6}'.format(str(x[0]),x[1],x[2],x[5],x[3],x[4]))
    print(linea)  

def main():

    server = 'LAPTOP-U1RN1B8E\MSSQLSERVER01'
    database = 'bikerentdb' 
    username = 'developer' 
    password = 'P4$$w0rd' 

    #Conecction String
    driver='DRIVER={ODBC Driver 17 for SQL Server};'
    others=f"SERVER={server};DATABASE={database};UID={username};PWD={password}"
    connection_string='{}{}'.format(driver,others)
    con = pyodbc.connect(connection_string)
    #cursor es el intermediario entre la base de datos y sus objetos
    cur = con.cursor()
    res=cur.execute("SELECT @@VERSION AS 'SQL Server Version Details'")
    for r in res:
        print(r[0])

    #display menu until user presses 5

    while True:
        #menu options
        print("1. INSERT -- (C)reate")
        print("2. DISPLAY-- (R)ead")
        print("3. UPDATE -- (U)pdate")
        print("4. DELETE -- (D)elete")
        print("5. EXIT")
        # ask user to enter what he wants to do
        try:
            ch=int(input("Enter Your choice:"))
            #call relevant fucntions defined above
            if (ch==1): insert(con, cur)
            if (ch==2): display(cur)
            if (ch==3): update(con, cur)
            if (ch==4): delete(con, cur)
            if (ch==5): break
        except:
            print('Entre una selección válida')
        
#call main
# esta funcion da una condicion. Hace que si se exporta
#el modulo a otro programa, no se ejecute la funcion
#__main__ por defecto
if __name__=='__main__':
    main() 