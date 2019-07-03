def noble(A):
    def sorting(arr):
        if len(arr)>1:
            mid=len(arr)//2
            L=arr[:mid]
            R=arr[mid:]
            sorting(L)
            sorting(R)
            i,j,k=0,0,0
            while i<len(L) and j <len(R):
                if L[i]<R[j]:
                    arr[k]=L[i]
                    i+=1
                else:
                    arr[k]=R[j]
                    j+=1
                k+=1

            while i<len(L):
                arr[k]=L[i]
                i+=1
                k+=1
            while j<len(R):
                arr[k]=R[j]
                j+=1
                k+=1
        return arr
    sorting(A)
    n=len(A)-1
    for i in range(len(A)-1):
        if A[i]==A[i+1]:
            continue
        if A[i]==n-i:
            return A[i]

    if A[n]==0:
        return 0
    return -1
arr=[0]
print(noble(arr))
