import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Astana97$',
    database = 'users'
)
mycursor = mydb.cursor()
#mycursor.execute('SELECT * FROM people')
mycursor.execute('SELECT * FROM people')
myresult = mycursor.fetchall()
#myresult = mycursor.fetchone()

#for row in myresult:
    #print(row)
print(myresult)

mydb.commit()
