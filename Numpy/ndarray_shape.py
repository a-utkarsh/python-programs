import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print(a)
print (a.shape)

#This resizes the array

a.shape = (3,2)
print (a.shape)
print("")
#NumPy also provides a reshape function to resize an array.
a = np.array([[1,2,3],[4,5,6]])
#b = a.reshape(3,2)
print (a.reshape(3,2))
print(a.shape)
