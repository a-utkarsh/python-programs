#Resize method
import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print ('First array:')
print (a)
print ('\n')
print ('The shape of first array:')
print (a.shape)
print ('\n')
b = np.resize(a, (3,2))
print ('Second array:')
print (b)
print ('\n')
print ('The shape of second array:')
print (b.shape)
print ('\n')
# Observe that first row of a is repeated in b since size is bigger
print ('Resize the second array:')
b = np.resize(a,(3,3))
print (b)

#Append method
a = np.array([[1,2,3],[4,5,6]])
print ('First array:')
print (a )
print ('\n')
print ('Append elements to array:' )
print (np.append(a, [7,8,9]))
print ('\n')
print ('Append elements along axis 0:' )
print (np.append(a, [[7,8,9]],axis = 0) )
print ('\n')
print ('Append elements along axis 1:')
print (np.append(a, [[5,5,5],[7,8,9]],axis = 1))

#insert method

import numpy as np
a = np.array([[1,2],[3,4],[5,6]])

print ('First array:')
print (a )
print ('\n')

print ('Axis parameter not passed. '
      'The input array is flattened before insertion.' )
print (np.insert(a,3,[11,12]))
print ('\n')
print ('Axis parameter passed.'
       ' The values array is broadcast to match input array.')

print ('Broadcast along axis 0:')
print (np.insert(a,1,[11],axis = 0) )
print ('\n')

print ('Broadcast along axis 1:')
print (np.insert(a,1,11,axis = 1))

#delete
import numpy as np
a = np.arange(12).reshape(3,4)

print ('First array:')
print (a)
print ('\n')

print ('Array flattened before delete operation as axis not used:' )
print (np.delete(a,5))
print ('\n')

print ('Column 2 deleted:' )
print (np.delete(a,1,axis = 1))
print ('\n')

print ('A slice containing alternate values from array deleted:')
a = (np.array([1,2,3,4,5,6,7,8,9,10]))
print (np.delete(a, np.s_[::2]))

#Unique method
import numpy as np
a = np.array([5,2,6,2,7,5,6,8,2,9])

print ('First array:')
print (a)
print ('\n')

print ('Unique values of first array:')
u = (np.unique(a))
print (u)
print ('\n')

print ('Unique array and Indices array:')
u,indices = np.unique(a, return_index = True)
print (indices )
print ('\n')

print ('We can see each number corresponds to index in original array:')
print (a)
print ('\n')

print ('Indices of unique array:')
u,indices = np.unique(a,return_inverse = True)
print (u)
print ('\n')

print ('Indices are:')
print (indices)
print ('\n')

print ('Reconstruct the original array using indices:')
print (u[indices])
print ('\n')

print ('Return the count of repetitions of unique elements:')
u,indices = (np.unique(a,return_counts = True))
print (u)
print (indices)

