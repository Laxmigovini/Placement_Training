import sqlite3
 # Creting Connection
con=sqlite3.Connection("Student.db")
print(con)
 #Creating Table
con.execute("create table stud(rollno number primarykey, name text,branch text,age number,percentage real)")
print("Table created")
 #Inserting values
con.execute("insert into stud(rollno,name,branch,age,percentage)values(01,'abc','CSE',30,80)")
con.execute("insert into stud(rollno,name,branch,age,percentage)values(02,'lmn','CSE',35,85)")
con.execute("insert into stud(rollno,name,branch,age,percentage)values(03,'xyz','CSE',25,89)")
print("Values Inserted")
 #Update Record
con.execute("update stud set name='bcd' where rollno=2;") 
print("Record Updated") 
 
#Delete a record 
con.execute("delete from stud where rollno=3;") 
print("Record Deleted") 
# Selecting all records 
print("\trollno\t name\t branch\t age\t percentage") 
r=con.execute("select * from stud;") 
for c in r: 
    print("\t",c[0],"\t",c[1],"\t",c[2],"\t",c[3],"\t",c[4])
