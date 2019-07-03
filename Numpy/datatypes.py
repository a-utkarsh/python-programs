
"""Object − To be converted to data type object
Align − If true, adds padding to the field to make it similar to C-struct
Copy − Makes a new copy of dtype object.
If false, the result is reference to builtin data type object"""

#int8, int16, int32,
#  int64 can be replaced by equivalent string 'i1', 'i2','i4', etc.

import numpy as np

dt = np.dtype('i2')
print (dt)


# file name can be used to access content of age column
import numpy as np

dt = np.dtype([('age',np.int8)])
a = np.array([(10,),(20,),(30,)], dtype = dt)
print (a['age'])
    

student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
c= np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)
print (c['name'])