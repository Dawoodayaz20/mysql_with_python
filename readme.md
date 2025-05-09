# MySql Database with Python

## Steps to Create MySql DataBase with Python:

1. We connect to MySql Database by
    `mysql.connector.connect`.
2. With this, we connect to the database. We also have to put parameters in `.connect() function` 
<`(
    host="localhost",
    user="root",
    passwd="your_password",
    database="your_database_name"
)`>

### MySQL Cursor:
> A MySQL cursor is a database object that enables the end-user to retrieve, process, and scroll through rows of the result set one at a time.
`mycursor = mydb.cursor()`
>This is how we specify the cursor of our database.

3. To create a database:
<mycursor.execute("CREATE DATABASE STUDENTS")>

