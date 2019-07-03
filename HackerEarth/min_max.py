A=[1,4,6,2,3]
L=[0,1,3]
R=[2,2,4]
X=[5,6,7]
temp=[]
for i in range(len(L)):
    x=(R[i]-L[i]+1)*X[i]
    temp.append(x)
temp.sort()
print(temp)
max=0
min=0
N=2
for i in range(N):
    min+=temp[i]
    max+=temp[len(temp)-N+i]
print(sum(A)+min, sum(A)+max)