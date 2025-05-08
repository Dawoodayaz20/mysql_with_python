import mysql.connector

print("Connecting...")
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Agent#1122",
    database="testdb"
)

if(mydb):
 print("Connected!")

# name = input("Enter your name: ") 
# if (name): 
#     print(mydb)

mycursor = mydb.cursor()


# To show databases created, we run this code:
# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)


#TO CREATE A TABLE:
# mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")


#To show a table created earlier
# mycursor.execute("SHOW TABLES")
# for tb in mycursor:
#     print(tb)


# sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
# students = [("Bob", 22),
#             ("Bob", 18),
#             ("Bob", 28),
#             ("Bob", 32),
#             ("Bob", 25)]
# To execute a single string like ("Bob", 22), we use mycursor.execute
# But for executing a tuple having arrays, we use mycursor.executemany.
# mycursor.executemany(sqlFormula, students)
# mydb.commit()


# Get all data in a table:
# This code is for quering the database to select all records in a table and show them
mycursor.execute("SELECT * FROM students")
myresult = mycursor.fetchall()
for row in myresult: 
   print(row)


# Get some specific data in the row of a table:
# This command is for quering the database to select a specific record in a table and show on the screen:
mycursor.execute("SELECT age FROM students")
myresult = mycursor.fetchone()
for row in myresult: 
   print(row)