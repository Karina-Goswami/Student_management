import mysql.connector
from mysql.connector import Error
print("  \n ABC college")
print("---------------------------------------")
print(" 1.Computer engineering")
mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="",
                             database="student_data")
mycursor=mydb.cursor()
print(mydb)
mycursor.execute("show tables")

for x in mycursor:
  print(x)
#course deatils       
print("Course table")
cursor =mydb.cursor()

cursor.execute("SELECT * FROM course")
myresult = cursor.fetchall()

for x in myresult:
    print(x)


#student details
def studetail():
    print("Student details")
    cursor =mydb.cursor() 
    cursor.execute("SELECT * FROM studb")
    myresult = cursor.fetchall()
    for x in myresult:
      print(x)

#order by    
def order():
    cursor = mydb.cursor()
    sql = "SELECT * FROM course ORDER BY subject_name"
    cursor.execute(sql)
    myresult = cursor.fetchall()
    for x in myresult:
      print(x)

#fetch 5 rows
def limit():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM studb LIMIT 5")
    myresult = cursor.fetchall()
    for x in myresult:
      print(x)

#update
def update():
    cursor = mydb.cursor()
    sql = "UPDATE studb SET Semester = '4' WHERE Name = 'ruhi'"
    cursor.execute(sql)
    mydb.commit()
    print(cursor.rowcount, "record(s) affected")

#function call
limit()
order()
studetail()
update()
