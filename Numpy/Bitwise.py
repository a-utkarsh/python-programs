import numpy as np
print ('Binary equivalents of 13 and 17:')
a,b = 13,17
print (bin(a), bin(b))
print ('\n')

print ('Bitwise AND of 13 and 17:')
print (np.bitwise_and(13, 17))

print ('Bitwise OR of 13 and 17:')
print (np.bitwise_or(13, 17))

print ('Bitwise XOR of 13 and 17:')
print (np.bitwise_xor(13, 17))

print ('Bitwise complement of 13')
print (np.bitwise_not(13))

print ('Bitwise Left shift of 13')
print (np.left_shift(13,2))

print ('Bitwise Right of 13')
print (np.right_shift(13,2))

