#SPlit
import numpy as np
a = np.arange(9)
print ('First array:')
print (a)
print ('\n')
print ('Split the array in 3 equal-sized subarrays:')
b = (np.split(a,3))
print (b )
print ('\n' )
print ('Split the array at positions indicated in 1-D array:')
b = np.split(a,[4,7])
print (b)

#hsplit method
import numpy as np
a = np.arange(16).reshape(4,4)

print ('First array:')
print (a)
print ('\n')

print ('Horizontal splitting:')
b = np.hsplit(a,2)
print (b)
print ("\n")

#vsplit
print("Vsplit array is")
d= np.vsplit(a,2)
print(d)

#rsplit method