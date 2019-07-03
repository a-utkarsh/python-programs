def pascals(n):
    #n=5
    A=[1]

    final=[]
    for i in range(n):
    #print(A)
        final.append(A)
        newlist=[]
        newlist.append(A[0])
        for j in range(len(A)-1):

            newlist.append(A[j]+A[j+1])
        newlist.append(A[-1])
        A=newlist
    #final.append(A)
    return final
print(pascals(5))
#c=0

n=5
for i in range(1,n+1):
    C=1
    print(" " * (n- i), end=" ")
    for j in range(1,i):

        print(C,end=" ")
        C=int(C*(i-j)/j)
    print(C,end=" ")
    print(" ")


n=5
final=[]
for i in range(1,n+1):
    C=[1]
    for j in range(1,i):
        C.append(C[0])
        #C = int(C * (i - j) / j)
        C[j]=int(C[j-1]*(i-j)/j)
    final.append(C)
print(final)
