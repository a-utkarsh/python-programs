import numpy as np
var1 = "Hello World"
var2 = "Hello Python"

print(np.char.lstrip('H'))
print(np.char.add(var1, var2))
print(np.char.multiply(var1, 3))
print(np.char.center(var1, 3))
print(np.char.replace(var1, "H" , "W"))
print(np.char.split('o'))
print(np.char.index(var1, 'H'))
print(np.char.upper(var1))
print(np.char.lower(var1))
print(np.char.swapcase(var2))
print(np.char.title(var1))
print(np.char.count(var1, 'l'))
