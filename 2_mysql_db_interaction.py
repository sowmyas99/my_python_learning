#2) use python to interact with MySQL db server. Provide a list of options to user like add 
# database, add table, add a row in a table, delete table, delete database

import mysql.connector  
  

def create_database():

    print("Enter database name: ")
    dbname = input()
    myconn = mysql.connector.connect(host = "localhost", user = "xxxx",passwd = "xxxx")  
  
    #creating the cursor object  
    cur = myconn.cursor()  
  
    try:  
        #creating a new database  
        cur.execute("CREATE DATABASE IF NOT EXISTS %s" %dbname) 
  
    except:  
        myconn.rollback()  
            
    myconn.close()  


def show_databases():
    #Create the connection object   
    myconn = mysql.connector.connect(host = "localhost", user = "xxxx",passwd = "xxxx")    
  
    #creating the cursor object  
    cur = myconn.cursor()  
  
    try:  
        #get the list of all the databases
        dbs = cur.execute("SHOW DATABASES")  
      
    except:  
        myconn.rollback()  
  
    for x in cur:  
        print(x)
          
    myconn.close()  


def add_table():
      
    #Create the connection object   
    myconn = mysql.connector.connect(host = "localhost", user = "xxxx",passwd = "xxxx", database = "DB1")   
  
    #creating the cursor object  
    cur = myconn.cursor()  
  
    try:  
        #Creating a table with name Employee having four columns i.e., name, id, salary, and department id  
        dbs = cur.execute("CREATE TABLE EMPLOYEE(name varchar(20) not null, id int(20) not null primary key, salary float not null, Dept_id int not null)")  
    except:  
        myconn.rollback()  
  
    myconn.close()  


def add_row():
    #Create the connection object   
    myconn = mysql.connector.connect(host = "localhost", user = "xxxx",passwd = "xxxx", database = "DB1")  
    #creating the cursor object  
    cur = myconn.cursor()  
    sql = "INSERT INTO EMPLOYEE(name, id, salary, dept_id) values (%s, %s, %s, %s)"
  
    #The row values are provided in the form of tuple   
    val = ("John", 110, 25000.00, 201)  
  
    try:  
        #inserting the values into the table  
        cur.execute(sql,val)  
  
        #commit the transaction   
        myconn.commit()  
      
    except:  
        print("Exception")
        myconn.rollback()  
  
    print(cur.rowcount,"record inserted!")  
    myconn.close()  


def delete_table():
    #Create the connection object   
    myconn = mysql.connector.connect(host = "localhost", user = "xxxx",passwd = "xxxx", database = "DB1")  
    #creating the cursor object  
    cur = myconn.cursor()  
    sql = "DROP TABLE EMPLOYEE"
  
    try:  
        #Deleting the values from the table  
        cur.execute(sql)  
  
        #commit the transaction   
        myconn.commit()  
      
    except:  
        print("Exception")
        myconn.rollback()  
  
    print(cur.rowcount,"Record deleted!")  
    myconn.close()  


def delete_database():
    #Create the connection object   
    myconn = mysql.connector.connect(host = "localhost", user = "xxxx",passwd = "xxxx")  
    #creating the cursor object  
    cur = myconn.cursor()  
    sql = "Drop database DB1"
  
    try:  
        #Deleting the database  
        cur.execute(sql)  
      
    except:  
        print("Exception")
        myconn.rollback()  
  
    print(cur.rowcount,"Database deleted!")  
    myconn.close()  


def mysql_db_operations(argument):
    switcher = {
        1: create_database,
        2: show_databases,
        3: add_table,
        4: add_row,
        5: delete_table,
        6: delete_database
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "DB operation not supported!!")
    # Execute the function
    print (func())


print("Enter the db operations to perform:")
print("1. Create database")
print("2. Show databases")
print("3. Add table")
print("4. Add row")
print("5. Delete table")
print("6. Delete database")

input_val=input()
mysql_db_operations(int(input_val))
