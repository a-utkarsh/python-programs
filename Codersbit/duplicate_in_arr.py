def repeatedNumber(A):
    A = list(A)
    n = len(A)
    for i in range(n):
        if A[abs(A[i])] > 0:
            A[abs(A[i])] = -A[abs(A[i])]
        else:
            return abs(A[i])
    return -1
arr=[1,2,2,4]
print(repeatedNumber(arr))