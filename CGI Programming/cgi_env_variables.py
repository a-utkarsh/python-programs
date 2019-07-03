
import os

print ("Content-type: text/html\r\n\r\n")
print ("<font size=+1>Environment</font><\br>")
for i in os.environ.keys():
   print ("%20s: %s<\b" % (i, os.environ[i]))