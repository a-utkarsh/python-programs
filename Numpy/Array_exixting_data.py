# ndarray from list of tuples
import numpy as np

x = [1,2,3,4,5]

a = np.asarray(x)
print(a)
print (a.reshape(5,1))





# obtain iterator object from list
import numpy as np
list = range(1,5)
it = iter(list)

# use iterator to create ndarray
x = np.fromiter(it, dtype = float)
print(x)
print (x.reshape(2,2))