import statistics

A=[2,2,2,2,1,5]
B=statistics.median(A)
C=[]
for i in A:
    x=i-B

    C.append(abs(x))
print(C)
print(int(sum(C)))
