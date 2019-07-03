#The following procedure updates all the records having SEX as 'M'.
#Here, we increase AGE of all the males by one year.

#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","anand@123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to UPDATE required records
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
