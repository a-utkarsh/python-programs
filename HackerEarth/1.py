def squre(N):
    list1 = []
    while N>0:
        total=N*N
        N-=2
        list1.append(total)
    return sum(list1)

T=int(input())
Num=[]
for i in range(T):
    N= int(input())
    Num.append(N)
for j in Num:
    print(squre(j))