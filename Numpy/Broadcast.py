



#2) Broadcast_to method
import numpy as np
a = np.arange(4).reshape(1,4)
print ('The original array:')
print (a)
print ('\n')
print ('After applying the broadcast_to function:' )
print (np.broadcast_to(a,(4,4)))

#3) expand Dims
import numpy as np
x = np.array(([1,2],[3,4]))
print ('Array x:')
print (x)
print ('\n')
y = np.expand_dims(x, axis = 0)
print ('Array y:')
print (y )
print ('\n')
print ('The shape of X and Y array:')
print (x.shape, y.shape )
print ('\n')
# insert axis at position 1
y = np.expand_dims(x, axis = 1)
print ('Array Y after inserting axis at position 1:' )
print (y)
print ('\n')
print ('x.ndim and y.ndim:')
print(x.ndim,y.ndim)
print ('\n')
print ('x.shape and y.shape:')
print (x.shape, y.shape)

#Sqeeze method
x = np.arange(9).reshape(1,3,3)
print ('Array X:')
print (x)
print ('\n')
y = np.squeeze(x)

print ('Array Y:')
print (y)
print ('\n')

print ('The shapes of X and Y array:')
print (x.shape, y.shape)