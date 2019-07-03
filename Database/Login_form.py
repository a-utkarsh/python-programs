#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb
import MySQLdb
db = MySQLdb.connect("localhost","root","anand@123","TESTDB" )
cursor = db.cursor()


# Create instance of FieldStorage
form = cgi.FieldStorage()
first = input("first name")
last = input("last name")
# Get data from fields
first_name = form.getvalue('first_name')

last_name  = form.getvalue('last_name')


print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")

print ("<h2>Hello %s %s</h2>" % (first_name, last_name))
print ("</body>")
print ("</html>")




# Drop table if it already exist using execute() method.
# Create table as per requirement
sql = "INSERT INTO STUDENT(First_Name,Last_Name) VALUES(%s, %s)" ,(first ,last)


   # Execute the SQL command
cursor.execute(*sql)
   # Commit your changes in the database
db.commit()


# disconnect from server
db.close()