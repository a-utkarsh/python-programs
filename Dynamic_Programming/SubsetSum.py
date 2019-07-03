#Subset Sum using naive recursion
def subsetsum(arr,n,sum):
    if sum==0:
        return True
    if n==0 and sum!=0:
        return False
    if(sum<arr[n-1]):
        return subsetsum(arr,n-1,sum)
    return (subsetsum(arr,n-1,sum-arr[n-1]) or subsetsum(arr,n-1,sum))
arr=[3, 34, 4, 12, 5, 2]
sum=12
print(subsetsum(arr,len(arr)-1,sum))

#Subset sum using dynamic programming approach
def subsetsumDP(arr,n,sum):
    table=[[False for i in range(sum+1)] for j in range(n+1)]
    #If sum is 0, then answer is true
    for i in range(n+1):
        table[i][0]=True
    # If sum is not 0 and set is empty,then answer is false
    for j in range(1,sum+1):
        table[0][j]=False

    for i in range(1,n+1):
        for sm in range(1,sum+1):
            if sm<arr[i-1]:
                table[i][sm]=table[i-1][sm]
            if sm>=arr[i-1]:
                table[i][sm]=table[i-1][sm] or table[i-1][sm-arr[i-1]]
    return table[n][sum]



print(subsetsumDP(arr,len(arr)-1,sum))