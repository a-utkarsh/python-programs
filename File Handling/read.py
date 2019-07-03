#!/usr/bin/python3

# Open a file
fo = open("gratia.txt", "r+")
str = fo.read()
print ("Read String is : ", str)

# Close opened file
fo.close()