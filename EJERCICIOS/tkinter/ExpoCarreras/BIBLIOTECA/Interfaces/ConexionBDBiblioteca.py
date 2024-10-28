import mysql.connector
class Cconexion:
    
 def conexion():
       
    try:
            conexion = mysql.connector.connect(user="root",
                            host="localhost",                            
                            password="bru455no", 
                            database="BibliotecaJoseHporto")  
            print ("Conexion Correcta")
            return conexion           
    except mysql.connector.Error as error: 
        print ("Error AL conectarte a la base de datos{}".format(error))
            
        return conexion