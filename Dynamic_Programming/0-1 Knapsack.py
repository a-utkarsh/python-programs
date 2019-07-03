# Using Naive recursive solution
def kanpsack(n,c,p,w):
    if n==0 or c==0:
        return 0
    elif w[n]>c:
        return kanpsack(n-1,c,p,w)
    else:
        return max(p[n]+kanpsack(n-1,c-w[n],p,w),kanpsack(n-1,c,p,w))
val = [10,12,28]
wt = [1,2,4]
W = 6
n = len(val)-1
print( kanpsack(n,W,val,wt))

#using Dynamic programming
def knapsack(w,p,c):
    table=[[0 for i in range(c+1)]for j in range(len(w)+1)]
    for i in range(len(w)+1):
        for j in range(c+1):
            if i==0 or j==0:
                table[i][j]=0
            elif(w[i-1]<=j):
                table[i][j]=max(p[i-1]+table[i-1][j-w[i-1]],table[i-1][j])
            else:
                table[i][j]=table[i-1][j]
    return table[len(w)][c]
print(knapsack(wt,val,W))