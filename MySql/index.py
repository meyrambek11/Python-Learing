import mysql.connector 

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Astana97$',
    #database = 'sakila'
)
mycursor = mydb.cursor()
#mycursor.execute('CREATE DATABASE testdb123')
#mycursor.execute('SHOW DATABASES')
#for db in mycursor:
    #print(db)
#mycursor.execute('CREATE TABLE people (login VARCHAR(255), password INTEGER(10))')
#mycursor.execute('SHOW TABLES')
#for tb in mycursor:
    #print(tb)




