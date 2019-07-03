file = open("gratia.txt" , "w+")
file.write(" hey I am Utkarsh Anand! from Gratia Technology")
print ("Name of the file: ", file.name)

print(file.fileno())
print(file.isatty())

line = file.readline(2)

line = file.readlines()
print ("Read Line: %s" % (line))
print ("Read Line: %s" % (line))

line = file.readline()
print ("Read Line: %s" % (line))
print(file.buffer)
file.truncate(2)

