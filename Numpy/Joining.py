# Concatenate
import numpy as np
a = np.array([[1,2],[3,4]])
print ('First array:')
print (a)
print ('\n')
b = np.array([[5,6],[7,8]])
print ('Second array:')
print (b)
print ('\n')
# both the arrays are of same dimensions
print ('Joining the two arrays along axis 0:')
print (np.concatenate((a,b)))
print ('\n')
print ('Joining the two arrays along axis 1:')
print (np.concatenate((a,b),axis = 1))

#Stack method
a = np.array([[1,2],[3,4]])

print ('First Array:')
print (a)
print ('\n')
b = np.array([[5,6],[7,8]])

print ('Second Array:')
print (b)
print ('\n')

print ('Stack the two arrays along axis 0:')
print (np.stack((a,b),0) )
print ('\n')

print ('Stack the two arrays along axis 1:')
print (np.stack((a,b),1))

#Hstack method
import numpy as np
a = np.array([[1,2],[3,4]])

print ('First array:')
print (a)
print ('\n')
b = np.array([[5,6],[7,8]])

print ('Second array:')
print (b)
print ('\n')

print ('Horizontal stacking:')
c = (np.hstack((a,b)))
print (c)
print ('\n')

#Vstack
import numpy as np
a = np.array([[1,2],[3,4]])

print ('First array:')
print (a)
print ('\n')
b = np.array([[5,6],[7,8]])

print ('Second array:')
print (b)
print ('\n')

print ('Vertical stacking:' )
c = np.vstack((a,b))
print (c)