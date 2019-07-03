A=[5,6, 8, 6, 1, 2, 4, 5 ]
A[len(A)-1]= (A[len(A)-1]+1)
if(A[0]==0):
    print(A[1:len(A)], end=" ")
else:
    print(A[0:len(A)],end=" ")