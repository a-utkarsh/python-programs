import numpy as np
a = np.arange(12).reshape(3,4)
#Transpose Method
print ('The original array is:')
print (a)
print ('\n')

print ('The transposed array is:')
print (np.transpose(a))


#.T method
print ('\n')
print ('The 2nd transposed array is:')
print(a.T)

#rollaxes
print ('\n')
print ('The 3rd transposed array is:')
print(np.rollaxis(a,1))

print ('\n')
print ('The transposed array is:')
print(np.swapaxes(a, 1, 1))