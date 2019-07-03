import numpy as np
x = np.empty([3,2], dtype = int)
print (x)

#zero
x = np.zeros((5,2) )
print (x)

# custom type

x = np.zeros((2,2), dtype = [('x', 'f4'), ('y', 'i4')])
print (x)

x = np.ones([2,2], dtype = int)
print (x)