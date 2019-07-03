n = int(input())
temp = [0]*3
res = [0]*3
k = 0
for i in range(n,0,-1):

    a = list(map(int,input().split()))
    if(k == 0):
        k = 1
        for i in range(3):
            temp[i] = a[i]
    else:
        for i in range(3):
            res[i] = a[i] + min(temp[(i+1)%3], temp[(i+2)%3])
        temp = res[:]
print(min(temp))