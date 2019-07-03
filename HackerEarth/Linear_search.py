#A=[1,2,3,4,1]
n,key=map(int,input().split())
A=list(map(int,input().split()))

for i in range(len(A)-1,0,-1):
    if(A[i]==key):
        print(i+1)
        break
