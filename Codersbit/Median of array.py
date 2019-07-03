def findMedianSortedArrays(A, B):
    C = list(A) + list(B)
    C.sort()
    D = C[:]
    x = 0
    if len(D) % 2 == 0:
        x = (D[int(len(D) / 2) - 1] + D[(len(D) // 2)]) / 2
    else:
        x = D[(len(D) // 2)]
    return x
A=[0,23]
B=[]
print(findMedianSortedArrays(A,B))
