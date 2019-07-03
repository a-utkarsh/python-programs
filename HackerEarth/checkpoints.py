N = int(input())
X=[]
Y=[]
for i in range(N):
    x ,y = map(int, input().split())
    X.append(x)
    Y.append(y)
S=int(input())
count=0
for i in range(N):

    for j in range(N):
        if((X[i]-X[j])+(Y[i]-Y[j]))==S:
            count+=1
print(count)
