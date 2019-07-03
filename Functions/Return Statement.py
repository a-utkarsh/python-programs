# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2
   sub = arg1- arg2
   print ("Inside the function : ", total)
   return total,sub

# Now you can call sum function
print("Outside the function : ", sum(20,10))