import mysql.connector 

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Astana97$',
    database = 'users'
)

mycursor = mydb.cursor()
name = input("Write name, please: ")
passwordd = input("Write password, please: ")
print("Thank you")
sqlinfo = 'INSERT INTO people (login, password) VALUES (%s, %s)'
user1 = (name,passwordd)

#user = [("User1",789), ("User2",456),("User3",123)]

#mycursor.executemany(sqlInfo,user)

mycursor.execute(sqlinfo, user1)
mydb.commit()
