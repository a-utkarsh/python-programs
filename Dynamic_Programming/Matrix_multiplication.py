def matrix_multi(arr,i,j):
    import math
    if i==j:
        return 0
    minx= math.inf

    for k in range(i,j):
        count=matrix_multi(arr,i,k)+matrix_multi(arr,k+1,j)+arr[i-1]*arr[k]*arr[j]
        if count<minx:
            minx=count
    return minx

arr = [10, 100, 20, 5, 80]
n = len(arr)

print(matrix_multi(arr, 1, n - 1))

#Matrix multiplication using dynamic programming
def MatrixMulti(arr,n):
    import math
    table=[[0 for i in range(n)] for j in range(n)]
    for l in range(2,n):# l is chain length
        for i in range(n-l+1):
            j=i+l-1
            table[i][j]=math.inf
            for k in range(i,j):
                count=table[i][k]+table[k+1][j]+arr[i-1]*arr[k]*arr[j]
                if count<table[i][j]:
                    table[i][j]=count
    return table[1][n-1]
print(MatrixMulti(arr,len(arr)))