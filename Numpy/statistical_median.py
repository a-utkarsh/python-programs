import numpy as np

a = np.array([[30, 65, 70], [80, 95, 10], [50, 90, 60]])

print('Our array is:')
print(a)
print('\n')

#median
print('Applying median() function:')
print(np.median(a))
print('\n')

#mean
print ('Applying mean() function:')
print (np.mean(a))
print ('\n'  )

#average
print("average")
print(np.average(a))
print("")

#Standard deviation
print("std deveiation")
print(np.std(a))

#variance
print("variance")
print(np.var(a))