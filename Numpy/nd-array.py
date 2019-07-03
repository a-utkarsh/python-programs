import  numpy as np
a= np.array([1,2,2])
print(a)

#Two dimensional or more than one dimension
b = np.array([[1, 2], [3, 4]])
print (b)
print(b.shape)
print(b.ndim)
#minimum dimensions
c = np.array([1, 2, 3,4,5], ndmin = 3)
print (c.shape)
print(c)
print(c.ndim)
#datatype parameter
d = np.array([1, 2, 3], dtype = complex)
print (d)