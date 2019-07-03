for i in range(1,11):
   for j in range(1,11):
      k=i*j
      print (k, end='\t')
   print("")

#The print() function inner loop has end=' '
# which appends a space instead of default newline.
# Hence, the numbers will appear in one row.


#Last print() will be executed at the end of inner for loop.