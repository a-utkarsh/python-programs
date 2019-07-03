import numpy as np
a = np.arange(24)
print (a)

# this is one dimensional array

print(a.ndim)

# now reshape it
b = a.reshape(2,4,3)
print (b)
print(b.ndim)
# b is having three dimensions