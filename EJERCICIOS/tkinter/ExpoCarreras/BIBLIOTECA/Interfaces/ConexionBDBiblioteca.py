import mysql.connector

def conexion():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="bru455no",  
        database="bibliotecajosehporto"
    )
    return mydb.cursor(), mydb