a = int(input(" Enter a number"))
b= int(input("Enter another number"))

if ( a == b ):
  print ("a is equal to b")
else:
   print ("a is not equal to b")

if ( a != b ):
   print ("a is not equal to b")
else:
   print ("a is equal to b")

if ( a < b ):
   print ("a is less than b" )
else:
   print ("a is not less than b")

if ( a > b ):
   print ("a is greater than b")
else:
   print ("a is not greater than b")

a,b=b,a #values of a and b swapped. a becomes 10, b becomes 21

if ( a <= b ):
   print ("a is either less than or equal to  b")
else:
   print ("a is neither less than nor equal to  b")

if ( b >= a ):
   print ("b is either greater than  or equal to b")
else:
   print ("b is neither greater than  nor equal to b")