import math


def printSubsequences(arr, n):
    opsize = math.pow(2, n)
    A=[]
    C=[]

    # Run from counter 000..1 to 111..1
    for counter in range(1, (int)(opsize)):
        B = []
        for j in range(0, n):

            if (counter & (1 << j)):
                B.append(arr[j])
                #print(arr[j], end=" ")
        A.append(B)
        #print()
    for i in A:
        if i.count(i[0])==len(i):
            C.append(i)

    return len(C)
        #A.append(arr[j])
    # Driver progra


arr = [{2}, {2, 3}, {2, 3}, {2, 3, 5}]
n = len(arr)
print("All Non-empty Subsequences")

print(printSubsequences(arr,n))