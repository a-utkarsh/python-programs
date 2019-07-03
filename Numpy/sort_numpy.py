import numpy as np
a = np.array([[3, 7], [9, 1]])
print('Our array is:')
print(a)
print('\n')


print('Applying sort() function:')
print(np.sort(a))
print('\n')

print('Sort along axis 0:')
print(np.sort(a, axis=0))
print('\n')

# Order parameter in sort function
dt = np.dtype([('name', 'S10'), ('age', int)])
a = np.array([("raju", 21), ("anil", 25), ("ravi", 17), ("amar", 27)], dtype=dt)

print('Our array is:')
print(a)
print('\n')

print('Order by name:')
print(np.sort(a, order='age'))
print(np.sort(a, order='name'))