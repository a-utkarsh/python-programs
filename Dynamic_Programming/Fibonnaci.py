#Fibonnaci using bottom up
n = int(input())
fib = [0]*(n+1)
fib[1],fib[0] = 1,1
for i in range(2,n+1):
    fib[i] = fib[i-1]+fib[i-2]
print(fib[n-1])
#Fibonnici using top-down
fib = [0]*(n+1)
def fibn(n):
    if (fib[n]==0):
        if(n<=1):
            fib[n]=n
        else:
            fib[n]=fibn(n-1)+fibn(n-2)
    return fib[n]
print(fibn(n))
