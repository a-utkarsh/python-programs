A=[1,3,-1]
best=-1000000000000

df=0
for i in range(len(A)):
    for j in range(len(A)-1,0,-1):
        df=abs(A[j]-A[i])+abs(i-j)
        best=max(df, best)
        
        #diff.append(df)
print(best)
