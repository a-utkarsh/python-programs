import numpy as np
a = np.arange(8)
print ('The original array:')
print (a)
print ('\n')
print(a.ravel())
b = a.reshape(4,2)
print ('The modified array:')
print (b)

#Flat method
a = np.arange(8).reshape(2,4)
print ('The original array:')
print (a)
print ('\n')

print ('After applying the flat function:')
# returns element corresponding to index in flattened array
print (a.flat[2])


# Flatten method
a = np.arange(8).reshape(2,4)
print ('The original array is:' )
print (a )
print ('\n' )
# default is column-major

print ('The flattened array is:' )
print (a.flatten() )
print ('\n')

#Ravel method

a = np.arange(8).reshape(2,4)

print ('The original array is:')
print (a)
print ('\n')

print ('After applying ravel function:' )
a
print ('\n')
