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

mycursor.execute("SHOW TABLES")

for tb in mycursor:
    print(tb)
