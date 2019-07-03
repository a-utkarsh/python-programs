def maxDistance(A):
    import math

    A=list(A)
    i=0
    j=len(A)-1
    max=-math.inf


    if len(A) == 0:
        return -1
    elif(len(A)>1):
        while i<=j:
            if i==j==len(A)-1:
                return 0

            if i==j:
                i+=1
                j=len(A)-1
            if A[j]>=A[i] and j-i>max:
                if(A[j]==A[i]):
                    max=j-i
                else:
                    max=j-i

            else:
                j-=1
        return max


    else:
        return 0

A=(6,4,5,2)
print(maxDistance(A))

