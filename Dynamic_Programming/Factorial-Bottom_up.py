#Bottom up dynamic programming to find factorial
n=int(input())
F=[0]*(n+1)
F[0]=1
for i in range(1,n+1):
    F[i]=F[i-1]*i
print(F[n])
#Top to down dynamic programming to find factorial
def solve(n):
    if n==0:
        return 1
    if F[n]>0:
        return F[n]
    else:
        F[n]=n*solve(n-1)
        return F
print(solve(n))





