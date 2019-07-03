

#A=[3,4,1,4,1]
def repeatednum(A):
    for i in A:
        if A.count(i)>1:
            return i
        #break

    else:
        return -1
A=[3,4,1,4,1]
print(repeatednum(A))