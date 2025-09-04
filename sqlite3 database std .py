import sqlite3 
# Creting Connection 
con=sqlite3.Connection("employee.db") 
print(con) 
#Creating Table 
con.execute("create table emp(id number primarykey, name text,desig text,age number,sal number)") 
print("Table created")
 
#Inserting values 
 
con.execute("insert into emp(id,name,desig,age,sal)values(01,'abc','Dev',30,50000);") 
con.execute("insert into emp(id,name,desig,age,sal)values(02,'lmn','Test',35,30000);") 
con.execute("insert into emp(id,name,desig,age,sal)values(03,'xyz','Admin',25,60000);") 
 
print("Values Inserted") 
#Update Record 
con.execute("update emp set name='bcd' where id=2;") 
print("Record Updated") 
#Delete a record 
con.execute("delete from emp where id=3;") 
print("Record Deleted") 
# Selecting all records 
print("\t E.id \t E.name\t E.Designation \t E.Age\t E.Sal") 
r=con.execute("select * from emp;") 
for c in r: 
    print("\t",c[0],"\t",c[1],"\t",c[2],"\t\t",c[3],"\t",c[4])
