def scorer(l1,l2):

    c1= list(map(int, input().split()))[:l1]
    c2= list(map(int, input().split()))[:l2]
    if sum(c1)>sum(c2):
        return "C1"
    else:
        return "C2"
T= int(input())
result=[]
for i in range(T):
    l1, l2 = map(int, input().split())
    result.append(scorer(l1,l2))
for i in result:
    print(i)