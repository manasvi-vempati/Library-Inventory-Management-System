import mysql.connector

def mydbConnection():
    connection = None
    try:
        connection = mysql.connector.connect(host="localhost",user="root",passwd="Welcome@123")
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def mydbQuery(connection, query, message):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print(message)
    except Error as e:
        print(f"The error '{e}' occurred")
    cursor.close()

## Creating a new database if it doesnt exist already
createDB="create database if not exists LIBRARY"

##creating a books table
BooksTbl="create table IF NOT EXISTS LIBRARY.BOOKS (Bkid INT primary key,Bkname VARCHAR(255), Authname VARCHAR(255),Totcop INT,Circno INT,Bal INT,BookStatus VARCHAR(255))"

##creating a members table
MembersTbl="create table IF NOT EXISTS LIBRARY.MEMBERS (Memid INT primary key, Memname VARCHAR(255), Memph INT, Memaddress VARCHAR(255), Mememail VARCHAR(50),MemStatus VARCHAR(255))"

##creating a registry table
regisTbl="CREATE TABLE IF NOT EXISTS LIBRARY.Registry(RegID INT primary key ,MemID INT not null,BookID INT not null,BookName VARCHAR(255),DOI VARCHAR(255),DOR VARCHAR(255),foreign key (MemID) references MEMBERS(Memid),foreign key (BookID) references BOOKS(Bkid))"

connection=mydbConnection()
mydbQuery(connection, createDB, "Database LIBRARY created successfully!" )
mydbQuery(connection, BooksTbl, "Books table has been created successfuly in LIBRARY database" )
mydbQuery(connection, MembersTbl, "Members table has been created successfuly in LIBRARY database" )
mydbQuery(connection, regisTbl, "Registry table has been created successfuly in LIBRARY database" )

print(" ")
print(" ")
print("Library Database is ready to use! Happy reading!!")
