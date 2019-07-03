import math







N=4
A=[2,3,2,3]
B=[]
C=[]
for i in A:
    B.append(math.factorial(i))
print(B)
for i in B:
    C.append(primeFactors(i))
print(C)
print(primeFactors(2))

